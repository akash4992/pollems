from django.urls import path,include
from pollingapp import views
from django.conf.urls import  url
urlpatterns = [

    path('add/', views.PollView.as_view(), name='poll_add'),
    path('<int:id>/edit/', views.PollView.as_view(), name='poll_edit'),

    url(r'^(?P<id>\d+)/delete/$', views.delete,name='poll_delete'),
    path('',views.index, name='polls_list'),
    path('<int:id>/details/',views.details, name="poll_details"),
    url(r'^(?P<id>\d+)/$', views.poll,name='single_poll'),



]
