from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from pin.models import Pin
from .serializers import PinSerializer, NoteSerializer

#############################################################################################################################
##  Start of Pin CRUD
#Create
@api_view(['POST'])
def pin_create(request):
    if request.method == 'POST':
        serializer = PinSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Read
@api_view(["GET"])
def pin_list(request):
    pins = Pin.objects.all()
    serialized_pins = PinSerializer(instance=pins, many=True)
    return Response(data=serialized_pins.data,status=status.HTTP_200_OK)

@api_view(["GET"])
def single_pin(request, pk):
    try:
        pin  = Pin.objects.get(pk = pk)
    except Exception as e:
        return Response(data={"msg": "this pin does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    serialized_pin = PinSerializer(instance=pin)
    return Response(data=serialized_pin.data,status=status.HTTP_200_OK)


#Update
@api_view(["PUT", "PATCH"])
def update_pin(request, pk):
    try:
        pin  = Pin.objects.get(pk = pk)      
    except Exception as e:
        return Response(data={"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    serialized_pin = PinSerializer(instance=pin, data = request.data )
    if serialized_pin.is_valid():
        serialized_pin.save()
        return Response(serialized_pin.data, status=status.HTTP_200_OK)
    return Response(serialized_pin.errors, status=status.HTTP_400_BAD_REQUEST)


#D
@api_view(["DELETE"])
def delete_pin(request, pk):
    res = {}
    try:
        pin  = Pin.objects.get(pk = pk)
        pin.delete()
        res['data']= 'Successfully deleted the pin'
        res['status'] = status.HTTP_200_OK
    except Exception as e:
        res['data']= 'Error While Deleting: {}'.format(str(e))
        res['status'] = status.HTTP_400_BAD_REQUEST
    
    return Response(data=res.get('data'), status = res.get('status'))

#End of Pin CRUD
#############################################################################################################################


#############################################################################################################################
##  Start of Note CRUD
#Create
@api_view(['GET'])
def note_create(request, pin_id):
    if request.method == 'GET':
        target_pin = Pin.objects.get(pk=pin_id)
        target_pin = PinSerializer(instance=target_pin) 
        newdict={'item':"test"}
        newdict.update(target_pin.data)
        return Response(target_pin.data, status=status.HTTP_200_OK)
        #serializer = NoteSerializer(data=request.data)
    #if serializer.is_valid():
    #    serializer.save()
    #    return Response(serializer.data, status=status.HTTP_200_OK)
    #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Read
@api_view(["GET"])
def pin_list(request):
    pins = Pin.objects.all()
    serialized_pins = PinSerializer(instance=pins, many=True)
    return Response(data=serialized_pins.data,status=status.HTTP_200_OK)

@api_view(["GET"])
def single_pin(request, pk):
    try:
        pin  = Pin.objects.get(pk = pk)
    except Exception as e:
        return Response(data={"msg": "this pin does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    serialized_pin = PinSerializer(instance=pin)
    return Response(data=serialized_pin.data,status=status.HTTP_200_OK)


#Update
@api_view(["PUT", "PATCH"])
def update_pin(request, pk):
    try:
        pin  = Pin.objects.get(pk = pk)      
    except Exception as e:
        return Response(data={"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    serialized_pin = PinSerializer(instance=pin, data = request.data )
    if serialized_pin.is_valid():
        serialized_pin.save()
        return Response(serialized_pin.data, status=status.HTTP_200_OK)
    return Response(serialized_pin.errors, status=status.HTTP_400_BAD_REQUEST)


#D
@api_view(["DELETE"])
def delete_pin(request, pk):
    res = {}
    try:
        pin  = Pin.objects.get(pk = pk)
        pin.delete()
        res['data']= 'Successfully deleted the pin'
        res['status'] = status.HTTP_200_OK
    except Exception as e:
        res['data']= 'Error While Deleting: {}'.format(str(e))
        res['status'] = status.HTTP_400_BAD_REQUEST
    
    return Response(data=res.get('data'), status = res.get('status'))




