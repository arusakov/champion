# Generated by Django 2.1.7 on 2019-02-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]