# Generated by Django 2.1.7 on 2019-03-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choicedata',
            name='is_it_right',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=10),
        ),
    ]
