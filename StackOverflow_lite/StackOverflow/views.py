from django.shortcuts import render
from rest_framework import generics
from .models import Questions, Answers
from  .serializers import QuestionsSerializer, AnswersSerializer

# Create your views here.
# Get questions api/v1/questions
# Get single question api/v1/questions/<int:questionId>
# Get answers 

class QuestionsListView(generics.ListCreateAPIView):
    queryset =  Questions.objects.all()
    serializer_class = QuestionsSerializer

class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class AnswersListView(generics.CreateAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

    