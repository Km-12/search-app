from django.db import models
import uuid


class Member(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID"
    )
    company = models.CharField(max_length=100, verbose_name="所属")
    name = models.CharField(max_length=20, verbose_name="名前")
    birthday = models.CharField(max_length=4, verbose_name="誕生日")
    hometown = models.CharField(max_length=20, verbose_name="出身")
    history = models.CharField(max_length=100, verbose_name="経歴")
    awards = models.CharField(max_length=100, null=True, verbose_name="受賞歴")
    comment = models.TextField(blank=True, null=True, verbose_name="寸評")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return self.name
