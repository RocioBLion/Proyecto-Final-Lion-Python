from django.urls import path

from computer import views

app_name = "computer"
urlpatterns = [
    path("computers/", views.ComputerListView.as_view(), name="computer-list"),
    path("computer/add/", views.ComputerCreateView.as_view(), name="computer-add"),
    path("computer/<int:pk>/detail/", views.ComputerDetailView.as_view(), name="computer-detail"),
    path("computer/<int:pk>/update/", views.ComputerUpdateView.as_view(), name="computer-update"),
    path("computer/<int:pk>/delete/", views.ComputerDeleteView.as_view(), name="computer-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]
