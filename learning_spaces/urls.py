from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Reservation", api.reservationViewSet)
router.register("Room", api.roomViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("learning_spaces/reservation/", views.reservationListView.as_view(), name="learning_spaces_reservation_list"),
    path("learning_spaces/reservation/create/", views.reservationCreateView.as_view(), name="learning_spaces_reservation_create"),
    # path("learning_spaces/Reservation/create/", views.createReservation, name="learning_spaces_reservation_create"),
    # path("learning_spaces/Reservation/create/<Room>/", views.createReservation, name="learning_spaces_reservation_create"),
    path("learning_spaces/reservation/detail/<uuid:pk>/", views.reservationDetailView.as_view(), name="learning_spaces_reservation_detail"),
    path("learning_spaces/reservation/update/<uuid:pk>/", views.reservationUpdateView.as_view(), name="learning_spaces_reservation_update"),
    path("learning_spaces/room/", views.roomListView.as_view(), name="learning_spaces_room_list"),
    path("learning_spaces/room/create/", views.roomCreateView.as_view(), name="learning_spaces_room_create"),
    path("learning_spaces/room/detail/<uuid:pk>/", views.roomDetailView.as_view(), name="learning_spaces_room_detail"),
    path("learning_spaces/room/update/<uuid:pk>/", views.roomUpdateView.as_view(), name="learning_spaces_room_update"),
    url(r'^ajax/checkReservations/$', views.checkReservations, name='checkReservations'),
    # url(r'^delete-entry/(?P<pk>\d+)/$', views.reservationDeleteView.as_view(), name='delete_reservation'),
    path("learning_spaces/Reservation/delete/<uuid:pk>/", views.reservationDeleteView.as_view(), name='delete_reservation'),
)
