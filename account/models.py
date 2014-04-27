from django.db import models

class Account(models.Model):
    class Meta:
        managed = False

    guid = models.CharField(primary_key=True, max_length=32)

    name = models.CharField(max_length=2048)
    code = models.CharField(max_length=2048, null=True)
    description = models.CharField(max_length=2048, null=True)

    parent_guid = models.ForeignKey('self', null=True)

    account_type = models.CharField(max_length=2048)
    commodity_guid = models.CharField(max_length=32, null=True)
    commodity_scu = models.IntegerField()
    non_std_scu = models.IntegerField()

    hidden = models.IntegerField(null=True)
    placeholder = models.IntegerField(null=True)

