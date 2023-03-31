from django.urls import path
from form.views import home,CreateForm,UpdateForm,DeleteForm,ViewForm


urlpatterns = [
    path('',home,name='home'),
    path('create/',CreateForm,name='create'),
    path('update/<str:pk>/',UpdateForm,name = 'update'),
    path('delete/<str:pk>/',DeleteForm,name = 'delete'),
    path('view/<str:pk>/',ViewForm,name = 'view')

]    
