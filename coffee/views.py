from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from .serializers import CoffeeMachineProductSerializer, CoffeePodProductSerializer
from .models import CoffeeMachineProduct as coffee_machine
from .models import CoffeePodProduct as coffee_pod, Category as product_category


class CoffeeMachineProduct(APIView):
    def get(self, request):
        query = Q()
        filterList = request.GET.items()
        if request.GET:
            for k,v in filterList:
                if k=='category':
                    query = query & Q(category=v)
                elif k=='water_line':
                    query = query & Q(water_line=v)

            queryset = coffee_machine.objects.filter(query)
        else:
            queryset = coffee_machine.objects.all().order_by('name')
        serializer = CoffeeMachineProductSerializer(queryset, many=True)
        return Response(serializer.data)


class CoffeePodProduct(APIView):

    def get(self, request):
        try:
            query = Q()
            filterList = request.GET.items()
            if request.GET:
                for k,v in filterList:
                    if k=='category':
                        query = query & Q(category=v)
                    elif k=='pack_size':
                        query = query & Q(pack_size=v)
                    elif k=='flavor':
                        query = query & Q(flavor=v)
                queryset = coffee_pod.objects.filter(query)
            else:
                queryset = coffee_pod.objects.all().order_by('name')
            serializer = CoffeePodProductSerializer(queryset, many=True)
        except Exception as e:
            return Response(e)

        return Response(serializer.data)
