from django.db import models

# Create your models here.

class PopularPostedManager(models.Manager):
    def get_queryset(self):
        return super(PopularPostedManager, self).get_queryset().filter(is_popular=True)

class TopAuthorsManager(models.Manager):
    def get_queryset(self):
        return super(TopAuthorsManager, self).get_queryset().filter(is_top=True)


