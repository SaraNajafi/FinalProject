from django.contrib import admin
from django.urls import path
from website.views import *
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'website'

urlpatterns = [
    # path('', index_view, name='index'),
    # path('about', about_view, name='about'),
    # path('contact', contact_view, name='contact'),
    # path('newsletter', newsletter_view, name='newsletter'),
    # path('', TemplateView.as_view(template_name='comming-soon.html'), name='comming_soon'),
    # path('about/', RedirectView.as_view(url='/comming_soon/')),
    # path('contact/', RedirectView.as_view(url='')),
    # path('newsletter/', RedirectView.as_view(url='')),
    path('', RedirectView.as_view(url='/initial-page/')),
    path('about/', RedirectView.as_view(url='/initial-page/')),
    path('contact/', RedirectView.as_view(url='/initial-page/')),
    path('newsletter/', RedirectView.as_view(url='/initial-page/')),
    # other URL patterns...
    path('initial-page/', initial_page_view, name='initial-page'),
]
