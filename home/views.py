import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.shortcuts import render
from home.forms import UserRegisterForm
from home.forms import UserUpdateForm
from computer.models import Computer
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import login, logout, authenticate

from home.forms import AvatarForm
from home.models import Avatar

def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"avatar_url": avatars[0].image.url}
    return {}

def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    ) 
    
def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        computers = Computer.objects.filter(query)
        
        context_dict.update(
            {
                "computers": computers,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )
    
def avatar_load(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid and len(request.FILES) != 0:
            image = request.FILES["image"]
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect("home:index")

    form = AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="home/avatar_form.html",
    )

def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"register.html", {"mensaje":"Usuario Creado :)"})

    else:
        form = UserCreationForm()
        #form = UserRegistrationForm()

    return render(request,"register.html" , {"form":form})

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
        template_name="user_form.html",
    )        


def login_request(request):

    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=user, password=contra)

            if user is not None:
                login(request, user)

                return render(request,"index.html", {"mensaje":f"Bienvenido {usuario}"})

            else:

                return render(request,"index.html", {"mensaje":"Error,datos incorrectos"})

        else:

                return render(request,"index.html", {"mensaje":"Error,formulario erroneo"})

    
    form = AuthenticationForm()

    return render(request,"login.html", {'form':form})