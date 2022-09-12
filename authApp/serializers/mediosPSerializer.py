from authApp.models.mediosP import MediosP
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediosP
        fields = ['valorApagar', 'efectivo', 'tarjeta_debito','tarjeta_credito','pse',]
        
