from django.http import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Poll, Choice
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
'''
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
	
	return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))
	#return HttpResponse("This is poll %s." % poll_id)
	
def results(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	return render_to_response('polls/results.html', {'poll': p})
	#return HttpResponse("This is poll results %s." % poll_id)
'''	
def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selection = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render_to_response('polls/detail.html', {'poll':p, 'error_message': "You didn't select anything"},
			context_instance=RequestContext(request))
	else:
		selection.votes += 1
		selection.save()
		return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
		#return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
	return HttpResponse("This is poll vote %s." % poll_id)