from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('persons/update/<int:pk>/', views.person_update),
    path('persons/delete/<int:pk>/', views.person_delete),
    path('jobs/', views.job_list),
    path('jobs/<int:pk>/', views.job_detail),
    path('jobs/update/<int:pk>/', views.job_update_delete),
    path('jobs/delete/<int:pk>/', views.job_update_delete),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('jobs/<int:pk>/members/', views.job_members),
]
