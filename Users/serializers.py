from rest_framework import serializers
from Users.models import Complains, User, Messages
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
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
        return User.objects.create_user(**validate_data)
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password','last_login']

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'
        
class ComplainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complains
        fields = '__all__'