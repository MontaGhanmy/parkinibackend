from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'parkings', views.ParkingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/register/', views.RegisterAPI.as_view()),
    path('api/auth/login/', views.LoginAPI.as_view()),
    path('api/auth/user/', views.UserAPI.as_view()),
    path('api/auth/logout/', views.Logout.as_view()),
    path('admin/', admin.site.urls),
]
