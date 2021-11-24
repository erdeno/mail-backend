from django.shortcuts import Http404


from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes


from .models import Email

from .serializers import EmailSerializer



@authentication_classes([authentication.TokenAuthentication])
class EmailsList(APIView):
    def get(self, request, mailbox, format=None):
        if mailbox == "inbox":
            emails = Email.objects.filter(receiver=request.user, archived=False)
        elif mailbox == "sent":
            emails = Email.objects.filter(sender=request.user)
        elif mailbox == "archive":
            emails = Email.objects.filter(receiver=request.user, archived=True)
        else:
            return Response({'error': 'invalid mailbox'})
        emails = emails.order_by("-timestamp").all()
        serializer = EmailSerializer(emails, many=True)
        return Response(serializer.data)

@authentication_classes([authentication.TokenAuthentication])
class EmailDetail(APIView):
    def get_object(self, user, emailId):
        try:
            return Email.objects.get(receiver=user, pk=emailId)
        except Email.DoesNotExist:
            raise Http404
        
    def get(self, request, emailId, format=None):
        user = request.user
        email = self.get_object(user, emailId)
        serializer = EmailSerializer(email)
        return Response(serializer.data)
    
    def put(self, request, emailId, format=None):
        user = request.user
        email = self.get_object(user, emailId)  
        if request.data.get('read'):
            print(request.data.get('read'))
            email.read = request.data.get('read')
            email.save()
        elif request.data.get('archived'):
            email.archived = request.data.get('archived')
            email.save()
        serializer = EmailSerializer(email)
        return Response(serializer.data) 
        
        
            
        