from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'trydjango18.views.about', name='about'),
    url(r'^education/$', 'education.views.education', name='education'),
    url(r'^experience/$', 'experience.views.experience', name='experience'),
    url(r'^certificates/$', 'certificates.views.certificates', name='certificates'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),

]

#if settings.DEBUG:
#	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)