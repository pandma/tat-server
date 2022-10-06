from django.urls import path
from .views import Tasks_views, One_task_view, Find_by_subpage_id_view


urlpatterns = [
    path("", Tasks_views.as_view()),
    path("/subpage", Find_by_subpage_id_view.as_view()),
    path("/task", One_task_view.as_view()),
]
