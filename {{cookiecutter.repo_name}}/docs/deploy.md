# 部署文档

#### 创建数据库

创建数据库, 数据库名为`xfish`， 且编码为utf8， 以支持中文， 如下：
```
mysql> create database xfish DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

#### 创建数据库表

```
python manage.py migrate
```

#### 创建管理员

```
python manage.py createsuperuser
```