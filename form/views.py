from django.shortcuts import render,redirect,get_object_or_404
from form.serializer import FormSerializer
from form.models import ContactForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.



def home(request):
    dataset = ContactForm.objects.all()
    data = {
        'home_title':'THis is Home page',
        'dataset': dataset,
        }
    
    return render(request,'home.html',data)


@login_required(login_url='login')
def CreateForm(request):
    
    if request.method == "POST":
        form = FormSerializer(request.POST,request.FILES)
        if form.is_valid :
            form.save()
            return redirect('home')
        else:
            return HttpResponse("form data is invalid") 
    formdata =  FormSerializer()
    context = {'form':formdata}        
    return render(request,'form/ContactForm.html',context)

@login_required(login_url='login')
def UpdateForm(request,pk):
    
    formobject = get_object_or_404(ContactForm,id =pk)
    
    if(request.method == "POST"):
        form = FormSerializer(request.POST,request.FILES,instance=formobject)
        if form.is_valid :
            form.save()
            return redirect('home')
        else:
            return HttpResponse("form data is invalid") 
    formdata = FormSerializer(instance=formobject)
    context = {'form':formdata}
    return render(request,'form/ContactForm.html',context)

@login_required(login_url='login')
def DeleteForm(request,pk):
    try :
        formobject = get_object_or_404(ContactForm,id =pk)
        form = FormSerializer(request.POST,instance=formobject)
        if request.method == 'POST':
            formobject.delete()
            return redirect('home')
        context = {
            'form':form,
            'id': pk
        }
        return render(request,'form/DeleteConfirmation.html',context= context)
    except:
        return HttpResponse("id is invalid")

def ViewForm(request,pk):
    try:
        formobj = get_object_or_404(ContactForm,id =pk)        
        return render(request,'form/ViewFormData.html',{'form':formobj})
       
    except:
        return HttpResponse("Invalid Id")            



         




