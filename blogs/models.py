from django.db import models


class Blog(models.Model):
    blog_name = models.CharField(max_length=100)
    blog_content = models.CharField(max_length=2000)

    def __str__(self):
        return self.blog_name