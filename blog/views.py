from django.views.generic import TemplateView, DetailView
from blog.models import BlogPost, Navigation
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class HomePageView(TemplateView):
    template_name = 'index.html'
    post_lists = BlogPost.objects.order_by('-created_date').filter(active=1)
    nav_lists = Navigation.objects.order_by('nav_priority').filter(active=1)

    def get_context_data(self, **kwargs):
        postpaginator = Paginator(self.post_lists, 3)  # show $ contacts per page
        page = self.request.GET.get('page')

        try:
            posts = postpaginator.page(page)
        except PageNotAnInteger:
            posts = postpaginator.page(1)
        except EmptyPage:
            posts = postpaginator.page(postpaginator.num_pages)

        context = super(HomePageView, self).get_context_data(**kwargs)
        context['nav_lists'] = self.nav_lists
        context['post_lists'] = posts
        return context


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    nav_lists = Navigation.objects.order_by('nav_priority').filter(active=1)
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['nav_lists'] = self.nav_lists
        return context

