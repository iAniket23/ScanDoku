# Generated by Django 3.2.8 on 2022-06-19 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sudokuScanner', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sudokuScanner.user'),
            preserve_default=False,
        ),
    ]
