# Generated by Django 2.1.5 on 2019-11-24 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0013_python'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.Python')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='firstapp.DetailofStudent')),
            ],
        ),
    ]
