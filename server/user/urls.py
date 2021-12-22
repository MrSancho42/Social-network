from django.urls import path, include
from .views import *


urlpatterns = [
    path('activity/', UserActivityView.as_view(), name='user_activity'),
    path('register/', CreateUserView.as_view(), name='create_user'),
    path('logout/', BlacklistTokenView.as_view(), name='logout'),
]
