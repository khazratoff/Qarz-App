# Generated by Django 4.0.6 on 2022-07-19 10:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QarzModel',
            fields=[
                ('person', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='images/def.png', null=True, upload_to='')),
                ('amount', models.IntegerField(null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]