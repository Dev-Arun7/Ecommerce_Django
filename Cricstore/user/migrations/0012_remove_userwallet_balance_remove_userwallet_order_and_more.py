# Generated by Django 4.2.5 on 2023-10-28 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_replymessage_admin_delete_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwallet',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='userwallet',
            name='order',
        ),
        migrations.RemoveField(
            model_name='userwallet',
            name='status',
        ),
        migrations.AlterField(
            model_name='replymessage',
            name='admin',
            field=models.ForeignKey(default=(27,), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]