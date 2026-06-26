from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('websites/', views.website_list, name='website_list'),

    path('add/', views.add_website, name='add_website'),

    path('edit/<int:pk>/', views.edit_website, name='edit_website'),

    path('delete/<int:pk>/', views.delete_website, name='delete_website'),

    path('monitor/', views.monitor_websites, name='monitor_websites'),

    path('logs/', views.logs, name='logs'),

    path('website_logs/<int:pk>/',
         views.website_logs,
         name='website_logs'),

    path('notifications/',
         views.notifications_list,
         name='notifications_list'),

    path('notifications/<int:pk>/read/',
         views.mark_notification_read,
         name='mark_notification_read'),

    path('notifications/read-all/',
         views.mark_all_read,
         name='mark_all_read'),

    path('notifications/count/',
         views.notification_count,
         name='notification_count'),
]