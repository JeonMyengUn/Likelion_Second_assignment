from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('Date published')
    content = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]
