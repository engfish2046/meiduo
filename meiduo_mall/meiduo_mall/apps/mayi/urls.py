from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mayi/authorization/$', views.MayiURLView.as_view()),
    # url(r'^qq/user/$', views..as_view()),
]