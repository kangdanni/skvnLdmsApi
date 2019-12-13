from django.shortcuts import render

# Create your views here.
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *

import bcrypt
import jwt

class LoginView(APIView):
    """
    로그인
    """
    #required_alternate_scopes = settings.DEFAULT_PERMISSION_SCOPES

    def post(self, request, format=None):
        request_serializer = RequestLoginSerializer(data=request.data)

        if not request_serializer.is_valid():
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        rt_data = {
            'statusCode': status.HTTP_401_UNAUTHORIZED,
            'success': False,
            'message': 'Password not match',
            'user' : request.data['uid'],
            'token' : ''
        }

        try:
            user_info = TVtnUser.objects.values('password', 'uid').get(uid=request.data['uid'], use_yn = 'Y')
        except TVtnUser.DoesNotExist:
            rt_data['statusCode'] = status.HTTP_404_NOT_FOUND
            rt_data['message'] = 'User info not exists.'

        if rt_data['statusCode'] == status.HTTP_401_UNAUTHORIZED:
            if bcrypt.hashpw(request.data['password'].encode('utf-8'), user_info['password'].encode("utf-8")) == user_info['password'].encode('utf-8'):
                ##인증 완료시 토큰 발급
                rt_data['statusCode'] = status.HTTP_200_OK
                rt_data['success'] = True
                rt_data['message'] = 'Login succeded.'
                rt_data['token'] = jwt.encode( {'uid':user_info['uid']}, 'sktelink', algorithm='HS256').decode('unicode_escape')

        response_serializer = ResponseLoginSerializer(rt_data)
        return Response(response_serializer.data, status=rt_data['statusCode'])

class ShopInfoView(APIView) :
    """
    shopinfo 가져오기
    """
    def post(self, request, format=None):
        request_serializer = RequestShopInfoSerializer(data=request.data)

        if not request_serializer.is_valid():
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        rt_data = {
            'statusCode': status.HTTP_401_UNAUTHORIZED,
            'success': False,
            'message': 'Unauthorized',
            'rt_data' : ''
        }

        dec = jwt.decode(request.data['token'], 'sktelink', algorithm='HS246')
        uid = request.data['uid']
        if uid == dec['uid'] : 
            shop_info = TVtnUsedPhoneShopcommon.objects.values('store_cd','store_nm').all()

            rt_data['statusCode'] = status.HTTP_200_OK
            rt_data['success'] = True
            rt_data['message'] = 'Request Succeded.'
            rt_data['rt_data'] = list(shop_info)
            

        response_serializer = ResponseLoginSerializer(rt_data)
        return Response(response_serializer.data, status=rt_data['statusCode'])
