# Generated by Django 4.1.1 on 2023-02-03 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0005_remove_user_parking_number_parking_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="parking",
            name="parking_name",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="parking",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                db_column="owner",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]