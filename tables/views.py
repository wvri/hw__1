from rest_framework import generics
from .models import Table
from .serializers import TableSerializer
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from rest_framework.decorators import api_view

class TableListCreateView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

@api_view(['GET'])
def available_tables(request):
    date_str = request.GET.get('date')
    if not date_str:
        return Response({'error': 'Date parameter is required'}, status=400)
    
    date = parse_date(date_str)
    reserved_tables = Reservation.objects.filter(date=date).values_list('table_id', flat=True)
    available_tables = Table.objects.exclude(id__in=reserved_tables)
    
    serializer = TableSerializer(available_tables, many=True)
    return Response(serializer.data)
