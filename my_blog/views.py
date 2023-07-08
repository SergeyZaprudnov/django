from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from my_blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'description',)
    success_url = reverse_lazy('my_blog:list')
    extra_context = {
        'title': 'Добавить Блог'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'description',)
    extra_context = {
        'title': 'Редактирование Блога'
    }


    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('my_blog:view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogLDetailView(DetailView):
    model = Blog
    extra_context = {
        'title': 'Просмотр Блога'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.blog_views += 1
        self.object.save()
        return self.object



class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('my_blog:list')
    extra_context = {
        'title': 'Удаление Блога'
    }
