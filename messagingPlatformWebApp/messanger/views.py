
from django.shortcuts import get_object_or_404, render
from .models import Message

# Create your views here.

def index(request):
    msgs = Message.objects.order_by("msgDate")
    context ={"msgs":msgs}

    return render(request, "messanger.html", context)

#def m(request):
#    msgs = M
#    return render(request, "messanger.html", {"msg":msg})