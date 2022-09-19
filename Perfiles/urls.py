from django.urls import path
from Perfiles.views import AvatarUpdateView, CustomLogoutView, UserUpdateView, login_request, register, userCreateAvatar

urlpatterns = [
    path('signup/', register, name="signup"),
    path('login/', login_request, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('update-user/', UserUpdateView.as_view(), name="update-user"),
    path('crear-avatar/', userCreateAvatar, name="crear-avatar"),
    path('update-avatar/<int:pk>/', AvatarUpdateView.as_view(), name="update-avatar"),
] 
