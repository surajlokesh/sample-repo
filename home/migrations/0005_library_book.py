# Generated by Django 2.2.2 on 2019-07-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190702_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='book',
            field=models.CharField(blank=True, max_length=30, verbose_name='book name'),
        ),
    ]