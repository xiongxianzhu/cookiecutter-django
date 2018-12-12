# 项目模型-model

- Menu: 菜单管理，用来存储系统可用的URL
- Role: 角色组，通过外键关联Menu，角色组中的用户将继承Role关联菜单的访问权限
- Structure：组织架构，包含单位和部门信息
- UserProfile： 自定义用户认证模型，替换系统原有的User模型

on_delete :在django2.0版本以前，定关联字段时，on_delete选项并不是必须的，而在django2.0版本后，在定义关联字段时on_delete是必须要定义的，常用参数如下：

```
on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null
on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值
```

#### 菜单-Menu

属性 | 类型 | 必填 | 默认值 | 备注
:-|:-:|:-:|:-:|:-: 
id | int | 是 | | ID
name | string(30) | 是 | | 菜单名(unique=True)
parent | self | 是 | | 父菜单
menu_type | string(20) | 否 | | 菜单类型(MODEL='模型', CATEGORY='分类')
icon | string(50) | 是 | | 图标
code | string(50) | 是 | | 编码
url | string(128) | 是 | | 链接
desc | string(128) | 否 | | 描述
sort | int | 否 | 0 | 排序编号
created_at | datetime | 是 | datetime.now | 创建时间
updated_at | datetime | 是 | datetime.now | 更新时间

#### 权限-Permission

属性 | 类型 | 必填 | 默认值 | 备注
:-|:-:|:-:|:-:|:-: 
id | int | 是 | | ID
name | string(80) | 是 | | 权限名称
menu | Menu | 是 | | 菜单URL授权
desc | string(128) | 否 | | 描述
enable | boolean | 是 | True | 是否启用
created_at | datetime | 是 | datetime.now | 创建时间
updated_at | datetime | 是 | datetime.now | 更新时间

#### 角色-Role(组的概念)

属性 | 类型 | 必填 | 默认值 | 备注
:-|:-:|:-:|:-:|:-: 
id | int | 是 | | ID
name | string(32) | 是 | | 角色名称
permissions | List(Permission) | 是 | | 角色权限
desc | string(128) | 是 | | 描述
created_at | datetime | 是 | datetime.now | 创建时间
updated_at | datetime | 是 | datetime.now | 更新时间


#### 组织架构-Structure

属性 | 类型 | 必填 | 默认值 | 备注
:-|:-:|:-:|:-:|:-: 
id | int | 是 | | ID
name | string(60) | 是 | | 名称
stru_type | string(20) | 是 | "DEPARTMENT" | 类型(("unit", "单位"), ("department", "部门"))
parent | self | 是 | | 父架构
created_at | datetime | 是 | datetime.now | 创建时间
updated_at | datetime | 是 | datetime.now | 更新时间


#### 用户-UserProfile

属性 | 类型 | 必填 | 默认值 | 备注
:-|:-:|:-:|:-:|:-: 
id | int | 是 | | ID
uid | string(32) | 是 | | 用户ID(用户唯一标识)
username | string(80) | 否 | | 用户名(唯一)
email | string(80) | 否 | | 邮箱
mobile_phone | string(11) | 是 | '' | 手机号码
nickname | string(50) | 否 | | 昵称(可编辑， 可重复)
gender | string(10) | 否 | | 性别(MALE-男, FEMALE-女, UNKNOWN-保密)
birthday | date | 否 | | 出生日期(yyyy-MM-dd)
avatar | string(100) | 否 | | 头像(路径)
structure | Structure | 否 | | 组织架构
password | string(80) | 否 | | 密码
is_active | boolean | 是 | True | 是否激活
card_num | string(20) | 否 | | 身份证号码
real_name | string(20) | 否 | | 真实姓名
bio | string(100) | 否 | | 个人简介
location | string(100) | 否 | | 所在地
address | string(100) | 否 | | 通讯地址
roles | List(Role) | 否 | [] | 角色
freeze | int | 否 | 0 | 冻结
income | int | 否 | 0 | 佣金
balance | int | 否 | 0 | 余额
level | int | 否 | 1 | 等级
following | User | 否 | | 关注
followers | List(User) | 否 | | 好友
<!-- is_admin | boolean | 是 | False | 是否管理员 -->
is_superuser | boolean | 是 | False | 是否超级管理员
is_staff | boolean | 是 | False | 是否职员(可登录django管理后台)
is_lock | boolean | 是 | False | 是否锁定
last\_login\_ip | string(20) | 否 | | 最近登录IP
last\_login\_ip\_area | string(20) | 否 | | 最近登录地区
login\_error\_num | int | 是 | 0 | 登录错误次数
<!-- is_debug |  boolean | 是 | False | 允许调试
is_generate |  boolean | 是 | False | 是否生成 -->
date_joined | datetime | 是 | datetime.now | 注册时间
last_login | datetime | 是 | datetime.now | 最近登录时间
<!-- registered_at | datetime | 是 | datetime.now | 注册时间
logined_at | datetime | 是 | datetime.now | 最近登录时间 -->
locked_at | datetime | 是 | datetime(1970, 1, 1) | 锁定时间
confirmed_at | datetime | 是 | datetime(1970, 1, 1) | 确认时间
signin_at | datetime | 否 | datetime(1970, 1, 1) | 最近签到时间

#### 文章-Post

属性 | 类型 | 必填 | 默认值 | 备注
:-|:-:|:-:|:-:|:-: 
id | int | 是 | | ID
slug | string | 是 | | 文章唯一标识
author | User | 是 |  | 作者
title | string | 是 | | 标题
body | string | 否 | | 正文
category | PostCategory | 否 | | 分类
tags | List | 否 | | 标签
is_enable | bool | 是 | True | 是否发表
comments | List | 否 | | 评论
pub_time | datetime | 否 |  | 发表时间
created_at | datetime | 是 | datetime.now | 创建时间
updated_at | datetime | 是 | datetime.now | 更新时间

#### 文章分类-PostCategory

属性 | 类型 | 必填 | 默认值 | 备注
:-|:-:|:-:|:-:|:-: 
id | int | 是 | | ID
name | string(40) | 是 | | 名称
desc | string | 否 | | 描述
count | int | 是 | 0 | 数量
sort | int | 否 | 0 | 排序编号
is_enable | boolean | 是 | False | 是否启用
created_at | datetime | 是 | datetime.now | 创建时间
updated_at | datetime | 是 | datetime.now | 更新时间

#### 标签-Tag

属性 | 类型 | 必填 | 默认值 | 备注
:-|:-:|:-:|:-:|:-: 
id | int | 是 | | ID
name | string(30) | 是 | | 名称
created_at | datetime | 是 | datetime.now | 创建时间
updated_at | datetime | 是 | datetime.now | 更新时间

#### 评论-Comment

属性 | 类型 | 必填 | 默认值 | 备注
:-|:-:|:-:|:-:|:-: 
id | int | 是 | | ID
user | User | 是 | | 用户
body | string | 否 | | 内容
pub_time | datetime | 否 | | 评论时间
post | Post | 否 | | 文章
reply_comment | self | 否 | | 回复评论
created_at | datetime | 是 | datetime.now | 创建时间
updated_at | datetime | 是 | datetime.now | 更新时间