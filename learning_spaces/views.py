from django.views import generic
from . import models
from . import forms
from django.shortcuts import render, redirect
from django.utils import timezone
from bootstrap_datepicker_plus import DateTimePickerInput


class reservationListView(generic.ListView):
    model = models.reservation
    form_class = forms.reservationForm


class reservationCreateView(generic.CreateView):
    model = models.reservation
    form_class = forms.reservationForm
    def get_form(self):
        form = super().get_form()
        form.fields['start_time'].widget = DateTimePickerInput()
        return form

def createReservation(request, room):
    {}.__format__(room)
    if request.method == "POST":
        form = forms.reservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.start_time = request.user
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
