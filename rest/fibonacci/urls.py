from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from fibonacci import views

urlpatterns = [
    path('fibonacci/', views.fibonacci_list),
    path('fibonacci/new/<int:size>', views.fibonacci_new),
    path('fibonacci/delete/<int:size>', views.fibonacci_delete),
]

urlpatterns = format_suffix_patterns(urlpatterns)