from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups','is_superuser','avatar')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

# 获取用户个人信息序列化器
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' #所有列的数据
        depth = 2  # 查询深度

def check_username(username):
    if len(username) < 6:
        raise serializers.ValidationError('不能小于6个字符')
    return username

class UserCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id','username','email')
        fields = '__all__'
        read_only_fields = ('last_login','date_joined','groups','user_permissions') #只读字段
        depth = 2  # 查询深度
        # 使用extra_kwargs参数为ModelSerializer添加或修改原有的选项参数
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'username': {'required': True, 'validators':[check_username]},
        }

    # 由于用户表中的密码要特殊处理-加密(set_password)需要重写内部提供的create方法
    def create(self, validated_data):
        user = User(**validated_data)
        # 对密码进行加密
        user.set_password(validated_data['password'])
        user.save()
        return user

    # 由于用户表中的密码要特殊处理-加密(set_password)需要重写内部提供的update方法
    def update(self, instance, validated_data):
        for key,value in validated_data.items():
            setattr(instance,key,value)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

    # validate_<field_name> 方法:对 <field_name> 字段进行验证
    def validate_last_name(self, value):
        if len(value) > 10:
            raise serializers.ValidationError('姓名过长')
        return value

    # validate 方法:对多个字段进行比较校验
    def validate(self, attrs):
        username = attrs['username']
        last_login = attrs['is_superuser']
        return attrs