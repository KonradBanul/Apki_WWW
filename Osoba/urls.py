from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.OsobaList.as_view()),
    path('snippets/<int:pk>/', views.OsobaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
