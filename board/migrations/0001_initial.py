# Generated by Django 3.2.6 on 2021-08-12 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcuser', '0002_auto_20210811_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='SUBJECT')),
                ('contents', models.TextField(verbose_name='CONTENTS')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='REG Time')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.fcuser', verbose_name='AUTHOR')),
            ],
            options={
                'verbose_name': 'NamoWebiz 게시글',
                'verbose_name_plural': 'NamoWebiz 게시글',
                'db_table': 'fastcampus_board',
            },
        ),
    ]
