# Generated by Django 4.1.7 on 2023-03-21 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0006_changetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='thumbnail',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]