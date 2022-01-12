"""Platzigram Views"""

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime

def hello_world(request): 
    """Return a greeting"""
    # now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    # return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))
    return HttpResponse('Oh hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sort_integers(request):
    # # import pdb; pdb.set_trace()
    numbers = sorted(request.GET['numbers'].split(','))
    data = {
        'status': 'ok',
        'numbers': numbers,
        'msg': 'Integers sorted succesful'
    }
    return JsonResponse(data, safe=False)

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome'.format(name)
    return HttpResponse(message)