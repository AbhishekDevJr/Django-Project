# Generated by Django 5.1.1 on 2024-10-04 05:56

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expenseId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('category', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('expenseDate', models.DateTimeField(default=datetime.datetime.now)),
                ('creationDate', models.DateTimeField(default=datetime.datetime.now)),
                ('currency', models.CharField(default='INR', max_length=50)),
                ('status', models.CharField(default='PENDING', max_length=50)),
            ],
        ),
    ]
