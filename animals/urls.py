from django.urls import path
from animals import views

urlpatterns = [
    path("", views.main, name="main"),
    path("new_animal", views.new_animal, name="new_animal")
]