# Generated by Django 5.0 on 2023-12-09 21:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_for_exams', '0002_test_testanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answeroption',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_options', to='tests_for_exams.question'),
        ),
    ]
