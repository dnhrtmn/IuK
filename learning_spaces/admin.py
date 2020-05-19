from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User


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
        # "start_time",
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
        "created_by",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        # "description",
        # "location",
        # "size",
    ]


admin.site.register(models.reservation, reservationAdmin)
admin.site.register(models.room, roomAdmin)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)