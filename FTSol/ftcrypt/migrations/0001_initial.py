# Generated by Django 3.2 on 2021-05-04 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FTCRYPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postfile', models.FileField(upload_to='')),
                ('insertedon', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Post File',
                'verbose_name_plural': 'Post Files',
                'db_table': 'mst_postfile',
                'ordering': ['-insertedon'],
            },
        ),
    ]
