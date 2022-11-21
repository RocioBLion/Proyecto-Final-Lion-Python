from django.shortcuts import render
from django.contrib import messages
from home.forms import UserRegisterForm
from home.forms import UserUpdateForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    ) 
    
def register(request):
    form = UserRegisterForm(request.POST) if request.POST else UserRegisterForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("login")

    return render(
        request=request,
        context={"form": form},
        template_name="registration/register.html",
    )


@login_required
def user_update(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home:index")

    form = UserUpdateForm(model_to_dict(user))
    return render(
        request=request,
        context={"form": form},
        template_name="registration/user_form.html",
    )    