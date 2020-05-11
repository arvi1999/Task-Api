from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Category,Item
from .serializers import CategorySerializer, ItemSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['POST'])
    def create_category(self, request, pk=None):
        if 'name' in request.data:
            name = request.data['name']
            user = request.user
            # user = User.objects.get(id=1)
            category = Category.objects.create(user=user, name=name)
            serializer = CategorySerializer(category, many=False)
            response = {'message': 'Category created', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide Category Name'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def update_category(self, request, pk=None):
        if 'name' in request.data:
            name = request.data['name']
            user = request.user
            category = Category.objects.get(id=pk, user = user.id)
            category.name = name
            category.save()
            serializer = CategorySerializer(category, many=False)
            response = {'message': 'Category updated', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'You need to provide Category Name and User details'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'])
    def delete_category(self, request, pk=None):
        # user = User.objects.get(id=1)
        user = request.user
        category = Category.objects.get(id=pk,user = user.id)
        category.delete()
        serializer = CategorySerializer(category, many=False)
        response = {'message':'Category deleted', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def get_category(self, request, pk=None):
        category = Category.objects.filter(user=request.user.id)
        serializer = CategorySerializer(category, many=True)
        response = {'message': 'Categories created by logged in User', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update category like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create category like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You cant delete category like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def update_item(self, request, pk=None):
        if 'title' and 'description' and 'due_date' in request.data:
            title = request.data['title']
            description = request.data['description']
            due_date = request.data['due_date']
            user = request.user
            # user = User.objects.get(id=1)
            item = Item.objects.get(user=user.id, id=pk)
            item.title = title
            item.description = description
            item.due_date = due_date
            item.save()
            serializer = ItemSerializer(item, many=False)
            response = {'message': 'Item details Updated', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'Please provide all details i.e. title, description and due_date. You cant update Category'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['GET'])
    def get_item(self, request, pk=None):
        item = Item.objects.filter(user = request.user.id)
        serializer = ItemSerializer(item, many = True)
        response = {'message':'Items list for logged in User', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)


    #
    # @action(detail=False, methods=['POST'])
    # def create_item(self, request, pk=None):
    #     if 'title' and 'description' and 'due_date' and 'category' in request.data:
    #         title = request.data['title']
    #         description = request.data['description']
    #         due_date = request.data['due_date']
    #         user = request.user
    #         category = request.data['category']
    #         # user = User.objects.get(id=1)
    #         item = Item.objects.create(title = title, description = description, due_date = due_date, user=user, category = category)
    #         serializer = ItemSerializer(item, many=False)
    #         response = {'message': 'New Item created', 'result': serializer.data}
    #         return Response(response, status=status.HTTP_200_OK)
    #     else:
    #         response = {
    #             'message': 'Please provide all details i.e. title, description and due_date and category.'}
    #         return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['DELETE'])
    def delete_item(self, request, pk=None):
        # user = User.objects.get(id=1)
        user = request.user
        item = Item.objects.get(id=pk, user = user.id)
        item.delete()
        serializer = ItemSerializer(item, many=False)
        response = {'message': 'Item deleted', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)


    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update an Item like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'You cant delete an Item like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # def create(self, request, *args, **kwargs):
    #     response = {'message': 'You cant create and item like this'}
    #     return Response(response, status=status.HTTP_400_BAD_REQUEST)


