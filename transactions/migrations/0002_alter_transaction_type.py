# Generated by Django 5.1.3 on 2024-11-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('income', 'Income'), ('outcome', 'Outcome')], max_length=10),
        ),
    ]
