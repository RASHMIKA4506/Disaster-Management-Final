# Generated by Django 4.1.7 on 2024-04-22 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0006_states'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='disaster.states'),
        ),
    ]
