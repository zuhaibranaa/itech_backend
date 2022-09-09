from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('ledger/', include('django_ledger.urls', namespace='django_ledger')),
    path('api/routeros/', include('RouterOS.urls')),
    path('api/users/', include('Users.urls')),
    path('api/accounting/', include('Accounting.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
