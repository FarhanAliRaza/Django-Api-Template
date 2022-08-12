
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from app import settings
from accounts.views import login_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', login_view, name='login'),
    path('api/', include('core.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
