# Generated by Django 2.2.3 on 2019-07-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190721_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='stat',
            field=models.CharField(choices=[('Ожидает выполнеиния', 'Ожидает выполнеиния'), ('Выполняется', 'Выполняется'), ('Выполнено', 'Выполнено')], default='Ожидает выполнеиния', max_length=25),
        ),
    ]
