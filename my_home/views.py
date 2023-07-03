from django.shortcuts import render

from my_home.models import Product


def index(request):
    return render(request, 'index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
    return render(request, 'contacts.html')


def product(request):
    products_for_all = Product.objects.all()
    context = {
        'title': 'Продукты',
        'object_list': products_for_all
    }
    return render(request, 'product.html', context)
