from django.template import Context
from polls.models import Poll
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    # Grab all poll objects from db
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    c = Context({'latest_poll_list': latest_poll_list})

    return render_to_response('polls/index.html', c)

def detail(request, poll_id):
    return HttpResponse('This is the detail for %s.' % poll_id)

def result(request, poll_id):
    return HttpResponse('This is the result for %s.' % poll_id)

def vote(request, poll_id):
    return HttpResponse('This is the vote for %s.' % poll_id)



