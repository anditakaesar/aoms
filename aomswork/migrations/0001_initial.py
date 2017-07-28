# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 03:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('color_name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('-color_name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-create_date',),
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aomswork.Order')),
            ],
            options={
                'ordering': ('-create_date',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(max_length=200)),
                ('product_desc', models.CharField(max_length=2000)),
            ],
            options={
                'ordering': ('-create_date',),
            },
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aomswork.Color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aomswork.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.IntegerField()),
                ('product_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aomswork.ProductColor')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(through='aomswork.ProductColor', to='aomswork.Color'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aomswork.ProductColor'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderdetails',
            field=models.ManyToManyField(related_name='_order_orderdetails_+', to='aomswork.OrderDetail'),
        ),
    ]
