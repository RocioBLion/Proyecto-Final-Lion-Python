from django.urls import path

from computer import views

app_name = "computer"
urlpatterns = [
    path("courses/", views.ComputerListView.as_view(), name="course-list"),
    path("course/add/", views.ComputerCreateView.as_view(), name="course-add"),
    path("course/<int:pk>/detail/", views.ComputerDetailView.as_view(), name="course-detail"),
    path("course/<int:pk>/update/", views.ComputerUpdateView.as_view(), name="course-update"),
    path("course/<int:pk>/delete/", views.ComputerDeleteView.as_view(), name="course-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]
