from django.shortcuts import render

from my_home.models import Product


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'index.html', context)


def contacts(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    subjects = request.POST.get('subjects')
    message = request.POST.get('message')
    print(f'"Имя" {name}\n"Емэйл" {email}\n"Тема сообщения" {subjects}\n"Сообщение" {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'contacts.html', context)


def product(request):
    products_for_all = Product.objects.all()
    context = {
        'title': 'Продукты',
        'object_list': products_for_all
    }
    return render(request, 'product.html', context)
