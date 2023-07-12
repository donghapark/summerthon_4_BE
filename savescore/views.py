from django.shortcuts import render,get_object_or_404
from .models import Score
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from rest_framework.views import APIView
from .serializers import ScoreSerializer


class GetScore(RetrieveAPIView):
    queryset=Score.objects.all()
    serializer_class=ScoreSerializer
# class GetScore(APIView):
#     def get(self, request, pk):
#         score = get_object_or_404(Score, testId=pk)
#         score_serializer = ScoreSerializer(score)
#         return Response(score_serializer.data, status=200)