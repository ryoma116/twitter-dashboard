from django.db import models

from core.models import BaseDateModel


class Account(BaseDateModel):
    """Twitterアカウント"""

    id = models.PositiveBigIntegerField("アカウントID", primary_key=True)
    username = models.CharField("ユーザー名", max_length=30)
    name = models.CharField("名前", max_length=100)
    started_at = models.DateTimeField("Twitter開始日時")
    description = models.CharField("プロフィール本文", max_length=320, null=True)
    url = models.URLField("ウェブサイト", max_length=200, null=True)
    profile_image_url = models.URLField("プロフィール画像URL", max_length=200, null=True)
    location = models.CharField("場所", max_length=60, null=True)
    followers_count = models.IntegerField("フォロワー数", default=0)
    following_count = models.IntegerField("フォロー数", default=0)
    tweet_count = models.IntegerField("ツイート数", default=0)
    listed_count = models.IntegerField("リスト登録数", default=0)

    class Meta:
        verbose_name = verbose_name_plural = "Twitterアカウント"
        db_table = "account"

    def __str__(self):
        return f"{self.name}"
