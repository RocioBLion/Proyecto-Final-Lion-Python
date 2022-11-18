from django.shortcuts import render

from django.contrib import messages

from cellphone.models import Cellphone
from cellphone.forms import CellphoneForm


def create_cellphones(request):
    if request.method == "POST":
        cellphone_form = CellphoneForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if cellphone_form.is_valid():
            data = cellphone_form.cleaned_data
            actual_objects = Cellphone.objects.filter(
                brand=data["brand"], model=data["model"], description=data["description"], price=data["price"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"Cellphone {data['brand']} - {data['model']} - {data['description']} - {data['price']} ya está creado",
                )
            else:
                cellphone = Cellphone(brand=data["brand"], model=data["model"],description=data["description"], price=data["price"])
                cellphone.save()
                messages.success(
                    request,
                    f"Cellphone {data['brand']} - {data['model']} - {data['description']} -{data['price']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"cellphone": Cellphone.objects.all()},
                template_name="cellphone/cellphone_list.html",
            )

    cellphone_form = CellphoneForm(request.POST)
    context_dict = {"form": cellphone_form}
    return render(
        request=request,
        context=context_dict,
        template_name="cellphone/cellphone_form.html",
    )

def cellphones(request):
    return render(
        request=request,
        context={"cellphones": Cellphone.objects.all()},
        template_name="cellphone/cellphone_list.html",
    )
