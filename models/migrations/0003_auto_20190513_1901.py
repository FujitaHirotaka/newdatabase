# Generated by Django 2.2 on 2019-05-13 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20190513_1853'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together={('analysisterm0', 'analysisterm1', 'analysisterm2', 'analysisterm3', 'analysisterm4', 'analysisterm5', 'analysisterm6', 'analysisterm7', 'analysisterm8', 'analysisterm9')},
        ),
    ]
