from django.urls import reverse_lazy
from django.views.generic import CreateView
from my_blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'slug', 'description',)
    success_url = reverse_lazy('my_home:index')
