from django.views import generic
from . import models
from . import forms
from django.shortcuts import render, redirect
from django.utils import timezone
from bootstrap_datepicker_plus import DatePickerInput
from .filters import reservationFilter

from .models import reservation


class reservationListView(generic.ListView):
    model = models.reservation
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
                context['filter'] = reservationFilter(self.request.GET, queryset=self.object_list.filter(created_by=self.request.user))
                return context


class reservationCreateView(generic.CreateView):
    model = models.reservation
    form_class = forms.reservationForm

    def get_form(self):
        form = super().get_form()
        form.fields['start_time'].widget = DatePickerInput(format='%d.%m.%Y')
        return form

def createReservation(request, room):
    {}.__format__(room)
    if request.method == "POST":
        form = forms.reservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.start_time = timezone.now()
            reservation.created_by = request.user
            # reservation.created = timezone.now()
            reservation.save()
            return redirect('reservation_list', pk=reservation.pk)
    else:
        form = forms.reservationForm()
        print(request)
    return render(request, 'learning_spaces/reservation_form.html', {'form':form})

class reservationDetailView(generic.DetailView):
    model = models.reservation
    form_class = forms.reservationForm


class reservationUpdateView(generic.UpdateView):
    model = models.reservation
    form_class = forms.reservationForm
    pk_url_kwarg = "pk"


class roomListView(generic.ListView):
    model = models.room
    form_class = forms.roomForm


class roomCreateView(generic.CreateView):
    model = models.room
    form_class = forms.roomForm

    def form_valid(self, form):
        room = form.save(commit=False)
        room.created_by = self.request.user
        print(self.request.user)
        return super().form_valid(form)


class roomDetailView(generic.DetailView):
    model = models.room
    form_class = forms.roomForm


class roomUpdateView(generic.UpdateView):
    model = models.room
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
