# Generated by Django 4.0.4 on 2022-05-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothname', models.CharField(max_length=100)),
                ('clothfile', models.ImageField(default='', upload_to='media/image')),
                ('clothgender', models.CharField(max_length=100)),
                ('clothtype', models.CharField(max_length=100)),
                ('clothcolour', models.CharField(max_length=100)),
                ('clothpattern', models.CharField(max_length=100)),
                ('clothsizes', models.CharField(max_length=100)),
                ('clothprice', models.DecimalField(blank=True, decimal_places=0, default=None, max_digits=20, null=True)),
                ('clothdesigner', models.CharField(default=None, max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(default=None, max_length=100)),
                ('cart', models.CharField(default='0', max_length=100)),
                ('wishlist', models.CharField(default='0', max_length=100)),
                ('order', models.CharField(default='0', max_length=100)),
            ],
            options={
                'db_table': 'cuitems_table',
            },
        ),
        migrations.CreateModel(
            name='Cusignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('dateofbirth', models.CharField(max_length=100)),
                ('phoneno', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('username', models.CharField(default=None, max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cusignup_table',
            },
        ),
    ]
