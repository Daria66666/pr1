from django.http import HttpResponse

from .models import Account


def index(request):
    l = Account.objects.all()
    output = ' '.join([a.name for a in l])
    return HttpResponse(output)