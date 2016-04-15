from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from sms_app.models import Contact, MessageTemplate

def query_users_from_get_args(request, users):
    if request.GET :
        if request.GET.get('name'):
            users = users.filter(name = request.GET['name'])
        if request.GET.get('address'):
            users = users.filter(address = request.GET['address'])
        if request.GET.get('balance'):
            users = users.filter(balance = request.GET['balance'])
        if request.GET.get('contact_type'):
            users = users.filter(contact_type = request.GET['contact_type'])    
    return users

def log_out(request):
    logout(request)
    return redirect('/sms_app')
    
@login_required
def sms_template_index(request):
    users = Contact.objects.all()
    test_contact = users.all().filter(name = 'Test User')[0]
    if request.POST : 
        new_template = MessageTemplate(template_text = request.POST['sms_template'], template_title = request.POST['template_title'])
        if new_template.save():
            messages.success(request, 'Template saved successfuly')
    sms_templates = MessageTemplate.objects.all()
    return render(request, 'sms_app/sms_template_index.html', {'sms_templates' : sms_templates, 'test_contact' : test_contact})

@login_required
def view_sms_template(request, sms_id):
    old_template = MessageTemplate.objects.all().filter(pk = sms_id)[0]
    users = Contact.objects.all()
    test_contact = users.all().filter(name = 'Test User')[0]
    if request.POST : 
        old_template.template_text = request.POST.get('sms_template')
        old_template.save()
    users = query_users_from_get_args(request, users)
    return render(request, 'sms_app/view_sms_template.html', {'sms_template' : old_template.template_text, 'test_contact' : test_contact, 'queried_users' : users})
    
@login_required
def send_sms(request):
    users = query_users_from_get_args(request, Contact.objects.all())
    print '\n'.join(['Texting ' + x.name + ' with phone number ' + x.phone_number for x in users])
    return redirect('sms_app:sms_template_index')
