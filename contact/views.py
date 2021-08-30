from django.shortcuts import render, redirect
from .models import contact
# Create your views here.


def Contact(request) :  
    name = request.POST['name'] 
    email = request.POST['email']
    message = request.POST['message']
    contact.objects.create(
        Name = name,
        Email = email,
        Message = message,
        
    )
    return redirect('/Home')


    

