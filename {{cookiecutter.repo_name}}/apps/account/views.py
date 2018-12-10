# from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import Menu, Role, Structure, UserProfile
from account.serializers import (MenuSerializer, RoleSerializer,
        StructureSerializer, UserProfileSerializer)


# class MenuList(APIView):

#     def get(self, request, format=None):
#         menus = Menu.objects.all()
#         serializer = MenuSerializer(menus, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         serializer = MenuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class MenuDetail(APIView):

#     def getObject(self, pk):
#         try:
#             return Menu.objects.get(pk=pk)
#         except Menu.DoesNotExist as e:
#             raise Http404

#     def get(self, request, pk, format=None):
#         menu = self.getObject(pk)
#         serializer = MenuSerializer(menu)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         menu = self.getObject(pk)
#         serializer = MenuSerializer(menu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         menu = self.getObject(pk)
#         menu.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class StructureList(generics.ListCreateAPIView):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer


class StructureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer


class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
