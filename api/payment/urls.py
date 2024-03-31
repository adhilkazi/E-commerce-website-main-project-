from django.urls import path
from .import views
from .views import PaymentAPIViewSet

urlpatterns = [
    path('gettoken/<str:id>/<str:token>/',views.generate_token,name="token.generate"),
    path('process/<str:id>/<str:token>/',views.process_payment,name="payment.process"),
    path('',PaymentAPIViewSet.as_view(),name="payment"),
]