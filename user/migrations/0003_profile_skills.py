# Generated by Django 4.1.7 on 2023-04-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_user_alter_message_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.CharField(default='no skillset', max_length=100),
        ),
    ]