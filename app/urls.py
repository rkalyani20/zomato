from django.urls import path
from app.views import *

urlpatterns = [
    path('restaurant/', RestaurantApi.as_view()),
    path('signup/',SignupApi.as_view()),
    path('placeorder/',Placeorder.as_view()),
    path('addmenu/',MenuApi.as_view()),
    path('showmenu/',ShowMenuApi.as_view()),
    path('showorder/',ShowOrderApi.as_view()),


]   