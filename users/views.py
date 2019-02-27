from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import models
from rest_framework.authtoken.models import Token
from . import serializers
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
import requests
from requests.auth import HTTPDigestAuth
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from .models import TravellerDetails, TicketDetails
url = "http://test.etravelsmart.com/etsAPI/api/"
# class UserListView(generics.ListCreateAPIView):
#     queryset = models.CustomUser.objects.all()
#     serializer_class = serializers.UserSerializer

url = "http://test.etravelsmart.com/etsAPI/api/"


class UserListView(APIView):
    serializer_class = UserSerializer

    # def get(self, request):
    #     user = models.CustomUser.objects.all()
    #     serializer = UserSerializer(user, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        # data = JSONParser().parse(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     user = self.get_object(pk)
    #     user.delete()
    #     return Response("No content",status=status.HTTP_204_NO_CONTENT)


class UserLogin(APIView):
    # def get(self, request):
    #     user = models.CustomUser.objects.all()
    #     serializer = UserSerializer(user, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        # data = JSONParser().parse(request)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     user = self.get_object(pk)
    #     user.delete()
    #     return Response("No content",status=status.HTTP_204_NO_CONTENT)


class UserUpdate(APIView):
    serializer_class = UserSerializer

    def get_object(self, pk):
        try:
            return models.CustomUser.objects.get(pk=pk)
        except models.CustomUser.DoesNotExist:
            raise NotFound(detail="Error 404, page not found", code=404)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    serializer_class = UserSerializer

    def get_object(self, pk):
        try:
            return models.CustomUser.objects.get(pk=pk)
        except models.CustomUser.DoesNotExist:
            raise NotFound(detail="Error 404, page not found", code=404)

    def get(self, request, pk):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)


class Logged_in_users(APIView):

    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class CheckEmailAvail(APIView):

    def get_object(self, pk):
        try:
            return models.CustomUser.objects.get(pk=pk)
        except models.CustomUser.DoesNotExist:
            raise NotFound(detail="Error 404, page not found", code=404)

    def get(self, request, pk):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)


class DeleteSpecificUser(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CityInfo(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        url = "http://test.etravelsmart.com/etsAPI/api/getStations"
        response = requests.get(url, auth=HTTPDigestAuth("TixdoAPI1", "123456"), timeout=10)

        json_data = json.loads(response.text)

        return Response(json_data, status=status.HTTP_200_OK)





class AvailableBuses(APIView):
    # permission_classes = (permissions.IsAuthenticated)
    # permission_classes = permissions.IsAuthenticatedOrReadOnly

    def get(self, request, *args, **kwargs):

        source = self.request.query_params.get('from')
        destination = self.request.query_params.get('to')
        dateOfJour = self.request.query_params.get('doj')
        routeScheduledId = self.request.query_params.get('routeScheduleId')

        get_bus_url = url+"getAvailableBuses?sourceCity="+source+"&destinationCity="+destination+"&doj="+dateOfJour

        response = requests.get(get_bus_url, auth=HTTPDigestAuth("TixdoAPI1", "123456"), timeout=10)
        json_data = json.loads(response.text)

        json_array = json_data['apiAvailableBuses']

        my_list = []

        for d in json_array:
            b_id = d['routeScheduleId']
            if routeScheduledId == b_id:
                my_list.append(d)

        json_data = json.dumps(my_list)

        json_data = json.loads(json_data)

        return Response(json_data, status=status.HTTP_200_OK)



class GetBusLayout(APIView):

    def get(self,request, *args, **kwargs):

        source = self.request.query_params.get('from')
        destination = self.request.query_params.get('to')
        date = self.request.query_params.get('doj')
        inventory = self.request.query_params.get('inventoryType')
        routeScheduledId = self.request.query_params.get('routeScheduleId')

        get_bus_info = url+"getBusLayout?sourceCity="+source+"&destinationCity="+destination+"&doj="+date+"&inventoryType="+inventory+"&routeScheduleId="+routeScheduledId

        response = requests.get(get_bus_info, auth=HTTPDigestAuth("TixdoAPI1", "123456"), timeout=10)
        jd = json.loads(response.text)

        return Response(jd, status=status.HTTP_200_OK)


class getRTCUpdatedFare(APIView):
    def get(self, request, *args, **kwargs):
        blockticket_key = self.request.query_params.get('blockTicketKey')

        get_rtc_url = url+"getRtcUpdatedFare?blockTicketKey="+str(blockticket_key)

        response = requests.get(get_rtc_url, auth=HTTPDigestAuth("TixdoAPI1", "123456"), timeout=10)

        json_data = json.loads(response.text)

        return Response(json_data, status=status.HTTP_200_OK)



class blockBusSeat(APIView):
    def post(self, request, *args, **kwargs):

        block_bus_url = url+"blockTicket"

        response = requests.post(block_bus_url, json=request.data, auth=HTTPDigestAuth("TixdoAPI1", "123456"),timeout=10)

        json_data = json.loads(response.text)

        return Response(json_data, status=status.HTTP_200_OK)



class getTicketByETSTNumber(APIView):
    def get(self, request, *args, **kwargs):

        ETSTNumber = self.request.query_params.get('ETSTNumber')

        etst_url = url+"getTicketByETSTNumber?ETSTNumber="+str(ETSTNumber)

        response = requests.get(etst_url, auth=HTTPDigestAuth("TixdoAPI1", "123456"), timeout=10)

        json_data = json.loads(response.text)

        etstNum = json_data['etstnumber']

        json_array = json_data["travelerDetails"]

        for d in json_array or []:
            travellerDetails = TravellerDetails()

            travellerDetails.name = d['name']
            travellerDetails.lastName = d['lastName']
            travellerDetails.seatnum = d['seatNo']
            travellerDetails.age = d['age']
            travellerDetails.gender = d['gender']
            travellerDetails.fare = d['fare']
            travellerDetails.etstNumber = etstNum

            ticketStatus = json_data["ticketStatus"]

            if ticketStatus != "CONFIRMED":
                travellerDetails.ticketStatus = ticketStatus

            travellerDetails.save()

            # TicketDetails Database Implementation

            pnr = json_data['opPNR']

            ticketDetails = TicketDetails()
            ticketDetails.etstnum = etstNum
            ticketDetails.pnrnum = pnr
            ticketDetails.ticketdump = json_data
            ticketDetails.ticketStatus = json_data['ticketStatus']
            ticketDetails.save()

        return Response(json_data, status=status.HTTP_200_OK)






class CancelTicketConfirmation(APIView):
    def post(self, request, *args, **kwargs):
        cancel_url = url + "cancelTicketConfirmation"

        response = requests.post(cancel_url, json=request.data, auth=HTTPDigestAuth("TixdoAPI1", "123456"), timeout=10)
        json_data = json.loads(response.text)

        return Response(json_data, status=status.HTTP_200_OK)


class CancelTicket(APIView):
    def post(self, request, *args, **kwargs):
        cancel_url = url + "cancelTicket"
        response = requests.post(cancel_url, json=request.data, auth=HTTPDigestAuth("TixdoAPI1", "123456"), timeout=10)
        json_data = json.loads(response.text)

        return Response(json_data, status=status.HTTP_200_OK)