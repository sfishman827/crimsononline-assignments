from django.http import HttpResponse, Http404
from polls.models import Poll, Choice
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
	latest = Poll.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('polls/index.html')
	c = Context({'latest_polls': latest,})
	return HttpResponse(t.render(c))
	#SHORTCUT:
	#return render_to_response('polls/index.html', {'latest_polls': latest})
	
def detail(request, poll_id):
	#try:
	#	p = Poll.objects.get(pk=poll_id)
	#except Poll.DoesNotExist:
	#	raise Http404
	
	#SHORTCUT:
	p = get_object_or_404(Poll, pk=poll_id)	
	
	return render_to_response('polls/detail.html', {'poll': p})
	#return HttpResponse("This is poll %s." % poll_id)
	
def results(request, poll_id):
	return HttpResponse("This is poll results %s." % poll_id)
	
def vote(request, poll_id):
	return HttpResponse("This is poll vote %s." % poll_id)