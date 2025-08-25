from .serializers import UserSerializer , ProfileSerializer , UpdateUserRoleSerializer
from .models import CustomeUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from order.serializers import OrderSerializer
from rest_framework import generics
from products.permissions import IsAdminOrReadOnly


class UserRegisterView(APIView):
    authentication_classes = []
    throttle_classes = [AnonRateThrottle]

    @extend_schema(request=UserSerializer, responses={200: UserSerializer})
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'user':serializer.data} , 201)
        return Response({'erorr':serializer.errors} , 400)




class UserOrderDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        username = request.user.username
        total_orders = request.user.user_orders.all()

        orders_list = []
        for order in total_orders:
            serializer = OrderSerializer(order)
            orders_list.append(
                {
                    "order_id": serializer.data["id"],
                    "status": serializer.data["status"],
                    "total_price": serializer.data["total_price"],
                }
            )

        return Response(
            {
                "username": username,
                "total_orders": total_orders.count(),
                "orders": orders_list,
            }
        )


class UpdateProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = CustomeUser.objects.all()

    def get_object(self):
            return self.request.user
    
    http_method_names = ['get' , 'put']        

    


class UpdateUserRoleView(generics.UpdateAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = UpdateUserRoleSerializer
    queryset = CustomeUser.objects.all()

    def put(self , request, *args, **kwargs):
        return self.update(request ,*args, **kwargs )
            
    http_method_names = ['put']        
    


 