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
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView, FormMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.utils.translation import gettext
import datetime


def checkReservations(request):
    room = request.GET.get('room', None)
    date = request.GET.get('date', None)
    print(request.user)
    reservations = models.Reservation.objects.filter(created_by__exact=request.user)
    print(reservations)
    reservations = reservations.filter(start_time__gt=datetime.date.today())
    print(reservations)
    if not reservations:
        queryset = models.Reservation.objects.filter(room__iexact=room, start_time__exact=date).values("block")
        return JsonResponse({"models_to_return": list(queryset)})

    else:
        print("empty")
        return


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
        print(self.request.POST)

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
            template_name='email/subjectConfirmation.txt'
        ).strip()
        from_email = 'admin@learning-spaces.com'
        recipient = [reservation.created_by.email]



        message = render_to_string(
        'email/emailConfirmation.txt', {'user': reservation.created_by.email, 'id': reservation.identifier, 'date': reservation.start_time,
             'block': reservation.block, 'room': reservation.room}
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

        subject = render_to_string(
            template_name='email/subjectDelete.txt'

        ).strip()
        from_email = 'admin@learning-spaces.com'
        recipient = [self.object.created_by.email]

        message = render_to_string(
            'email/emailDelete.txt', {'user': self.object.created_by.email, 'userDelete': self.request.user.email, 'id': self.object.identifier, 'date': self.object.start_time,
             'block': self.object.block, 'room': self.object.room}
        )
        html_message = render_to_string(
            'email/emailDelete.html',
            {'user': self.object.created_by.email, 'id': self.object.identifier, 'date': self.object.start_time,
             'block': self.object.block, 'room': self.object.room}
        )

        mail.send_mail(subject, message, from_email, recipient, html_message=html_message)



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
    output = gettext('Das ist ein Test')
    return render(request, "home.html", {}, output)


def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

class roomReservationsView(TemplateView):
    model = models.Room
    pk_url_kwarg = "pk"
    template_name = 'room_reservations.html'

    def get_context_data(self, **kwargs):
        context = super(roomReservationsView, self).get_context_data(**kwargs)
        room_data = models.Room.objects.all()
        context.update({'room_data': room_data})
        return context

    def getReservations(request):
        room = request.GET.get('room', None)

        queryset = models.Reservation.objects.filter(room__iexact=room).values()

        return JsonResponse({"models_to_return": list(queryset)})

class contactForm(generic.CreateView):
    model = models.contactRequests
    form_class = forms.contactForm
    template_name = "learning_spaces/contact.html"


    def form_valid(self, form):
        contactRequest = form.save(commit=False)
        contactRequest.created_by = self.request.user


        # subject = render_to_string(
        #     template_name='email/subjectContactForm.txt'
        # ).strip()
        from_email = self.request.user.email
        recipient = ['admin@learning-spaces.com']

        message = render_to_string(
            'email/emailContactForm.txt', {'user': self.request.user.email, 'subject': contactRequest.subject, 'message': contactRequest.message}
        )
        html_message = render_to_string(
            'email/emailContact.html',
            {'user': self.request.user.email,'subject': contactRequest.subject, 'message': message}
        )

        mail.send_mail(contactRequest.subject, message, from_email, recipient, html_message=html_message)

        return super().form_valid(form)



class user_dashboard(TemplateView):
    template_name = "learning_spaces/user_dashboard.html"


    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(user_dashboard, self).get_context_data(**kwargs)
        userObject = models.User.object.all()
        reservation_data = models.Reservation.objects.filter(created_by__exact=user, start_time__gte=datetime.date.today())
        contact_data = models.contactRequests.objects.filter(created_by__exact=user)
        context['reservation_data'] = reservation_data
        context['contact_data'] = contact_data
        context['userObject'] = userObject
        return context

class UserUpdateView(generic.UpdateView):
    model = models.User
    form_class = forms.UserAdminChangeForm
    template_name = "learning_spaces/user_detail.html"



    def form_valid(self, form):
        print(self.request)
        user = form.save(commit=True)
        user.save()
        return super().form_valid(form)












