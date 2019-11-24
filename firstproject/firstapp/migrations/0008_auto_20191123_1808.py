# Generated by Django 2.1.5 on 2019-11-24 00:08

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('firstapp', '0007_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='StuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]