# Generated by Django 3.1.4 on 2023-10-17 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etxealokairua', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alokairua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alokairu_data_hasiera', models.DateField(null=True)),
                ('alokairu_data_amaiera', models.DateField(null=True)),
                ('etxea_izena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etxealokairua.etxea')),
                ('pertsona_izena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etxealokairua.pertsona')),
            ],
        ),
    ]
