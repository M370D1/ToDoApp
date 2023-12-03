from django.urls import path, include

from ToDoApp.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, UserDetailsView, UserEditView, \
    UserDeleteView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='profile-details'),
        path('edit/', UserEditView.as_view(), name='profile-edit'),
        path('delete/', UserDeleteView.as_view(), name='profile-delete'),
    ]))
]
