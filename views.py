from django.shortcuts import render
# Create your views here.
def index(request):
    dest1= Destination()
    return render(request, "index.html",{'price':700})