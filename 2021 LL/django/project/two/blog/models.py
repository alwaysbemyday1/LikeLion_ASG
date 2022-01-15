from django.db import models

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]