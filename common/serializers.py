from rest_framework import serializers

class RequestLoginSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=12)
    password = serializers.CharField(max_length=100)

class ResponseLoginSerializer(serializers.Serializer):
    statusCode = serializers.IntegerField(read_only=True, help_text="상태코드")
    success = serializers.BooleanField(read_only=True, help_text="성공여부")
    message = serializers.CharField(read_only=True, help_text="결과 메시지")
    user = serializers.CharField(read_only=True, help_text="사용자ID")
    token = serializers.CharField(read_only=True, help_text="사용자token")

class RequestShopInfoSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=12)
    token = serializers.CharField(max_length=150)

class ResponseLoginSerializer(serializers.Serializer):
    statusCode = serializers.IntegerField(read_only=True, help_text="상태코드")
    success = serializers.BooleanField(read_only=True, help_text="성공여부")
    message = serializers.CharField(read_only=True, help_text="결과 메시지")
    rt_data = serializers.CharField(read_only=True, help_text="유통망 정보")
