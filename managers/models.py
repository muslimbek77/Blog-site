from django.db import models

# Create your models here.

class ThisMonthManager(models.Manager):
    def get_queryset(self):
        return super(ThisMonthManager, self).get_queryset().filter(is_popular=True)

class PopularPostedManager(models.Manager):
    def get_queryset(self):
        return super(ThisMonthManager, self).get_queryset().filter(is_popular=True)

class TopAuthorsManager(models.Manager):
    def get_queryset(self):
        return super(TopAuthorsManager, self).get_queryset().filter(is_top=True)


