from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import random
import string

# Create your views here.
def main(request):
    if request.method=="POST":
        message = request.POST['message']
        name = request.POST['name']
        contact =request.POST['contact']
        
        send_mail(
               "Cererea mesaj de catre " + name,
                        "pentru "+ message + " venita de la "+ name,
                        settings.EMAIL_HOST_USER,
                            [ settings.EMAIL_HOST_USER],
                
                            fail_silently=False,
                        )
    return render(request,"main.html")