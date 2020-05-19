from django.db import models
from django.urls import reverse
from django.utils import timezone



class reservation(models.Model):

    # Fields
    start_time = models.DateTimeField(default=timezone.now)
    # created = models.DateTimeField(default=timezone.now)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def publish(self):
        print(self)
        self.save()

    def get_absolute_url(self):
        return reverse("learning_spaces_reservation_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("learning_spaces_reservation_update", args=(self.pk,))


class room(models.Model):

    # Fields
    created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=100, editable=True)
    location = models.TextField()
    size = models.TextField(max_length=3, editable=True)

    class Meta:
        pass


    def __str__(self):
        return str(self.pk)

    def publish(self):
        self.save()

    def get_absolute_url(self):
        return reverse("learning_spaces_room_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("learning_spaces_room_update", args=(self.pk,))
