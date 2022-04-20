import logging
from django.shortcuts import render
from matplotlib.style import context
from .models import Message
from .forms import MsgForm
from datetime import datetime
from .encryption import aes

# Create your views here.

def index(request):
    #key = "TestKey"
    msgs = Message.objects.order_by("msgDate")

    context ={"msgs":msgs}

    return render(request, "messanger.html", context)

def sendmsg(request):
    key = "TestKey"
    msgs = Message.objects.order_by("msgDate")
    logging.debug(msgs)
    if request.method == "POST":
        msg = Message()
        msg.msgText = request.POST.get("msgContent")
        msg.msgText = aes.AESCipher(key).encrypt(msg.msgText)
        msg.msgDate = datetime.now()
        msg.userFrom = 12345

        msg.save()
        for msg in msgs:
            msgStr = msg.msgText[1:]
            msgBs = bytes(msgStr, "utf-8")
            msg.msgText = aes.AESCipher(key).decrypt(msgBs)
        context = {"msgs": msgs}
        return render(request, "messanger.html", context)
    else:
        for msg in msgs:
            msgStr = msg.msgText[1:]
            msgBs = bytes(msgStr, "utf-8")
            msg.msgText = aes.AESCipher(key).decrypt(msgBs)
        context = {"msgs": msgs}
        return render(request, "messanger.html", context)

