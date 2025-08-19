from rest_framework import serializers
from .models import Coupons


class CouponSerializers(serializers.ModelSerializer):
    class Meta:
        model =Coupons
        fields = ['id' , 'discount_value' ,'discount_type' , 'active' , 'coupon']
