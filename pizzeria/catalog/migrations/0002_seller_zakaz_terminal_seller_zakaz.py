# Generated by Django 4.1.7 on 2023-03-01 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter a first_name of seller', max_length=100)),
                ('last_name', models.CharField(help_text='Enter a last_name of seller', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_zakaz', models.CharField(help_text='Enter number of zakaz', max_length=10)),
                ('pizza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_open', models.DateField(blank=True, null=True)),
                ('time_close', models.DateField(blank=True, null=True)),
                ('total_pay', models.FloatField()),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.seller')),
                ('zakaz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.zakaz')),
            ],
        ),
        migrations.AddField(
            model_name='seller',
            name='zakaz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.zakaz'),
        ),
    ]
