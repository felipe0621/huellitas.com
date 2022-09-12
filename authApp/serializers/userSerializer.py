from rest_framework import serializers
from authApp.models import MediosP, User, mediosP
from .mediosPSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'idCard', 'address', 'phone', 'email', 'mediosP']
        
    def create(self, validated_data):
        mediosPData = validated_data.pop('mediosP')
        userInstance = User.objects.create(**validated_data)
        MediosP.objects.create(user=userInstance, **mediosPData)
        return userInstance
    
    def to_representation(self, obj):
      user = User.objects.get(id=obj.id)
      account = MediosP.objects.get(user=obj.id)
      return{
          'id': user.id,
          'username': user.username,
          'name': user.name,
          'idCard': user.idCard, 
          'address': user.address,
          'phone': user.phone,    
          'email': user.email,
          'account': {
              'id': mediosP.id,
              'valorApagar': mediosP.valorApagar,
              'efectivo': mediosP.efectivo,
              'tarjeta_debito': mediosP.tarjeta_debito,
              'tarjeta_credito': mediosP.tarjeta_credito,             
              'pse': mediosP.pse
          }          
      }  
