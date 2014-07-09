from django.conf.urls import patterns, url
from graminbazaar import views

urlpatterns=patterns('',
	url(r'^$',views.index, name='index'),
	#url(r'init_graphs',views.init_graphs, name='init_graphs'),
)
