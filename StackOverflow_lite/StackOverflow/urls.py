from django.urls import path
from .views import QuestionsListView, AnswersListView



urlpatterns = [
    path('questions', QuestionsListView.as_view(), name='questions'),
    path('answers', AnswerListView.as_view(), name='answers')
]