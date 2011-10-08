

#===============================================================================
# import os 
# PPATH = os.path.join(  os.path.dirname(__file__))
# 
# stylesheets = os.path.join(  PPATH,'public/stylesheets' )
# images = os.path.join(  PPATH,'public/images' )
# javascript = os.path.join(  PPATH,'public/javascript' )
#===============================================================================


from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

import globale.admin
globale.admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover 
dajaxice_autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(globale.admin.site.urls)) ,
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

    
    #===========================================================================
    # (r'^globale/admin/media/stylesheets/(?P<PPA>.*)$', 'django.views.static.serve', {'document_root': stylesheets}),
    # (r'^globale/admin/media/images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': images}),
    # (r'^globale/admin/media/javascript/(?P<path>.*)$', 'django.views.static.serve', {'document_root': javascript}),
    #===========================================================================

)
