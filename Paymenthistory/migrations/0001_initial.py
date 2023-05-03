# Generated by Django 4.1 on 2023-05-03 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Payment', '0003_payment_description_payment_item_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paymenthistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('failed', 'Failed')], default='due', max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Payment.payment')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Payment_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]