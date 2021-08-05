from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Plot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)

    

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    
    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    options = models.CharField(max_length=30)

    
    def __str__(self):
        return self.options

    @property
    def votes(self):
        return self.answer_set.count()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)



    
class Post(models.Model):
    title = models.CharField(max_length=40)
    desc = models.CharField(max_length=40)
    img = models.ImageField(upload_to="pic", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def comments(self):
        return self.comment_set.all()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100)
    





    


