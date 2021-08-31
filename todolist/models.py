from django.db import models

# Create your models here.
class TodoList(models.Model):
    date = models.DateField()
    content = models.CharField(max_length=200)
    plusmemo = models.TextField(null=True,default='')

    def __str__(self):
        return [self.content, self.plusmemo]