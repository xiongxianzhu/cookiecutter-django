from rest_framework import serializers
from account.models import Menu, Role, Structure, UserProfile


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('id', 'name', 'menu_type', 'icon', 'code', 'url', 'created_at', 'updated_at')


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('id', 'name', 'desc', 'created_at', 'updated_at')


class StructureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Structure
        fields = ('id', 'name', 'stru_type', 'created_at', 'updated_at')


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('id', 'uid', 'username', 'email', 'mobile', 'nickname',
                    'gender', 'birthday', 'avatar_url', 'password',
                    'is_active', 'card_num', 'real_name', 'resume',
                    'location', 'address', 'freeze', 'income',
                    'balance', 'level', 'is_superuser', 'is_staff',
                    'is_lock', 'last_login_ip', 'last_login_ip_area',
                    'login_error_num', 'date_joined', 'last_login',
                    'locked_at', 'confirmed_at', 'signin_at')
        
