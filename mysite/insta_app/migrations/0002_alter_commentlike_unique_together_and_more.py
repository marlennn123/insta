# Generated by Django 5.1.4 on 2024-12-21 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='commentlike',
            unique_together={('user', 'comment')},
        ),
        migrations.AlterUniqueTogether(
            name='postlike',
            unique_together={('user', 'post')},
        ),
    ]
