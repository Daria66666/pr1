from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import Account


def index(request):
    l = Account.objects.all()
    output = ' '.join([a.name for a in l])
    return HttpResponse(output)

def empty_page(request):
    context = {
    }
    return render_to_response('index.html', context)

def main_page(request):
    from datetime import datetime
    l = Account.objects.all()
    context = {
        'auth': request.user.is_authenticated,
        'name': request.user.username,
        'date': datetime.today(),
        'accounts': [
            str(a.value) for a in l
        ]
    }
    return render_to_response('main_page.html', context)


def login_user(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render_to_response('error.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('/main_page')

def login_page(request):
    return render_to_response('login_page.html')