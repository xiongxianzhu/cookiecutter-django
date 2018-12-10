from datetime import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


# Create your models here.
class Menu(models.Model):
    """ 菜单 """
    MENU_CHOICES = (
        ('MODEL', '模型'),
        ('CATEGORY', '分类'),
    )

    name = models.CharField(max_length=30, unique=True, verbose_name="菜单名")
    parent = models.ForeignKey("self", null=True, blank=True,
                on_delete=models.SET_NULL, verbose_name="父菜单")
    menu_type = models.CharField(max_length=20, default='MODEL',
                choices=MENU_CHOICES, verbose_name="类型")
    icon = models.CharField(max_length=50, null=True, blank=True,
                verbose_name="图标")
    code = models.CharField(max_length=50, null=True, blank=True,
                verbose_name="编码")
    url = models.CharField(max_length=128, unique=True, null=True,
                blank=True, verbose_name="链接")
    desc = models.CharField(max_length=128, unique=True, null=True,
                blank=True, verbose_name="描述")
    sort = models.IntegerField(default=0, verbose_name="排序编号")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    @classmethod
    def get_menu_by_request_url(cls, url):
        return dict(menu=Menu.objects.get(url=url))


class Permission(models.Model):
    """ 权限 """
    name = models.CharField(max_length=32, unique=True, verbose_name="权限名称")
    menu = models.ForeignKey("Menu", blank=True, on_delete=models.CASCADE,
                    verbose_name="菜单URL授权")
    desc = models.CharField(max_length=128, blank=True, null=True, verbose_name="描述")
    enable = models.BooleanField(default=True, verbose_name="是否启用")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "权限"
        verbose_name_plural = verbose_name


class Role(models.Model):
    """ 角色 """
    name = models.CharField(max_length=32, unique=True, verbose_name="角色名称")
    permissions = models.ManyToManyField("Permission", blank=True, verbose_name="URL授权")
    desc = models.CharField(max_length=128, blank=True, null=True, verbose_name="描述")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name


class Structure(models.Model):
    """ 组织架构 """
    TYPE_CHOICES = (
        ("UNIT", "单位"),
        ("DEPARTMENT", "部门"),
    )

    name = models.CharField(max_length=60, verbose_name="名称")
    stru_type = models.CharField(max_length=20, choices=TYPE_CHOICES,
                    default="DEPARTMENT", verbose_name="类型")
    parent = models.ForeignKey("self", null=True, blank=True,
                on_delete=models.SET_NULL, verbose_name="父类架构")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "组织架构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AccountManager(BaseUserManager):
    """ 用户管理 """

    # use_in_migrations = True
    
    def _create_user(self, email, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('Users must have an email address.')
        if not username:
            raise ValueError('Users must have a username.')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)


class UserProfile(AbstractUser):
    """ 用户 """
    GENDER_CHOICES = (
        ("MALE", "男"),
        ("FEMALE", "女"),
        ("UNKNOWN", "保密"),
    )
    
    uid = models.CharField(max_length=32, unique=True, verbose_name="UID")
    username = models.CharField(max_length=80, unique=True, verbose_name="用户名")
    email = models.CharField(max_length=80, verbose_name="邮箱")
    mobile = models.CharField(max_length=11, default='', verbose_name="手机号码")
    nickname = models.CharField(max_length=50, null=True, blank=True,
                    verbose_name="昵称")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,
                    default="MALE", verbose_name="邮箱")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    # avatar = models.ImageField(upload_to="image/%Y/%m", default="image/default.jpg",
    #                 max_length=100, null=True, blank=True, verbose_name="头像")
    avatar_url = models.URLField(max_length=255, null=True, blank=True,
                    verbose_name="头像链接")
    structure = models.ForeignKey("Structure", null=True, blank=True,
                    on_delete=models.SET_NULL, verbose_name="组织架构")
    roles = models.ManyToManyField("Role", blank=True, verbose_name="角色")
    card_num = models.CharField(max_length=20, null=True, blank=True, verbose_name="身份证号码")
    real_name = models.CharField(max_length=20, null=True, blank=True, verbose_name="真实姓名")
    resume = models.CharField(max_length=20, null=True, blank=True, verbose_name="简介")
    location = models.CharField(max_length=100, null=True, blank=True, verbose_name="所在地")
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name="通讯地址")
    freeze = models.IntegerField(default=0, verbose_name="冻结")
    income = models.IntegerField(default=0, verbose_name="佣金")
    balance = models.IntegerField(default=0, verbose_name="余额")
    level = models.IntegerField(default=1, verbose_name="等级")
    is_superuser = models.BooleanField(default=False, verbose_name="是否超级管理员")
    is_staff = models.BooleanField(default=False, verbose_name="是否职员")
    is_lock = models.BooleanField(default=False, verbose_name="是否锁定")
    last_login_ip = models.CharField(max_length=20, null=True, blank=True, verbose_name="最近登录IP")
    last_login_ip_area = models.CharField(max_length=20, null=True, blank=True, verbose_name="最近登录地区")
    login_error_num = models.IntegerField(default=0, verbose_name="登录错误次数")
    date_joined = models.DateTimeField(null=True, verbose_name="注册时间")
    last_login = models.DateTimeField(null=True, verbose_name="最近登录时间")
    locked_at = models.DateTimeField(null=True, verbose_name="锁定时间")
    confirmed_at = models.DateTimeField(null=True, verbose_name="确认时间")
    signin_at = models.DateTimeField(null=True, verbose_name="最近签到时间")

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True

    @property
    def avatar(self):
        if not self.avatar_url:
            return settings.AVATAR_URL_PREFIX + settings.DEFAULT_AVATAR