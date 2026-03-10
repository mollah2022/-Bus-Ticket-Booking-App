from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import SiteUser
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny

# ---------------- User ViewSet ----------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = SiteUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

# ---------------- Custom Token Login ----------------
class UserObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        check_user = SiteUser.objects.filter(username=username)
        if not check_user.exists():
            return Response({'error':'User not found'}, status=status.HTTP_404_NOT_FOUND)

        response = super(UserObtainAuthToken,self).post(request,*args,**kwargs)
        token = response.data['token']
        user = SiteUser.objects.get(username=username)
        serializer = UserRegisterSerializer(user)
        return Response({'token':token,'user':serializer.data})
