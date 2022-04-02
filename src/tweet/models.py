from django.db import models

from core.models import BaseDateModel


class Tweet(BaseDateModel):
    """ツイート"""

    id = models.PositiveBigIntegerField("ツイートID", primary_key=True)
    tweeted_at = models.DateTimeField("ツイート日時")
    text = models.CharField("ツイート本文", max_length=300)
    account = models.ForeignKey(
        "account.Account",
        verbose_name="Twitterアカウント",
        related_name="tweets",
        on_delete=models.SET_NULL,
        null=True,
    )
    source = models.CharField("ツイートしたアプリ名", max_length=200, default="")
    retweet_count = models.IntegerField("リツイート数", default=0)
    quote_count = models.IntegerField("引用リツイート数", default=0)
    reply_count = models.IntegerField("リプライ数", default=0)
    like_count = models.IntegerField("いいね数", default=0)

    class Meta:
        verbose_name = verbose_name_plural = "ツイート"
        db_table = "tweet"
