from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World!!!1')


def test(request):
    return HttpResponse('TestoTesto')

# Create your views here.
