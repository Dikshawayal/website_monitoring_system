from .models import Notification


def notifications(request):
    if request.user.is_authenticated:
        unread_count = Notification.objects.filter(
            is_read=False
        ).count()
        recent = Notification.objects.all()[:5]
        return {
            'unread_count': unread_count,
            'recent_notifications': recent,
        }
    return {
        'unread_count': 0,
        'recent_notifications': [],
    }
