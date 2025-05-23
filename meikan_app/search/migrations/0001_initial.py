# Generated by Django 5.1.7 on 2025-03-23 11:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company", models.CharField(max_length=100, verbose_name="所属")),
                ("name", models.CharField(max_length=20, verbose_name="名前")),
                ("birthday", models.CharField(max_length=4, verbose_name="誕生日")),
                ("hometown", models.CharField(max_length=20, verbose_name="出身")),
                ("history", models.CharField(max_length=100, verbose_name="経歴")),
                (
                    "awards",
                    models.CharField(max_length=100, null=True, verbose_name="受賞歴"),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="寸評"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="作成日時"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新日時"),
                ),
            ],
        ),
    ]
