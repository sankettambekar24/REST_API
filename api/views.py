from django.shortcuts import render
from django.http import JsonResponse
from api.models import Student
from api.serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import employee
from django.http import Http404
from rest_framework import generics,mixins
from blogs.models import blog,comment
from blogs.serializer import commentSerializer,blogSerializer

@api_view(['GET','POST'])
def studentsview(request):
    if request.method=='GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer= StudentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','DELETE'])
def studentsDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='POST':
         serializer=StudentSerializer(student,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_200_OK)
         else:
             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# class EmployeeList(APIView):
#     def get(self,request):
#         employees = employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer =EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)



# class EmployeeDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return employee.objects.get(pk=pk)
#         except employee.DoesNotExist:
#             raise Http404

#     def get(self, request,pk):
#         employee= self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self,request,pk):
#         employee = self.get_object(pk)
#         serializer= EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    

#     def delete(self,request,pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


### mixins
# class EmployeeList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset= employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
# class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset= employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self,request,pk):
#         return self.retrieve(request,pk)

#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
    
    # generics


class EmployeeList(generics.ListCreateAPIView):
    queryset= employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset= employee.objects.all()
     serializer_class = EmployeeSerializer
     lookup_field='pk'








##neseted serializer

class BlogView(generics.ListCreateAPIView):
    queryset= blog.objects.all()
    serializer_class= blogSerializer
    

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= blog.objects.all()
    serializer_class= blogSerializer
    lookup_field='pk'


class CommentView(generics.ListCreateAPIView):
    queryset= comment.objects.all()
    serializer_class= commentSerializer
    

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= comment.objects.all()
    serializer_class= commentSerializer
    lookup_field='pk'