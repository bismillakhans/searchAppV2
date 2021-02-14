# Generated by Django 2.2 on 2021-02-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0003_newcollegebasicinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewCollegeCollegeCities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.CharField(blank=True, max_length=200, null=True)),
                ('state_id', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.CharField(blank=True, max_length=200, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'new_college_college_cities',
                'managed': False,
            },
        ),
    ]
