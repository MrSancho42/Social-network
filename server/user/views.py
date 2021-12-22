from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import RegisterUserSerializer, UserSerializer


class CreateUserView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            if user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserActivityView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user_id = request.query_params.get('user_id', None)

        if user_id:
            serializer = UserSerializer(User.objects.get(id=user_id))
        else:
            serializer = UserSerializer(request.user)

        last_login = serializer.data['last_login']
        last_activity = serializer.data['last_activity']
        
        data = {'last_login': last_login, 'last_activity': last_activity}
        return Response(data=data, status=status.HTTP_200_OK)


class BlacklistTokenView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
