from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('I am working on django')
    return render(request, 'home/index.html',{})

def success_page(request):
    return HttpResponse("This is success page.")