from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.forms import modelformset_factory
from django.core.mail import send_mail
from .forms import userform, itemform
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Users, Items
from firstapp import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/auth/login')
def addusers(req):
    if req.method == 'POST':
        form = userform(req.POST)
        if form.is_valid():

            return HttpResponseRedirect('/thanks/')
    else:
        form = userform()

    return render(req, 'addusers.html', {'form': form})


@login_required(login_url='/auth/login')
def additems(req,action,oid):  
    if (action=="edit" or action=="add"):
        if action=="edit":
            items =models.Items.objects.get(pk=oid)
            form = itemform(req.POST or None, instance=items)
        else:
            form = itemform(req.POST)
            if not(form.is_valid()):
                form = itemform()
        d={
            "form": form
        }
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/firstapp/listitems')
        return render(req, 'additems.html',d)
    elif action=="del":
        models.Items.objects.get(pk=oid).delete()
        return HttpResponseRedirect('/firstapp/listitems')
    else:
        form = itemform()
        return render(req, 'additems.html', {'form': form})


@login_required(login_url='/auth/login')
def listitems(req):
    items = models.Items.objects.all()
    d={
        "items":items
    }
    return render(req,'listitems.html',d)

    


# if form.is_valid():
#     subject = form.cleaned_data['subject']
#     message = form.cleaned_data['message']
#     sender = form.cleaned_data['sender']
#     cc_myself = form.cleaned_data['cc_myself']

#     recipients = ['info@example.com']
#     if cc_myself:
#         recipients.append(sender)

#     send_mail(subject, message, sender, recipients)
#     return HttpResponseRedirect('/thanks/')
   

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



