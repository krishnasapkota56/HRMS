from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls
from Employee.views import loginView


urlpatterns = [
    path('inbox/notifications/',
         include(notifications.urls, namespace='notifications')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('employee/', include('Employee.urls', namespace='employee')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', loginView, name='default_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
