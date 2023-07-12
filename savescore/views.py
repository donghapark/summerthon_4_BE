from django.shortcuts import render
from .models import Score
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ScoreSerializer


class GetScore(APIView):
    def get(self,request):
        info=Score.objects.filter(testId=request.data["pk"]) 
        info_serializer=ScoreSerializer(info)
        return Response(info_serializer.data, status=200)