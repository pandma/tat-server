from django.urls import path
from .views import Tasks_views

urlpatterns = [
    path("", Tasks_views.as_view()),
]
