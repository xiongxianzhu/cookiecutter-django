from django.conf.urls import url
# 格式后缀
from rest_framework.urlpatterns import format_suffix_patterns
from account import views


urlpatterns = [
    url(r'^menus/$', views.MenuList.as_view()),
    url(r'^menus/(?P<pk>\d+)/$', views.MenuDetail.as_view()),
    url(r'^roles/$', views.RoleList.as_view()),
    url(r'^roles/(?P<pk>\d+)/$', views.RoleDetail.as_view()),
    url(r'^structures/$', views.StructureList.as_view()),
    url(r'^structures/(?P<pk>\d+)/$', views.StructureDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
