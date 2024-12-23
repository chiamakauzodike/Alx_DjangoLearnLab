from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Notification

# Create your views here.

class NotificationListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all()
        unread_count = notifications.filter(read=False).count()

        # Mark all as read (optional)
        notifications.update(read=True)

        return Response({
            'unread_count': unread_count,
            'notifications': [
                {
                    'id': n.id,
                    'actor': n.actor.username,
                    'verb': n.verb,
                    'timestamp': n.timestamp,
                    'read': n.read,
                    'target': str(n.target) if n.target else None
                } for n in notifications
            ]
        })
