from django.urls import path
from . import views 
from django.conf import settings
from .views import *
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('myprofile/', views.my_profile, name='myprofile'),
    path('lightningview/', views.lightning_view, name='lightning_view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register, name='register'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

