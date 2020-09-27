# Generated by Django 3.1.1 on 2020-09-26 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_work_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=160)),
                ('country', models.CharField(default='none', max_length=160)),
                ('position', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]