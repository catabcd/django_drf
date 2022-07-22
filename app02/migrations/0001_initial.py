# Generated by Django 2.1.5 on 2022-07-21 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('vum', models.IntegerField(verbose_name='浏览量')),
                ('content', models.TextField(verbose_name='内容')),
            ],
        ),
    ]