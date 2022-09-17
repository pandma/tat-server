from django.urls import path
from .views import Subpages_views, One_subpage_view, find_by_page_id_view

urlpatterns = [
    path("", Subpages_views.as_view()),
    path("/onepage", One_subpage_view.as_view()),
    path("/subpages", find_by_page_id_view.as_view()),
]
