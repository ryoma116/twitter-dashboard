from django.db import models
from django.utils import timezone


class BaseDateModel(models.Model):
    """モデルに作成日時/更新日時のタイムスタンプを追加するベースモデル

    * 全てのモデルはこれを継承する
    """

    created_at = models.DateTimeField("作成日時", default=timezone.now)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        abstract = True
