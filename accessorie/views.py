from django.contrib import messages
from django.shortcuts import render

from accessorie.models import Accessorie
from accessorie.forms import AccessorieForm

def create_accessories(request):
    if request.method == "POST":
        accessorie_form = AccessorieForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if accessorie_form.is_valid():
            data = accessorie_form.cleaned_data
            actual_objects = Accessorie.objects.filter(
                brand=data["brand"], model=data["model"], description=data["description"], price=data["price"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"Accessorie {data['brand']} - {data['model']} - {data['description']} - {data['price']} ya está creado",
                )
            else:
                accessorie = Accessorie(brand=data["brand"], model=data["model"],description=data["description"], price=data["price"])
                accessorie.save()
                messages.success(
                    request,
                    f"Accessorie {data['brand']} - {data['model']} - {data['description']} -{data['price']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"accessorie": Accessorie.objects.all()},
                template_name="my_app/accessorie_list.html",
            )

    accessorie_form = AccessorieForm(request.POST)
    context_dict = {"form": accessorie_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/accessorie_form.html",
    )

def accessories(request):
    return render(
        request=request,
        context={"accessories": Accessorie.objects.all()},
        template_name="my_app/accessorie_list.html",
    )