from django.urls import path, reverse_lazy, include
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from accounts.views import (
    UserCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
)

app_name = 'users'

user_patterns = [
    path('<username>/', UserDetailView.as_view(), name='user_detail'),
    path('<username>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<username>/delete/', UserDeleteView.as_view(), name='user_delete'),
]

urlpatterns = [
    # Login, Logout, Register
    path('login/', LoginView.as_view(
        template_name='accounts/registration/login.html',
        redirect_authenticated_user=True),
        name='login'
    ),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # Password Change
    path('password/change/', PasswordChangeView.as_view(
        template_name='accounts/registration/password_change.html',
        success_url=reverse_lazy('users:password_change_done')),
        name='password_change'),
    path('password/change/done/', PasswordChangeDoneView.as_view(
        template_name='accounts/registration/password_change_done.html'),
        name='password_change_done'),
    # Password Reset
    path('password/reset/', PasswordResetView.as_view(
        template_name='accounts/registration/password_reset.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.html',
        success_url=reverse_lazy('users:password_reset_done')),
        name='password_reset'),
    path('password/reset/done/', PasswordResetDoneView.as_view(
        template_name='accounts/registration/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accounts/registration/password_reset_confirm.html',
        success_url=reverse_lazy('users:password_reset_complete')),
        name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='accounts/registration/password_reset_complete.html'),
        name='password_reset_complete'),
    path('users/', include(user_patterns)),
]
