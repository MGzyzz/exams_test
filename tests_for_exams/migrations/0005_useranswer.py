# Generated by Django 5.0 on 2023-12-10 09:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_for_exams', '0004_remove_test_completed_remove_test_score_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests_for_exams.question')),
                ('selected_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests_for_exams.answeroption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
