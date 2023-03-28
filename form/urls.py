from django.urls import path
from form.views import home,Form,CreateForm


urlpatterns = [
    path('',home,name='home'),
    path('form/',Form,name="Form"),
    path('create/',CreateForm,name='CreateForm'),

]    
