from django.urls import path
from . import views as room_views

app_name = "rooms"

urlpatterns = [path("", room_views.all_rooms, name="home")]
