from django.shortcuts import render
from django.contrib import messages

from computer.models import Computer
from computer.forms import ComputerForm

def create_computers(request):
    if request.method == "POST":
        computer_form = ComputerForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if computer_form.is_valid():
            data = computer_form.cleaned_data
            actual_objects = Computer.objects.filter(
                brand=data["brand"], model=data["model"], description=data["description"], price=data["price"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"Computer {data['brand']} - {data['model']} - {data['description']} - {data['price']} ya está creado",
                )
            else:
                computer = Computer(brand=data["brand"], model=data["model"],description=data["description"], price=data["price"])
                computer.save()
                messages.success(
                    request,
                    f"Computer {data['brand']} - {data['model']} - {data['description']} -{data['price']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"computer": Computer.objects.all()},
                template_name="my_app/computer_list.html",
            )

    computer_form = ComputerForm(request.POST)
    context_dict = {"form": computer_form}
    return render(
        request=request,
        context=context_dict,
        template_name="my_app/computer_form.html",
    )

def computers(request):
    return render(
        request=request,
        context={"computers": Computer.objects.all()},
        template_name="my_app/computer_list.html",
    )