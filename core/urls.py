from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', views.LoginSignupView.as_view(), name='auth'),
    path('api/signup/', views.SignupView.as_view(), name='signup'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('api/profile/', views.ProfileView.as_view(), name='update_profile'),
    path('start-test/', views.StartTestView.as_view(), name='start_test'),
    path('test/<uuid:session_id>/step/<int:step>/', views.TestStepView.as_view(), name='test_step'),
    path('test/<uuid:session_id>/result/', views.TestResultView.as_view(), name='test_result'),
    path('save-response/', views.SaveResponseView.as_view(), name='save_response'),
]
