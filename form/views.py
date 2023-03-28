from django.shortcuts import render,redirect
from form.serializer import FormSerializer
from form.models import ContactForm
from django.http import HttpResponse

# Create your views here.



def home(request):
    return render(request,'home.html')

def Form(request):
    formdata =  FormSerializer()
    return render(request,'form/ContactForm.html',{'form':formdata}) 

def CreateForm(request):
    
    if request.method == "POST":
        form = FormSerializer(request.POST)
        if form.is_valid :
            form.save()
            return redirect('home')
        else:
            return HttpResponse("good") 
    formdata =  FormSerializer()
    context = {'form':formdata}        
    return render(request,'form/ContactForm.html',context)


