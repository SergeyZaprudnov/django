from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from my_home.models import Product, Category, Contacts, Version
from my_home.product_form import ProductForm, VersionProduct


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'my_home/product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'my_home/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('my_home:product')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'my_home/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('my_home:product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_formset = inlineformset_factory(Product, Version, formset=VersionProduct, fields='__all__', extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = version_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = version_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'my_home/product_delete.html'
    success_url = reverse_lazy('my_home:product')


def contacts(request):
    return render(request, 'my_home/contacts_form.html')
