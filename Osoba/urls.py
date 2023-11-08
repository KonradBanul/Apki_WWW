from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('jobs/', views.job_list),
    path('jobs/<int:pk>/', views.job_detail),
]
