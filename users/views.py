from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer

# Create your views here.
#for API
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
        })

#for django template
def register_page(request):
    if request.method == "POST":
        data = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
        }

        serializer = RegisterSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return render(request, "users/register.html", {
                "success": "Account created successfully!"
            })

        return render(request, "users/register.html", {
            "errors": serializer.errors
        })

    return render(request, "users/register.html")