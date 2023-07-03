from django.shortcuts import render

from my_home.models import Product


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'index.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
    return render(request, 'contacts.html', context)


def product(request):
    products_for_all = Product.objects.all()
    context = {
        'title': 'Продукты',
        'object_list': products_for_all
    }
    return render(request, 'product.html', context)
