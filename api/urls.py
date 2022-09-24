from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router=DefaultRouter()
router.register('home',views.NetflixView)
router.register('Signup', views.SignupView,basename='test')



urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.LoginView.as_view())
]
