from django.urls import path

from financa import views


urlpatterns = [path("", views.home, name="home")]
