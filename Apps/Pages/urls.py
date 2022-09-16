from django.urls import path
from .views import Pages_views, One_page_views

urlpatterns = [
    path("", Pages_views.as_view()),
    path("/onepage", One_page_views.as_view()),
]
