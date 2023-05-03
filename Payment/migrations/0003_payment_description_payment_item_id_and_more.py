# Generated by Django 4.1 on 2023-05-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0002_remove_payment_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='item_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('due', 'Due'), ('paid', 'Paid'), ('failed', 'Failed'), ('terminated', 'Terminated')], default='due', max_length=10),
        ),
    ]
