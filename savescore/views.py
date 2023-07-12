from django.shortcuts import render,get_object_or_404
from .models import Score
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,CreateAPIView

from rest_framework.views import APIView
from .serializers import ScoreSerializer


class createScore(CreateAPIView):#post임
    #queryset=Score.objects.all() #create이기 때문에 쿼리셋 쓸 필요 없음
        serializer_class=ScoreSerializer

class GetScore(RetrieveAPIView):#RetriveAPIView는 pk값이 필요함 //GET임
    queryset=Score.objects.all()
    serializer_class=ScoreSerializer
    
    