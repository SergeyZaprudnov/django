from django.shortcuts import render
from django.views.generic import ListView

from my_home.models import Product, Category


class IndexListView(ListView):
    model = Category
    extra_context = {
        'title': 'Главная'
    }


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


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }


