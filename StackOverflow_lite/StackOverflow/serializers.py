from rest_framework import serializers
from .models import Questions, Answers


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    answers = AnswersSerializer(many=True, required=False)

    class Meta:
        model = Questions
        fields = '__all__'



