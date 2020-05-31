from django.views import generic
from . import models
from . import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.utils import timezone
from bootstrap_datepicker_plus import DatePickerInput
from .filters import reservationFilter
from django.core import serializers, mail
from django.test import TestCase
from django.http import JsonResponse, HttpResponse
from .models import Reservation
from django.views.generic.edit import DeleteView, FormMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.template.loader import render_to_string
import datetime


def checkReservations(request):
    room = request.GET.get('room', None)
    date = request.GET.get('date', None)

    queryset = models.Reservation.objects.filter(room__iexact=room, start_time__exact=date).values("block")

    return JsonResponse({"models_to_return": list(queryset)})


class reservationListView(generic.ListView):
    model = models.Reservation
    template_name = "learning_spaces/reservation_list.html"

    # form_class = forms.reservationForm

    # Filtert die Reservierungen zuerst nach Status des aktuellen Benutzers (Admin oder nicht). Ist der Benutzer ein Admin,
    # bekommt er alle Reservierungen angezeigt. Ist der Nutzer kein Admin, so bekommt er nur seine Reservierungen angezeigt.
    # Alle Nutzer haben die Möglichkeiten nach Räumen zu filtern.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_admin:
            context['filter'] = reservationFilter(self.request.GET, queryset=self.object_list.filter())
            return context
        else:
            context['filter'] = reservationFilter(self.request.GET,
                                                  queryset=self.object_list.filter(created_by=self.request.user))
            return context


class reservationCreateView(generic.CreateView):
    model = models.Reservation
    form_class = forms.reservationForm

    def get_context_data(self, **kwargs):
        context = super(reservationCreateView, self).get_context_data(**kwargs)
        some_data = models.Room.objects.all()
        context.update({'some_data': some_data})
        print(context)
        return context

    def form_valid(self, form):
        reservation = form.save(commit=False)
        reservation.created_by = self.request.user


        if 'save_block1' in self.request.POST:
            reservation.block = 1
        elif 'save_block2' in self.request.POST:
            reservation.block = 2
        elif 'save_block3' in self.request.POST:
            reservation.block = 3
        elif 'save_block4' in self.request.POST:
            reservation.block = 4
        elif 'save_block5' in self.request.POST:
            reservation.block = 5
        elif 'save_block6' in self.request.POST:
            reservation.block = 6
        elif 'save_block7' in self.request.POST:
            reservation.block = 7

        subject = render_to_string(
            template_name='email/subject.txt'
        ).strip()
        from_email = 'admin@learning-spaces.com'
        recipient = [reservation.created_by.email]



        message = render_to_string(
        'email/email.txt', {'user': reservation.created_by.email}
        )
        html_message = render_to_string(
            'email/email.html', {'user': reservation.created_by.email, 'id': reservation.identifier, 'date': reservation.start_time, 'block':reservation.block, 'room':reservation.room}
        )


        mail.send_mail(subject, message, from_email, recipient, html_message=html_message)

        return super().form_valid(form)



class reservationDetailView(generic.DetailView):
    model = models.Reservation
    form_class = forms.reservationForm


class reservationUpdateView(generic.UpdateView):
    model = models.Reservation
    form_class = forms.reservationForm
    pk_url_kwarg = "pk"


class reservationDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = models.Reservation
    success_url = '/'
    success_message = "'%(id) deleted..."
    pk_url_kwarg = "pk"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # identifier = self.object.identifier
        # identifier_str = str(identifier)
        # request.session['identifier'] = identifier_str
        # message = 'Reservation: ' + request.session['identifier'] + ' deleted successfully'
        # message.success(self.request, message)
        return super(reservationDeleteView, self).delete(request, *args, **kwargs)


class roomListView(generic.ListView):
    model = models.Room
    form_class = forms.roomForm


class roomCreateView(generic.CreateView):
    model = models.Room
    form_class = forms.roomForm

    def form_valid(self, form):
        room = form.save(commit=False)
        room.created_by = self.request.user
        print(self.request.user)
        return super().form_valid(form)


class roomDetailView(generic.DetailView):
    model = models.Room
    form_class = forms.roomForm


class roomUpdateView(generic.UpdateView):
    model = models.Room
    form_class = forms.roomForm
    pk_url_kwarg = "pk"


class homeView(generic.TemplateView):
    template_name = "home.html"


def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})


def login_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "login.html", {})
