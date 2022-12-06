from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from computer.forms import CommentForm
from computer.forms import ComputerForm
from computer.models import Comment
from computer.models import Computer



class ComputerListView(ListView):
    model = Computer
    paginate_by = 3


class ComputerDetailView(DetailView):
    model = Computer
    template_name = "computer/computer_detail.html"
    fields = ["model", "brand", "description", "price", "image"]

    def get(self, request, pk):
        computer = Computer.objects.get(id=pk)
        comments = Comment.objects.filter(computer=computer).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "computer": computer,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)


class ComputerCreateView(LoginRequiredMixin, CreateView):
    model = Computer
    success_url = reverse_lazy("computer:computer-list")

    form_class = ComputerForm
    # fields = ["model", "brand", "description", "price", "image"]

    def form_valid(self, form):
        """Filter to avoid duplicate computers"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Computer.objects.filter(
            model=data["model"], brand=data["brand"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"The computer {data['model']} - {data['brand']} is already created",
            )
            form.add_error("name", ValidationError("Invalid action"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Computer {data['model']} - {data['brand']} sucessfuly created!",
            )
            return super().form_valid(form)


class ComputerUpdateView(LoginRequiredMixin, UpdateView):
    model = Computer
    fields = ["brand", "model", "description", "image", "price"]

    def get_success_url(self):
        computer_id = self.kwargs["pk"]
        return reverse_lazy("computer:computer-detail", kwargs={"pk": computer_id})

    def post(self):
        pass


class ComputerDeleteView(LoginRequiredMixin, DeleteView):
    model = Computer
    success_url = reverse_lazy("computer:computer-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        computer = get_object_or_404(Computer, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, computer=computer
        )
        comment.save()
        return redirect(reverse("computer:computer-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        computer = self.object.computer
        return reverse("computer:computer-detail", kwargs={"pk": computer.id})
