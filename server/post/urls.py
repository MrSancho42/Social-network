from django.urls import path, include
from .views import *


urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('<int:user_id>/', PostDetailView.as_view(), name='post_detail'),
    path('like/', PostLikeView.as_view(), name='like'),
    path('analitics/', PostAnaliticsView.as_view(), name='analitics'),
]
