# Generated by Django 3.0 on 2019-12-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examinees', '0003_examineeexam_answer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examineeexam',
            name='answer_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='examineeexam',
            name='exam_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='examineeexam',
            name='question_id',
            field=models.IntegerField(null=True),
        ),
    ]
