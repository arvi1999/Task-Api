# Generated by Django 3.0.6 on 2020-05-08 15:58

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('todoapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddConstraint(
            model_name='item',
            constraint=models.CheckConstraint(check=models.Q(created_on__lte=django.db.models.expressions.F('due_date')), name='correct_datetime'),
        ),
    ]
