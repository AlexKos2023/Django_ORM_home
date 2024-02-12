from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render

from main.models import Car, Client, Sale


def cars_list_view(request):
    cars = Car.objects.all()  # Получаем все объекты модели Car из базы данных
    context = {
        'cars': cars,  # Передаем объекты Car в контекст шаблона
    }
    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    context = {
        'car': car,
    }
    sales = Sale.objects.filter(car=car)  # Получаем все продажи, связанные с этим автомобилем
    clients = [sale.client for sale in sales]  # Получаем всех клиентов из продаж
    return render(request, 'main/details.html', {'car': car, 'clients': clients})

def sales_by_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)  # Получаем объект Car по его id
    try:
        sales = Sale.objects.filter(car=car)  # Получаем все продажи для данного автомобиля
        clients = []
        for sale in sales:
            clients.append(sale.client)
        context = {
            'car': car,  # Передаем объект Car в контекст шаблона
            'sales': sales,  # Передаем список продаж в контекст шаблона
            'clients': clients,  # Передаем список клиентов в контекст шаблона
        }
        template_name = 'main/sales.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
