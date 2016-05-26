from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sms_app.models import *
from sms_app.forms import *

def manage_user(request):
    try:
        contact = Contact.objects.get(pk = request.POST['users_select'])
        contact = ContactForm(request.POST, instance = contact).save()
    except Contact.DoesNotExist:
        form_data = ContactForm(request.POST)
        form_data.save()
    return redirect('sms_app:manage_users')
    
def remove_user(request):
    Contact.objects.get(pk = request.POST['users_select']).delete()
    return redirect('sms_app:manage_users')

@login_required
def manage_users(request):
    if request.POST:
        if 'manage_user' in request.POST:
            manage_user(request)
        elif 'delete_user' in request.POST:
            remove_user(request)
        else: 
            raise Exception('Invalid action. ')
    contacts = Contact.objects.all()
    form = ContactForm()
    return render(request, 'sms_app/manage_users.html', {'users' : contacts, 'form' : form})
