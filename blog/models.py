from django.db import models

# Create your models here.
class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=50)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title+ ' by ' + self.author