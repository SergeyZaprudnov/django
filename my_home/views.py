from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from my_home.models import Product, Category, Contacts


class IndexListView(ListView):
    model = Category
    extra_context = {
        'title': 'Главная'
    }


class ContactCreateView(CreateView):
    model = Contacts
    success_url = reverse_lazy('my_home:list')
    fields = ('name', 'email', 'message')
    extra_context = {
        'title': 'Контакты'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["title"] = "Наши контакты"
        return context_data


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }
