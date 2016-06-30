from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^about/', views.about, name='rango-about'),
    url(r'^$', views.index, name='rango-index'),
]
