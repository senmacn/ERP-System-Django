# Generated by Django 2.0.7 on 2019-11-10 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacture_apply',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('product_id', models.CharField(max_length=6)),
                ('name', models.CharField(blank=True, max_length=10)),
                ('applicant_id', models.CharField(blank=True, max_length=6)),
                ('applicant_name', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mps_list',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=10)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product_list',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('product_id', models.CharField(max_length=6)),
                ('name', models.CharField(blank=True, max_length=10)),
                ('forMps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_3.Mps_list')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_apply',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('product_id', models.CharField(max_length=6)),
                ('name', models.CharField(blank=True, max_length=10)),
                ('standard', models.CharField(blank=True, max_length=10)),
                ('apply_department', models.CharField(default='MRP', max_length=4)),
                ('for_mps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_3.Mps_list')),
            ],
        ),
        migrations.CreateModel(
            name='TimeForManufacture_list',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('in_time', models.DateField()),
                ('in_amount', models.IntegerField()),
                ('out_time', models.DateField()),
                ('out_amount', models.IntegerField()),
                ('forProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_3.Manufacture_apply')),
            ],
        ),
        migrations.CreateModel(
            name='TimeForProduct_list',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('time', models.DateField()),
                ('amount', models.IntegerField()),
                ('forProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_3.Product_list')),
            ],
        ),
        migrations.CreateModel(
            name='TimeForPurchase_list',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('time', models.DateField()),
                ('amount', models.IntegerField()),
                ('forProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_3.Purchase_apply')),
            ],
        ),
        migrations.AddField(
            model_name='manufacture_apply',
            name='for_mps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp_3.Mps_list'),
        ),
    ]
