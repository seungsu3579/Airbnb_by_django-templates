from django.urls import path
from rooms import views as rooms_views

urlpatterns = [path("", rooms_views.all_rooms, name="home")]
