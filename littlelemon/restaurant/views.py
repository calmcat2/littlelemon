from django.shortcuts import render
from rest_framework import generics,viewsets
from .serializers import MenuSerializer,BookingSerializer
from . import models
from rest_framework import permissions

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset=models.Menu.objects.all()
    serializer_class=MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=models.Menu.objects.all()
    serializer_class=MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset=models.Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes = [permissions.IsAuthenticated] 