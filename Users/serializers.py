from rest_framework import serializers
from Users.models import Customer,Manager

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Customer
        # fields = '__all__'
        exclude = ['is_admin','is_active']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    def validate(self,attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError('''Your Passwords Doesn't Match''')
        return super().validate(attrs)
    def create(self,validate_data):
        validate_data.pop('password2',None)
        return Customer.objects.create_user(**validate_data)
    
class ManagerRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Manager
        # fields = '__all__'
        exclude = ['is_admin','is_active']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    def validate(self,attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError('''Your Passwords Doesn't Match''')
        return super().validate(attrs)
    def create(self,validate_data):
        validate_data.pop('password2',None)
        return Manager.objects.create_user(**validate_data)
    
class CustomerLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = Customer
        fields = ['email','password']

class ManagerLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = Manager
        fields = ['email','password']

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ['password','last_login']

class ManagerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        exclude = ['password','last_login']