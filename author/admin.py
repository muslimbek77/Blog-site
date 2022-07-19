import django
from django.contrib import admin

from author.models import Author, AuthorJob

# Register your models here.
admin.site.register(AuthorJob)
admin.site.register(Author)
