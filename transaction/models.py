from django.db import models


class Transaction(models.Model):
    class Meta:
        managed = True

    guid = models.CharField(primary_key=True, max_length=32)
    num = models.CharField(max_length=2048)
    enter_date = models.CharField(max_length=14)  # TODO: format?
    post_date = models.CharField(max_length=14)  # TODO: format?
    description = models.CharField(max_length=2048)
    currency_guid = models.CharField(max_length=32)  # ForeignKey...
