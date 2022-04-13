
from django.shortcuts import render
# Create your views here.

def index(request):
    context ={"msg":"Hello There"}
    return render(request, "messanger.html", context)