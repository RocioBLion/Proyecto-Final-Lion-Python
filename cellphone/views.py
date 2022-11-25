from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from cellphone.models import Cellphone
from cellphone.forms import CellphoneForm
from cellphone.models import Comment
from cellphone.forms import CommentForm


class CellphoneListView(ListView):
    model = Cellphone
    paginate_by = 3


class CellphoneDetailView(DetailView):
    model = Cellphone
    template_name = "cellphone/cellphone_detail.html"
    fields = ["brand", "model", "description", "price"]

    def get(self, request, pk):
        cellphone = Cellphone.objects.get(id=pk)
        comments = Comment.objects.filter(cellphone=cellphone).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "cellphone": cellphone,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class CellphoneCreateView(LoginRequiredMixin, CreateView):
    model = Cellphone
    success_url = reverse_lazy("cellphone:cellphone-list")

    form_class = CellphoneForm
    # fields = ["name", "code", "description", "image"]

    def form_valid(self, form):
        """Filter to avoid duplicate cellphones"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Cellphone.objects.filter(
            brand=data["brand"], model=data["model"], description=data["description"], price=data["price"], image=data["image"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"The Cellphone {data['brand']} - {data['model']} is already created",
            )
            form.add_error("name", ValidationError("invalid action"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Cellphone {data['brand']} - {data['model']} successfully created",
            )
            return super().form_valid(form)


class CellphoneUpdateView(LoginRequiredMixin, UpdateView):
    model = Cellphone
    fields = ["brand", "model", "description", "price", "image"]

    def get_success_url(self):
        cellphone_id = self.kwargs["pk"]
        return reverse_lazy("cellphone:cellphone-detail", kwargs={"pk": cellphone_id})

    # def post(self):
        # pass


class CellphoneDeleteView(LoginRequiredMixin, DeleteView):
    model = Cellphone
    success_url = reverse_lazy("cellphone:cellphone-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        cellphone = get_object_or_404(Cellphone, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, cellphone=cellphone
        )
        comment.save()
        return redirect(reverse("cellphone:cellphone-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        cellphone = self.object.cellphone
        return reverse("cellphone:cellphone-detail", kwargs={"pk": cellphone.id})

