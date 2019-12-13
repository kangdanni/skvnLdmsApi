"""
__version__ = '0.0.0'
__author__ = 'kkangdanni@sk.com'
__date__ = '2019-12-11'
__copyright__ = 'Copyright 2019, SK Telink CO,LTD All Rights Reserved.'

"""


from django.db import models


# Create your models here.
"""
로그인
"""
class TVtnUser(models.Model):
    uid = models.CharField(max_length=12)
    password = models.CharField(max_length=100)
    is_admin = models.CharField(max_length=10, blank=True, null=True)
    created = models.CharField(max_length=14, blank=True, null=True)
    last_login = models.CharField(max_length=14, blank=True, null=True)
    use_yn = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 't_vtn_user'
        unique_together = (('uid', 'created'),)

"""
Shopinfo
"""
class TVtnUsedPhoneShopcommon(models.Model):
    store_cd = models.CharField(max_length=5, primary_key=True)
    store_nm = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_vtn_used_phone_shopcommon'

"""
columnlist
"""
class TVtnUsedPhoneCommoncode(models.Model):
    manage_id = models.CharField(max_length=5, primary_key=True)
	manage_nm = models.CharField(max_length=50) 
	manage_cd = models.CharField(max_length=50) 
	use_yn = models.CharField(max_length=2) 
	inspt_yn = models.CharField(max_length=2)
