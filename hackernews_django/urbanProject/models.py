from django.db import models

# Create your models here.
class hackerNewsAPI(models.Model):
    serial_id = models.AutoField(primary_key=True)
    article_id = models.IntegerField(null=True, unique=True)
    username = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=300, null=True)
    url = models.CharField(max_length=300, null=True)
    score = models.IntegerField(null=True)
    sentiment = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.title
