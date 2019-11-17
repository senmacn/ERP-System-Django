# Generated by Django 2.0.7 on 2019-11-10 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erp_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=10)),
                ('grade', models.FloatField(default=0)),
                ('tel', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order2',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('deliver2', models.BooleanField(default=False)),
                ('payment', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp_2.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('cost', models.IntegerField(default=0)),
                ('basic_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('zhiwu', models.CharField(max_length=10)),
                ('yeji', models.FloatField(default=0)),
                ('tel', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='order2',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp_2.Product'),
        ),
        migrations.AddField(
            model_name='order2',
            name='salesman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salesman', to='erp_1.Staff', verbose_name='销售员'),
        ),
    ]