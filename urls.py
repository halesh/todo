from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('todo.views',
    # Examples:
    url(r'^home/', 'home_page', {'home_template': 'home.html'}),
    url(r'^todo/(?P<state>\w+)/(?P<todo_id>\w+)/$', 'change_todo'),
    url(r'^filterdate/(?P<date_filter_type>\w+)/$', 'filter_todo'),
    # url(r'^todo/', include('todo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
