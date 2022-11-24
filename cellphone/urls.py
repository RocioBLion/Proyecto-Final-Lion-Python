from django.urls import path

from cellphone import views

app_name = "cellphone"
urlpatterns = [
    path("cellphones/", views.CellphoneListView.as_view(), name="cellphone-list"),
    path("cellphone/add/", views.CellphoneCreateView.as_view(), name="cellphone-add"),
    path("cellphone/<int:pk>/detail/", views.CellphoneDetailView.as_view(), name="cellphone-detail"),
    path("cellphone/<int:pk>/update/", views.CellphoneUpdateView.as_view(), name="cellphone-update"),
    path("cellphone/<int:pk>/delete/", views.CellphoneDeleteView.as_view(), name="cellphone-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]
