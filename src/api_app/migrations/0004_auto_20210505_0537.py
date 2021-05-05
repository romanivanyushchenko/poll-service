# Generated by Django 2.2.10 on 2021-05-05 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_auto_20210505_0339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answermodel',
            options={'verbose_name': 'Answer'},
        ),
        migrations.AlterModelOptions(
            name='pollmodel',
            options={'verbose_name': 'Poll'},
        ),
        migrations.AlterModelOptions(
            name='questionmodel',
            options={'verbose_name': 'Question'},
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='answers',
            field=models.ManyToManyField(blank=True, help_text='Только для вопросов с выбором варианта!', null=True, to='api_app.AnswerModel'),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='type',
            field=models.CharField(choices=[('text', 'Ответ текстом'), ('radio', 'Ответ с выбором одного варианта'), ('checkbox', 'Ответ с выбором нескольких вариантов')], max_length=10),
        ),
    ]
