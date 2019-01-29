from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response
from .models import Account, Client
from django.contrib.auth.models import User


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

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('login_page')
    else:
        return HttpResponse('Ты не залогинен')

def java(request):
    return render_to_response('java.html')

def register(request):
    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password'],
        email=request.POST['email']
    )
    client=Client(user=user)
    client.save()
    return HttpResponseRedirect('/login_page')

def registration_page(request):
    return render_to_response('registration_page.html')

def ajax_path(request):
    response = {
        'message': 10
        }
    return JsonResponse(response)

def notuniqlogin(request):
    if len(User.objects.filter(username=request.POST['login'])) == 0:
        response = True
    else:
        response = False
    return JsonResponse(response)
