from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index2/', Index2View.as_view(), name='index2')
]