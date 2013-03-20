from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll

#SLOW METHOD:
#urlpatterns = patterns('polls.views',
#	url(r'^$', 'index'),
#	url(r'^(?P<poll_id>\d+)/$', 'detail'),
#	url(r'^(?P<poll_id>\d+)/results/$', 'results'),
#	url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
#)

urlpatterns = patterns('polls.views',
	url(r'^$', 
		ListView.as_view(
			queryset = Poll.objects.order_by('-pub_date')[:5],
			context_object_name = 'latest_polls',
			template_name = 'polls/index.html')),
	url(r'^(?P<pk>\d+)/$',
		DetailView.as_view(
			model = Poll,
			template_name = 'polls/detail.html'),
		name='poll_detail'),
	url(r'^(?P<pk>\d+)/results/$',
		DetailView.as_view(
			model = Poll,
			template_name = 'polls/results.html'),
		name='poll_results'),
	url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)