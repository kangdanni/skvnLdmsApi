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
Common Code
"""
class TCommCdDtl(models.Model):
    comm_cd_grp = models.CharField(max_length=10)
    comm_cd = models.CharField(max_length=10)
    comm_nm = models.CharField(max_length=200, blank=True, null=True)
    ref_cd1 = models.CharField(max_length=500, blank=True, null=True)
    ref_cd2 = models.CharField(max_length=500, blank=True, null=True)
    ref_cd3 = models.CharField(max_length=500, blank=True, null=True)
    ref_cd4 = models.CharField(max_length=500, blank=True, null=True)
    deflt_yn = models.CharField(max_length=1, default='Y')
    rmrk = models.CharField(max_length=1000, blank=True, null=True)
    sort_no = models.IntegerField(blank=True, null=True)
    use_yn = models.CharField(max_length=1, default='Y')
    sys_use_yn = models.CharField(max_length=1, default='Y')
    inpt_menu_id = models.CharField(max_length=10, blank=True, null=True)
    regr_id = models.CharField(max_length=50, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    chgr_id = models.CharField(max_length=50, blank=True, null=True)
    chg_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_comm_cd_dtl'
        unique_together = (('comm_cd_grp', 'comm_cd'),)


