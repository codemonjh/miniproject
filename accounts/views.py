import jwt
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status,permissions
from rest_framework.response import Response


class UserView(APIView):
    # 일반회원가입
    def post(self, request):
        serializer = UserCreateSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        serializer = UserCreateSerialzier(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request):
        if not request.user.is_authenticated:
            return Response({"detail": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
        user = request.user
        user.delete()
        return Response({"detail": "회원 탈퇴가 완료되었습니다."}, status=status.HTTP_204_NO_CONTENT)
    
class GoogleLoginview(APIView):
    pass