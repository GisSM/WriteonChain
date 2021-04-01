from django.shortcuts import render
from .utils import balance_eth

def about_site(request):
    return render(request,'homepage/about_site.html',{'balance':balance_eth()})
