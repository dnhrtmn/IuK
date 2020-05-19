from django.contrib import admin
from django import forms

from . import models


class reservationAdminForm(forms.ModelForm):

    class Meta:
        model = models.reservation
        fields = "__all__"


class reservationAdmin(admin.ModelAdmin):
    form = reservationAdminForm
    list_display = [
        "start_time",

    ]
    readonly_fields = [
        "start_time",
    ]


class roomAdminForm(forms.ModelForm):

    class Meta:
        model = models.room
        fields = "__all__"


class roomAdmin(admin.ModelAdmin):
    form = roomAdminForm
    list_display = [
        "created",
        "last_updated",
        "description",
        "location",
        "size",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "description",
        "location",
        "size",
    ]


admin.site.register(models.reservation, reservationAdmin)
admin.site.register(models.room, roomAdmin)
