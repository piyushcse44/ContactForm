# Generated by Django 4.1.7 on 2023-03-28 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='Adress',
            field=models.CharField(default='xyz nagar', max_length=200),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='Email',
            field=models.EmailField(default='xyz@gmail.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='Message_Subject',
            field=models.CharField(max_length=1000, verbose_name='Message Subject'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='Name',
            field=models.CharField(default='Enter Your Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='Phone',
            field=models.CharField(default='0123456789', max_length=10),
        ),
    ]
