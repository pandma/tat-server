from django.urls import path
from .views import Subpages_views

urlpatterns = [path("", Subpages_views.as_view())]
