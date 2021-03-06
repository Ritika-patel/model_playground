# Generated by Django 3.1.7 on 2021-03-20 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_pizza_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desgination', models.CharField(max_length=256)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
                ('society_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.society')),
            ],
        ),
    ]
