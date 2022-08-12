import json
from core.serializers import *
# from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import IntegrityError
# from accounts.models import User
from rest_framework.pagination import PageNumberPagination



# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def create_api(request):
#     f = request.FILES['file']
#     n = request.POST.get('name')
#     ad = request.POST.get('address')
#     try:
#         p = Model.objects.create(name=n, location=ad, logo=f)
#     except IntegrityError:
#         return Response({"message": "Model already exists"}, status=status.HTTP_409_CONFLICT)
#     except Exception as e:
#         print(e)
#         return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#     return Response({'message': 'success'}, status = status.HTTP_200_OK)



# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def profile_api(request):
#     return Response({"fname" : request.user.fname, "lname" : request.user.lname, "credit":request.user.credit, "is_investor":(request.user.is_prop_dealer == False)})





# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def api_with_pages(request):


#     paginator = PageNumberPagination()
#     paginator.page_size = 20
#     ideas = Project.objects.all().order_by("-created_at")
#     result_page = paginator.paginate_queryset(ideas, request)
#     serializer = ProjectSerializer(result_page, many=True)
#     return paginator.get_paginated_response(serializer.data)



# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def api_with_parameter(request, id):
#     try:
#         p = Project.objects.get(id=id)
#         serializer = ProjectSerializer(p)
#         return Response({"message": "success", "project": serializer.data}, status=status.HTTP_200_OK)
#     except Project.DoesNotExist:
#         return Response({"message": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND)


# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def api_recieves_json_data(request, id):
#     data = json.loads(request.body)

#     try:
#         #do something with data
#         return Response({"message": "success", "appart": a.id}, status=status.HTTP_200_OK)

#     except Exception as e:
#         print(e)
#         return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)



# @api_view(["POST"])
# @permission_classes((IsAuthenticated, ))
# def api_recieves_form_data(request, id):
#     files = request.FILES.getlist('files')
#     file = request.FILES.get('file')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     try:
#         #do something with data
#         return Response({"message": "success"}, status=status.HTTP_200_OK)

#     except Exception as e:
#         print(e)
#         return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)






