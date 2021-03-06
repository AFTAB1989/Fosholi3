# Generated by Django 2.2.7 on 2019-11-23 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UpChairman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UNO',
            fields=[
                ('uno_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('uno_name', models.CharField(max_length=50)),
                ('uno_phone', models.CharField(max_length=15)),
                ('uno_address', models.CharField(max_length=150)),
                ('uno_email', models.EmailField(max_length=50, unique=True)),
                ('uno_password', models.CharField(max_length=50)),
                ('uno_nid_no', models.CharField(max_length=25, unique=True)),
                ('upc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UpChairman.UpChairman')),
            ],
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('union_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('union_name', models.CharField(max_length=25)),
                ('num_of_farmer', models.IntegerField()),
                ('farmable_land', models.IntegerField()),
                ('upz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UpChairman.Upazilla')),
            ],
        ),
    ]
