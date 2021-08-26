from django.shortcuts import render
from About.models import About , Experience , Skill ,Link
from Services.models import Services
from portfolio.models import portfolio
from testimonial.models import testimonial
from .models import Home
from django.http import HttpResponse
# Create your views here.

def Home(request) :
    about=About.objects.last()
    experience=Experience.objects.all()
    skill=Skill.objects.all()
    link=Link.objects.all()
    services=Services.objects.all()
    portfolio1=portfolio.objects.all()
    testimonial1=testimonial.objects.all()
    print(testimonial1)
    context= {'about':about,
             'experience':experience ,
             'skill':skill,
             'link':link,
             'services':services,
             'portfolio1':portfolio1,
             'testimonial1':testimonial1}
    return render(request,'Home/index.html',context)
