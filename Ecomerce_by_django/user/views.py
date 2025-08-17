from .serializers import UserSerializer
from .models import CustomeUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from order.serializers import OrderSerializer


class UserRegisterView(APIView):
    authentication_classes = []
    throttle_classes = [AnonRateThrottle]

    @extend_schema(request=UserSerializer, responses={200: UserSerializer})
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        password = serializer.validated_data["password"]

        user = CustomeUser.objects.create_user(
            name=serializer.validated_data["name"],
            username=serializer.validated_data["username"],
            email=serializer.validated_data["email"],
            password=password,
            role=serializer.validated_data["role"],
            status=serializer.validated_data["status"],
            phone=serializer.validated_data["phone"],
            city=serializer.validated_data["city"],
            address=serializer.validated_data["address"],            
        )

        return Response({"User ": UserSerializer(user).data}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):

        username = request.user.username
        total_orders = request.user.user_orders.all()
        for order in total_orders:
            serializer = OrderSerializer(order)
        return Response({"Username is  ": username, "total  orders": total_orders.count() , 'order status':serializer.data['status'] })