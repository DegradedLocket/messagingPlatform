
from django.shortcuts import render
from matplotlib.style import context
from .models import Message
from .forms import MsgForm
from datetime import datetime

# Create your views here.

def index(request):
    msgs = Message.objects.order_by("msgDate")
    context ={"msgs":msgs}
    
    return render(request, "messanger.html", context)

def sendmsg(request):
    msgs = Message.objects.order_by("msgDate")
    context ={"msgs":msgs}
    if request.method == "POST":
        msg = Message()
        msg.msgText = request.POST.get("msgContent")
        msg.msgDate = datetime.now()
        msg.userFrom = 12345
        
        msg.save()
        return render(request, "messanger.html", context)
    else:
        return render(request, "messanger.html", context)
