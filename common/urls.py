from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('getshopinfo/', GetShopInfoView.as_view(), name='getshopinfo'),
    path('getcommondata/', GetCommonDataView.as_view(), name='getcommondata'),
]
