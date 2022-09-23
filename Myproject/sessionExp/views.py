from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sesFunction(request,prdid):
    request.session.modified =  True

    if 'visit' in request.session:
        request.session['visit'] += 1

    else:
        request.session['visit'] = 1

    if 'product' in request.session:
        request.session['product'].append(prdid)
    else:
        request.session['product'] = ['prdid']

    print(request.session['product'])
    # return HttpResponse(f"I am activated {request.session['visit']}")

    resp = HttpResponse(f"I am activated {request.session['visit']}")
    if 'visit' in request.COOKIES:
        resp.set_cookie('visit', int(request.COOKIES['visit'])+1)
    # resp.set_cookie('cookie','I am a cookie')
    else:
        resp.set_cookie('visit',1)
    return resp
