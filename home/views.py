from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples = [
        {'name': "kashem khan", 'age': 33},
        {'name': "Shanto islam", 'age': 37},
        {'name': "Shanti islam", 'age': 22},
        {'name': "Rohan khureshi", 'age': 28},
    ]
    return render(request, "index.html", context={"peoples":peoples,"page": "Home"})

def contact(request):
    return render(request, "contact.html", context={'page': 'contact'})

def about(request):
    return render(request, "about.html", context={'page': 'about'})