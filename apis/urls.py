from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^news/', views.get_news),
    url(r'^new/', views.add_news),
    url(r'^news2/', views.get_news2),
]