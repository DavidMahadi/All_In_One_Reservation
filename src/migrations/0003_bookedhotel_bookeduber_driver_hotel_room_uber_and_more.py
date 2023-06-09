# Generated by Django 4.1.7 on 2023-03-20 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import src.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('src', '0002_rename_bookairplaneticket_airplaneticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BookedUber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('working_hours', models.IntegerField()),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('price_choices', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Uber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UberCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plateno', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('workedhours', models.IntegerField()),
                ('price_hour', models.FloatField(verbose_name=7000)),
                ('payment', models.FloatField(default=src.models.UberCars.price)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.driver')),
                ('uber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.uber')),
            ],
        ),
        migrations.DeleteModel(
            name='AirPlaneTicket',
        ),
        migrations.DeleteModel(
            name='HotelReservation',
        ),
        migrations.DeleteModel(
            name='Tour',
        ),
        migrations.DeleteModel(
            name='UberReservation',
        ),
        migrations.AddField(
            model_name='bookeduber',
            name='Uber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.uber'),
        ),
        migrations.AddField(
            model_name='bookeduber',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookedhotel',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='src.hotel'),
        ),
        migrations.AddField(
            model_name='bookedhotel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
