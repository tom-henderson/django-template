from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.conf import settings

from django_common.views import LogOutRedirectView

import django.contrib.auth.views

admin.autodiscover()

urlpatterns = [
    path('login/', LoginView.as_view(), name='log_in'),
    path('logout/', LogOutRedirectView.as_view(), name='log_out'),
    path('admin/logout/', LogOutRedirectView.as_view()),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
