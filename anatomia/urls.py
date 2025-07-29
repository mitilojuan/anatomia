# anatomia/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Explicitly define login and logout paths with flat template names
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), # <--- CHANGED
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # <--- CHANGED

    path('', include('anatomiapp.urls')),
]

# Serve media files during development. In production, a web server (like Nginx) would handle this.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)