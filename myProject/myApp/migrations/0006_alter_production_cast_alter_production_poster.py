# Generated by Django 5.0.4 on 2024-05-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_delete_verproduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='cast',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='production',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
