from rest_framework import serializers
from . models import *
from django_filters import rest_framework as django_filters

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductFilter(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    availability = django_filters.BooleanFilter(field_name='stock', method='filter_availability')

    class Meta:
        model = Product
        fields = ['price_range', 'category', 'availability']

    def filter_availability(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset        
