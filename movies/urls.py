from django.conf.urls import url
from . import views

app_name = 'movies'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/', views.DetailView.as_view(), name='detail'),
    url(r'^previous/', views.PreviousView.as_view(), name='previous'),
    # url(r'^?q=(?P<filter_by>[a-zA_Z]+)/$', views.DetailView.as_view(), name='movies'),
]
