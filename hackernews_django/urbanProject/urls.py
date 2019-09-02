from django.conf.urls import url
from urbanProject import views

urlpatterns = [
    url(r'^$', views.newslist),
]
