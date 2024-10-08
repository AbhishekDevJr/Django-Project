# Generated by Django 5.1.1 on 2024-10-02 09:27

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('createdAt', models.DateField(default=datetime.date.today)),
                ('blogId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
