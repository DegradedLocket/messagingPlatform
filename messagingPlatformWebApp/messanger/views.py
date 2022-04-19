
from django.shortcuts import render
from matplotlib.style import context
from .models import Message
from .forms import MsgForm
#from datetime import datetime

# Create your views here.

def index(request):
    msgs = Message.objects.order_by("msgDate")
    context ={"msgs":msgs}

    return render(request, "messanger.html", context)

def sendmsg(request):
    form = MsgForm
    if request == "POST":
        form = MsgForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = MsgForm()
    return render(request, "messanger.hmtl", {"form":form})
