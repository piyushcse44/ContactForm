from django.shortcuts import render,redirect,get_object_or_404
from form.serializer import FormSerializer
from form.models import ContactForm
from django.http import HttpResponse

# Create your views here.



def home(request):
    dataset = ContactForm.objects.all()
    data = {
        'home_title':'THis is Home page',
        'dataset': dataset,
        }
    
    return render(request,'home.html',data)



def CreateForm(request):
    
    if request.method == "POST":
        form = FormSerializer(request.POST)
        if form.is_valid :
            form.save()
            return redirect('home')
        else:
            return HttpResponse("form data is invalid") 
    formdata =  FormSerializer()
    context = {'form':formdata}        
    return render(request,'form/ContactForm.html',context)


def UpdateForm(request,pk):
    
    formobject = get_object_or_404(ContactForm,id =pk)
    
    if(request.method == "POST"):
        form = FormSerializer(request.POST,instance=formobject)
        if form.is_valid :
            form.save()
            return redirect('home')
        else:
            return HttpResponse("form data is invalid") 
    formdata = FormSerializer(instance=formobject)
    context = {'form':formdata}
    return render(request,'form/ContactForm.html',context)

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



         




