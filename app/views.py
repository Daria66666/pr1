from django.http import HttpResponse
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
        'date': datetime.today(),
        'accounts': [
            str(a.value) for a in l
        ]
    }
    return render_to_response('main_page.html', context)