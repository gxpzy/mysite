from django.db import models

# Create your models here.
from django.db import models


class Blog(models.Model):
    """
    一篇博客包括 文章的名字,作者,发布日期,路径
    """
    article_name = models.CharField(max_length=200)
    article_author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    file_path = models.CharField(max_length=200)

