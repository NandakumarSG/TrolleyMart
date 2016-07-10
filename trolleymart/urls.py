from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trolleymart.views.home', name='home'),
    # url(r'^trolleymart/', include('trolleymart.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
from django.conf.urls import url

from registration.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
]
