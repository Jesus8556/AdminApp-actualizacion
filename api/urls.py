from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cuenta',views.CuentaView,basename="cuenta")

urlpatterns = [
    path('admin/',include(router.urls))
]