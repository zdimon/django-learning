# Generated by Django 2.2.4 on 2019-08-17 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.News'),
            preserve_default=False,
        ),
    ]
