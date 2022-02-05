from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Favorite City'

jet_admin_panel_urlpatterns = [
    path("jet/", include("jet.urls", "jet")),
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
] if settings.ENABLE_JET_ADMIN else []

urlpatterns = [
    *jet_admin_panel_urlpatterns,
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # Django debug toolbar
    import debug_toolbar
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
