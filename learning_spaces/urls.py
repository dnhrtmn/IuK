from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("reservation", api.reservationViewSet)
router.register("room", api.roomViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("learning_spaces/reservation/", views.reservationListView.as_view(), name="learning_spaces_reservation_list"),
    path("learning_spaces/reservation/create/", views.reservationCreateView.as_view(), name="learning_spaces_reservation_create"),
    # path("learning_spaces/reservation/create/", views.createReservation, name="learning_spaces_reservation_create"),
    # path("learning_spaces/reservation/create/<room>/", views.createReservation, name="learning_spaces_reservation_create"),
    path("learning_spaces/reservation/detail/<int:pk>/", views.reservationDetailView.as_view(), name="learning_spaces_reservation_detail"),
    path("learning_spaces/reservation/update/<int:pk>/", views.reservationUpdateView.as_view(), name="learning_spaces_reservation_update"),
    path("learning_spaces/room/", views.roomListView.as_view(), name="learning_spaces_room_list"),
    path("learning_spaces/room/create/", views.roomCreateView.as_view(), name="learning_spaces_room_create"),
    path("learning_spaces/room/detail/<int:pk>/", views.roomDetailView.as_view(), name="learning_spaces_room_detail"),
    path("learning_spaces/room/update/<int:pk>/", views.roomUpdateView.as_view(), name="learning_spaces_room_update"),
)
