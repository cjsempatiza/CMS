# -*- coding: utf-8 -*-
# coding=UTF-8
'''
    Sempatiza

    Desarrollado por Lastchance SL
    web: www.lastchance.es
    email: jao@lastchance.es
    Fecha: 2010
'''

from django.conf.urls.defaults import *
from web.views import *
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.contrib import sitemaps
from django.contrib.sitemaps import GenericSitemap
from proyectos.models import Proyecto

info_dict = {
    'queryset': Pagina.objects.exclude(es_activo=False),
    'date_field': 'actualizado_el',
}

proyectos_dict = {
    'queryset': Proyecto.objects.exclude(es_activo=False),
    'date_field': 'actualizado_el',
}

sitemaps = {
    'paginas_especiales': NamedURLSitemap(['index', 'quienes', 'tutoriales','testimonios']), #'proyectos','clientes',
    'paginas_generales' : GenericSitemap(info_dict, priority=0.5, changefreq='monthly'),
    #'paginas_proyectos' : GenericSitemap(proyectos_dict, priority=0.5, changefreq='monthly'),
}

urlpatterns = patterns('',

    url(r'^$', 'web.views.index', name='index',),
    url(r'^clientes/$', 'web.views.clientes', name='clientes',),
    url(r'^testimonios/$', 'web.views.testimonios', name='testimonios',),
    url(r'^testimonios/(?P<testi_cat>[^/]+)/$', 'web.views.testimonios_cat', name='testimonios_cat',),
    #url(r'^proyectos/$', 'web.views.proyectos', name='proyectos',),
    #url(r'^proyectos/(?P<slug_proy>[^/]+)/$', 'web.views.proyecto_detail', name='proyecto_detail',),
    url(r'^tutoriales/$', 'web.views.tutoriales', name='tutoriales',),
    url(r'^tutoriales/(?P<tag_fil>\w+)*/$', 'web.views.tutoriales', name='tutoriales_fil',),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^(?P<path>.*)/$', 'web.views.paginas', name='page'),
)
