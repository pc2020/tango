from django.shortcuts import render
from django.http import HttpResponse
import os

# http://www.tangowithdjango.com/book17/chapters/templates_static.html

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    context_dict = {'boldmessage': "I am bold font from the context", 'basedir' : BASE_DIR }

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'rango/index.html', context_dict)
    #    return HttpResponse("Rango says hey there world wide web! Here is the <a href='/rango/about' />about page</a>")
