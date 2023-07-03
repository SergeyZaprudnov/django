from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)
    return render(request, 'contacts.html')
