from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "created_at", "updated_at"]
