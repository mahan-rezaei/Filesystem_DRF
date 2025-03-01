from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('create_user/', views.UserCreateView.as_view()),
    path('get_users_list/', views.UserListView.as_view()),
    path('deactivate_user/<int:user_id>', views.UserDeActiveView.as_view()),
]
