from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Post
from .serializers import PostSerializer, LikeSerializer
from .services import likes_by_date


class PostView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    def get(self, request, user_id):
        serializer = PostSerializer(Post.objects.get(id=user_id))
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostLikeView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostAnaliticsView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        date_from = request.query_params.get('date_from', None)
        date_to = request.query_params.get('date_to', None)

        data = likes_by_date(date_from, date_to)
        if data:
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
