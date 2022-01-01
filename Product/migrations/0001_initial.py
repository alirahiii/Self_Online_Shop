# Generated by Django 4.0 on 2021-12-26 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Salesman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_title', models.CharField(max_length=150)),
                ('sub_cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Product.category')),
            ],
        ),
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(blank=True, max_length=50, null=True)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(null=True)),
                ('brand', models.CharField(max_length=50, null=True)),
                ('price', models.BigIntegerField(null=True)),
                ('amount', models.IntegerField(null=True)),
                ('actvate', models.BooleanField()),
                ('img1', models.ImageField(upload_to='')),
                ('img2', models.ImageField(upload_to='')),
                ('img3', models.ImageField(upload_to='')),
                ('img4', models.ImageField(upload_to='')),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='Product.category')),
                ('sellsman_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='Salesman.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=400)),
                ('pro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.property')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
        ),
    ]
