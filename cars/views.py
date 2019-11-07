from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm, DeleteForm

# Create your views here.
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})

def new_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            #car.name = form.name
            #car.model_type = form.model_type
            #car.make = form.make
            #car.ftype = form.ftype
            #car.remarks = form.remarks
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'cars/car_edit.html', {'form': form})

def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_edit.html', {"form": form})

"""def car_delete(request, pk):
    car_to_delete = get_object_or_404(Car, pk=name)
    if request.method == "POST":
        form = DeleteForm(request.POST, instance=car_to_delete)
        if form.is_valid():
            car_to_delete.delete()
            cars = Car.objects.all()
            return render(request, 'cars/car_list.html', {'cars': cars})
    else:
        form = DeleteForm(instance=car_to_delete)
    return render(request, 'cars/car_delete.html', {"form": form})
    """