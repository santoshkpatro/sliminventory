from django.contrib.auth import authenticate
from rest_framework import serializers, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from app.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar']


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            credentials = serializer.data
            user = authenticate(**credentials)
            if not user:
                return Response(data={'detail': 'Either email or password is invalid'}, status=status.HTTP_401_UNAUTHORIZED)
            access_token = str(AccessToken.for_user(user))
            refresh_token = str(RefreshToken.for_user(user))
            return Response(data={
                'access_token': access_token,
                'refresh_token': refresh_token
            }, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
