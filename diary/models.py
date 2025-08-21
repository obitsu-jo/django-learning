from django.db import models
import uuid
from django.conf import settings

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='ID')
    title = models.CharField(max_length=100, verbose_name='タイトル')
    body = models.TextField(max_length=200, verbose_name='本文')
    page_date = models.DateField(verbose_name='日付')
    created_at = models.DateField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateField(auto_now=True, verbose_name='更新日時')

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Djangoの標準ユーザーモデルと関連付け
        on_delete=models.CASCADE, # ユーザーが削除されたら、その日記も削除する
        verbose_name='ユーザー'
    )
    
    def __str__(self):
        return self.title
