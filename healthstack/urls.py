
import os
from healthstack.settings import BASE_DIR
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from hospital import views

# For forgot password views and reset password views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user, name='login'),

    # App routes
    path('', include('hospital.urls')),
    path('doctor/', include('doctor.urls')),
    path('api/', include('api.urls')),
    path('hospital_admin/', include('hospital_admin.urls')),
    path('chat/', include('ChatApp.urls')),
    path('sslcommerz/', include('sslcommerz.urls')),
    path('pharmacy/', include('pharmacy.urls')),
    path('risk-checker/', include('risk_checker.urls')),
    


    # Debug toolbar
    path('__debug__/', include('debug_toolbar.urls')),

    # Password reset flow
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset-password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),
]

# ✅ Serve static and media files in dev mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(BASE_DIR, "static"))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


