from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^$', views.PostListView.as_view(), name='post-list'),
    url(r'^$', views.HomePageView.as_view(), name='home'),
]