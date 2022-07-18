# Generated by Django 3.2.14 on 2022-07-16 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128, unique=True)),
                ('icon', models.FileField(upload_to='category/')),
                ('post_count', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, verbose_name='Nomi')),
                ('slug', models.CharField(max_length=128, unique=True)),
                ('content', models.TextField()),
                ('sub_content', models.CharField(max_length=128)),
                ('image', models.ImageField(null=True, upload_to='post/')),
                ('published_date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('created', 'created'), ('moderation', 'moderation'), ('published', 'published')], max_length=15)),
                ('read_min', models.IntegerField(default=0)),
                ('views_count', models.PositiveIntegerField(default=0)),
                ('is_popular', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='author.author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='post.category')),
                ('tags', models.ManyToManyField(related_name='posts', to='post.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]