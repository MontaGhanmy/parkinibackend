from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'parkings', views.ParkingViewSet)
router.register(r'voitures', views.VoitureViewSet)
router.register(r'occupations', views.OccupationViewSet)
router.register(r'place', views.PlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notification/', views.NotificationView.as_view()),
    path('pricing/', views.PricingView.as_view()),
    path('api/auth/register/', views.RegisterAPI.as_view()),
    path('api/auth/login/', views.LoginAPI.as_view()),
    path('api/auth/user/', views.UserAPI.as_view()),
    path('api/auth/logout/', views.Logout.as_view()),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
