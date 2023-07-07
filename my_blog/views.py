from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from my_blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'description',)
    success_url = reverse_lazy('my_blog:list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'description',)
    success_url = reverse_lazy('my_blog:list')


class BlogListView(ListView):
    model = Blog


class BlogLDetailView(DetailView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('my_blog:list')
