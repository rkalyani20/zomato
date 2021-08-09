from app.models import Menu, Order, Restaurant
from rest_framework.response import Response
from app.serializers import RestaurantSerializer, MenuSerializer, OrderSerializer, Userseriealizer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated


#Create your views here.
class SignupApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = Userseriealizer(data= request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors)



class RestaurantApi(APIView): 
    permission_classes = (IsAuthenticated,)

    def post(self, request):                                            #Create
        serializer = RestaurantSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):        
        cat = Restaurant.objects.all()
        ser = RestaurantSerializer(cat,many = True)
        return Response(ser.data)

    
    def put(self, request):
        id = request.POST.get("id")        
        name = request.POST.get("name")        
        contact = request.POST.get("contact")        
        address = request.POST.get("address")        
        try:
            qs = Restaurant.objects.get(id=id)
            if qs:
                qs.name = name
                qs.contact = contact
                qs.address = address
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Restaurant Information Has Been Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:
            resp = {
                'success' : 'false',
                'message' : "Something went wrong please try again later",      
                }    
        return Response(resp, status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request):
        id = request.POST.get("id")  
        try:           
            qs = Restaurant.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Restaurant Deleted",
                    }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
    
class MenuApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = MenuSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)
        
class ShowMenuApi(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):        
        cat = Menu.objects.all()
        ser = MenuSerializer(cat,many = True)
        return Response(ser.data)
    
    # def get(self,request):
    #     id = request.GET.get('id')
    #     if id is not None:
    #         menu = Menu.objects.filter(restaurant_name=id)
    #         ser = MenuSerializer(menu,many=True)
    #         return Response(ser.data)   
    #     resp = {
    #             'success' : 'false',
    #             'message' : "Something went wrong try again",      
    #             }    
    #     return Response(resp, status=status.HTTP_304_NOT_MODIFIED)

class Placeorder(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        ser = OrderSerializer(data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data,status= status.HTTP_201_CREATED)

        return Response(ser.errors,status= status.HTTP_400_BAD_REQUEST)

       
class ShowOrderApi(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):        
        cat = Order.objects.all()
        ser = OrderSerializer(cat,many = True)
        return Response(ser.data)