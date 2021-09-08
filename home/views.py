from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    #context = {
        #"variable1":"this is sent" ,    #this is set of variable sent
        #"variable2":"sada going to srinagar",
        #"variable3":"by road and train"  }
    messages.success(request,'welcome sada website yaro')
    return render(request, 'index.html')
    #return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Course = request.POST.get('course')
        Address = request.POST.get('address')
        School = request.POST.get('school')
        
        contact = Contact(name=Name, email=Email, phone=Phone,course=Course, address=Address, school=School, date=datetime.today())
        contact.save()
        messages.success(request,'your data get submit')
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')