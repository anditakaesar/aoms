from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blog.models import BlogPost
from django.utils import timezone


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class PostListView(ListView):
    model = BlogPost
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
