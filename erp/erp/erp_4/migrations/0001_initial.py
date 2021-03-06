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
            name='jiagongzhongxin',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('xinghao', models.CharField(blank=True, max_length=6)),
                ('chejianbianhao', models.CharField(blank=True, max_length=6)),
                ('fuzeren', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp_1.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='jianyandan',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('chejianid', models.CharField(blank=True, max_length=2)),
                ('shijian', models.DateField(blank=True)),
                ('shuliang', models.CharField(blank=True, max_length=10)),
                ('jieguo', models.BooleanField(default=True)),
                ('jiagongzongxin_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp_4.jiagongzhongxin')),
                ('jyrid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp_1.Staff')),
                ('wuliaobianhao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp_1.Materials')),
            ],
        ),
        migrations.CreateModel(
            name='paigongdan',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('shijian', models.DateField(blank=True)),
                ('jiagongzhongxin_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp_4.jiagongzhongxin')),
                ('pgid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp_1.Staff')),
                ('wuliaobianhao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp_1.Materials')),
            ],
        ),
        migrations.CreateModel(
            name='zhizaodingdan',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('piliang', models.CharField(blank=True, max_length=6)),
                ('chejianbianhao', models.CharField(blank=True, max_length=6)),
                ('shijian', models.DateField(blank=True)),
                ('huohao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='erp_1.Materials')),
            ],
        ),
    ]
