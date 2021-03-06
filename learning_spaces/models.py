from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, User)
from django.conf import settings
import uuid


class Reservation(models.Model):
    # Fields
    start_time = models.DateField(default=timezone.now)
    room = models.CharField(max_length=5, blank=True, default='', verbose_name="Room")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    # created = models.DateTimeField(default=timezone.now)
    block = models.CharField(max_length=1, blank=True, default='')
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def publish(self, request):
        print(self, request.user)
        self.save()

    def get_absolute_url(self):
        return reverse("learning_spaces_reservation_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("learning_spaces_reservation_update", args=(self.pk,))


class Room(models.Model):
    # Fields
    created = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=100, editable=True)
    location = models.TextField()
    size = models.TextField(max_length=3, editable=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="", null=True, blank=True)
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    beamer = models.BooleanField(default=False)
    whiteboard = models.BooleanField(default=False)
    board = models.BooleanField(default=False)



    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def publish(self):
        print(self)
        self.save()

    def get_absolute_url(self):
        return reverse("learning_spaces_room_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("learning_spaces_room_update", args=(self.pk,))


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
            Creates and saves a User with the given email and password.
            """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
            Creates and saves a staff user with the given email and password.
            """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
            Creates and saves a superuser with the given email and password.
            """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

    def create_studentuser(self, email, password, ):
        """
            Creates and saves a superuser with the given email and password.
            """
        user = self.create_user(
            email,
            password=password,
        )
        user.student = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=25, default="")
    last_name = models.CharField(max_length=25, default="")
    postalcode = models.IntegerField(default=0, blank=True)
    city = models.CharField(max_length=25, default="")
    adress = models.CharField(max_length=25, default="")
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    student = models.BooleanField(default=False) # a user who is a student
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)


    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    @property
    def is_student(self):
        "Is the user a student?"
        return self.student

    def get_update_url(self):
        return reverse("user_update", args=(self.pk,))

    def get_absolute_url(self):
        return reverse("user_update", args=(self.pk,))

    object = UserManager()

class contactRequests(models.Model):
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=400)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="", null=True, blank=True)
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def get_absolute_url(self):
        return reverse("contactForm")

    def get_update_url(self):
        return reverse("contactRequest_detail", args=(self.identifier,))

class spaceLeftoverRequest(models.Model):
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=400)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="", null=True, blank=True)
    targetUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="", null=True, blank=True, related_name="+")
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reservation = models.OneToOneField(
        Reservation,
        on_delete=models.CASCADE,
    )
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("requests_detail", args=(self.identifier,))



