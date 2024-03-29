# Generated by Django 2.2 on 2019-05-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='納入先名称')),
            ],
            options={
                'verbose_name_plural': '納入先',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, null=True, verbose_name='項目名')),
            ],
            options={
                'verbose_name_plural': '水質分析項目',
            },
        ),
    ]
