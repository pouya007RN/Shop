# Generated by Django 2.2.3 on 2019-09-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('نام', models.CharField(max_length=50)),
                ('نام_خانوادگی', models.CharField(max_length=50, verbose_name='نام خانوادگی')),
                ('ایمیل', models.EmailField(max_length=254)),
                ('شماره_تماس', models.CharField(default='09', max_length=15, verbose_name='شماره تماس')),
                ('موضوع', models.CharField(max_length=50)),
                ('پیام_شما', models.TextField()),
            ],
        ),
    ]
