from django.shortcuts import redirect

def index(request):
    return redirect('sms_app:index')
