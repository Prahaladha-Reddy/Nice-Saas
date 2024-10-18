from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir=pathlib.Path(__file__).resolve().parent

def home_view(request,*args,**kwargs):
  return about_view(request,*args,**kwargs)


def about_view(request,*args,**kwargs):
  qs=PageVisit.objects.all()
  page_qs=PageVisit.objects.filter(path=request.path)
  html_template='home.html'
  my_title='My page'
  my_context={
    'page_title':my_title,
    'totalvisits':qs.count(),
    'percent':page_qs.count()*100/qs.count(),
    'page_qs':page_qs.count()
  }
  path=request.path
  html_template='home.html'
  PageVisit.objects.create(path=request.path)
  return render(request,html_template,my_context)



