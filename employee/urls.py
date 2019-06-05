from django.urls import path,include
from employee import views
from django.conf.urls import  url
urlpatterns = [

    path('',views.employee_list, name='employee_list'),
    path('<int:id>/details',views.employee_details,name='employee_details'),
    path('add/',views.employee_add,name='employee_add'),
    path('<int:id>/edit',views.employee_edit,name='employee_edit'),
    # path('<int:id>/delete', views.employee_delete,name='employee_delete'),

    url(r'^(?P<id>\d+)/delete/$', views.employee_delete,name='employee_delete'),



]
