from django.shortcuts import render
from . serializers import UserSerializers,CategorySerializers,PostSerializers,CommentSerializers,ProductSerializers
from . models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import filters
from django_filters import rest_framework as django_filters
from rest_framework.views import APIView


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    return Response({
        'username': user.username,
        'email': user.email,
    })


@api_view(['POST'])
def register(request):
    serializer = UserSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    categories = User.objects.all()
    serializer = UserSerializers(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email is None or password is None:
        return Response({'error': 'Please provide both username and password'}
                        , status=status.HTTP_400_BAD_REQUEST)
    else:
        user = authenticate(email=email, password=password)
        if user is not None:
            return Response({'token': user.token})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

#create category API
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request):
    serializer = CategorySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#update category API
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializers(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 # delete category API
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response('Category deleted')


#get category API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_category(request):
    categories = Category.objects.all()
    serializer = CategorySerializers(categories, many=True)
    return Response(serializer.data)


#get post API
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = PostSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#get category API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post(request):
    post = Post.objects.all()
    serializer = PostSerializers(post, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializers(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 # delete category API
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response('post deleted')


#get comment API
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
    serializer = CommentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#get comment API
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comment(request):
    comment = Comment.objects.all()
    serializer = CommentSerializers(comment, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializers(instance=comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 # delete category API
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return Response('comment deleted')


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

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = (filters.SearchFilter, django_filters.DjangoFilterBackend)
    search_fields = ['name', 'description']  
    filterset_class = ProductFilter


class PayPalPaymentView(APIView):
    def post(self, request):
        order_id = request.data.get('order')
        payment_method = request.data.get('payment_method')
        payment_id = request.data.get('payment_id')
        payment_status = request.data.get('payment_status')
        
        if not all([order_id, payment_method, payment_id, payment_status]):
            return Response({"error": "Missing required fields"}, status=400)

        try:
            order = Product.objects.get(id=order_id)
        except Product.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        payment = Payment.objects.create(
            order=order,
            payment_method=payment_method,
            payment_id=payment_id,
            payment_status=payment_status,
        )

        return Response({"message": "Payment created successfully", "payment_id": payment.id}, status=201)










