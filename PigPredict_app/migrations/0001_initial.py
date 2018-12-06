# Generated by Django 2.1.2 on 2018-11-28 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LAB_Clothe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('L', models.FloatField()),
                ('A', models.FloatField()),
                ('B', models.FloatField()),
                ('CLOTHE', models.CharField(choices=[('FVF2666', 'FVF2666'), ('FVF2429', 'FVF2429'), ('FVF2184', 'FVF2184')], default='FVF2184', max_length=256)),
            ],
        ),
    ]
