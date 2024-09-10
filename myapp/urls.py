from django.urls import path
from . import views

urlpatterns = [
     path('recent-products/', views.RecentProductView.as_view(), name='recent-products'),
]
