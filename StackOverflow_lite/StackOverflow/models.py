from django.db import models
from django.contrib.auth.models import User

# answers body
# questions body, topic
# users already taken care of


class Questions(models.Model):
    body = models.CharField(max_length=150)
    topic = models.CharField(max_length= 70)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('body', 'topic', )

    def __str__(self):
        return {'topic': self.topic ,'body': self.body}

class Answers(models.Model):
    body = models.CharField(max_length= 150)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('body', )
    
    def __str__(self):
        return {'question': self.question, 'answer': self.body}
        

