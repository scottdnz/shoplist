from django.shortcuts import render_to_response
#from django.http import HttpResponse

from interface.lib.items import fetch_items

# Create your views here.


def index(request):
    items = fetch_items()
    
    
    #return HttpResponse("Hello, world. You're at the ingredients index.")
    return render_to_response('ingredients_add.html', {'items': items})
    
