from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs): 
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello Contact</h1>')
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
        "title": "this is about us",
        "my_number": 456,
        "my_list": [123, 456, 3241],
        "my_html": '<h1>Hello World</h1>'
    }
    return render(request, 'about.html', my_context)    