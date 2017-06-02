from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blog.models import BlogPost, Navigation
from django.utils import timezone


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['nav_lists'] = Navigation.objects.all()
        return context
