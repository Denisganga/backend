from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView,ConversationAPIView,LoginAPIView
urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('conversation-page/', ConversationAPIView.as_view(), name='conversation-page'),
  path('login/', LoginAPIView.as_view(), name='login'),
  
]