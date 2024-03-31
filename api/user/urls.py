
from rest_framework import routers
from django.urls import path, include
from .views import UserDetails
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path("login/", views.signin, name='signin'),  # Corrected the name to 'signin'
    path('logout/<int:id>/', views.signout, name='signout'),
    path('<int:user_id>/', UserDetails.as_view(), name='user_details'),
    path('', include(router.urls))
]

