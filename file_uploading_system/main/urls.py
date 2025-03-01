from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('upload/', views.FileUploadView.as_view()),
    path('delete/', views.FileDeleteView.as_view()),
]