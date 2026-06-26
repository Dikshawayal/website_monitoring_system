from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .models import Website, MonitorLog, Notification
from .forms import WebsiteForm
from .checker import check_website


# ======================
# Dashboard
# ======================
@login_required
def dashboard(request):

    total = Website.objects.count()

    active = Website.objects.filter(status='UP').count()

    inactive = Website.objects.filter(status='DOWN').count()

    recent_websites = Website.objects.order_by('-last_checked')[:5]

    context = {
        'total': total,
        'active': active,
        'inactive': inactive,
        'recent_websites': recent_websites,
    }

    return render(
        request,
        'monitor/dashboard.html',
        context
    )


# ======================
# Website List
# ======================
@login_required
def website_list(request):

    search = request.GET.get('search')
    status = request.GET.get('status')

    websites = Website.objects.all()

    if search:
        websites = websites.filter(name__icontains=search)

    if status:
        websites = websites.filter(status=status)

    return render(
        request,
        'monitor/website_list.html',
        {'websites': websites}
    )


# ======================
# Check Websites
# ======================
@login_required
def monitor_websites(request):

    websites = Website.objects.all()

    for website in websites:

        result = check_website(website.url)

        prev_status = website.status
        website.status = result['status']
        website.response_time = result['response_time']
        website.last_checked = timezone.now()
        website.save()

        MonitorLog.objects.create(
            website=website,
            status=result['status'],
            status_code=result['status_code'],
            response_time=result['response_time']
        )

        if result['status'] == 'DOWN' and prev_status != 'DOWN':
            Notification.objects.create(
                website=website,
                message=f"{website.name} is DOWN!",
                type='DOWN'
            )

    messages.success(request, 'Website check completed!')
    return redirect('website_list')


# ======================
# Add Website
# ======================
@login_required
def add_website(request):

    if request.method == 'POST':

        form = WebsiteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Website added successfully!')
            return redirect('website_list')

    else:
        form = WebsiteForm()

    return render(
        request,
        'monitor/add_website.html',
        {'form': form}
    )


# ======================
# Edit Website
# ======================
@login_required
def edit_website(request, pk):

    website = get_object_or_404(
        Website,
        pk=pk
    )

    if request.method == 'POST':

        form = WebsiteForm(
            request.POST,
            instance=website
        )

        if form.is_valid():
            form.save()
            messages.success(request, 'Website updated successfully!')
            return redirect('website_list')

    else:

        form = WebsiteForm(
            instance=website
        )

    return render(
        request,
        'monitor/edit_website.html',
        {'form': form}
    )


# ======================
# Delete Website
# ======================
@login_required
def delete_website(request, pk):

    website = get_object_or_404(
        Website,
        pk=pk
    )

    if request.method == 'POST':

        website.delete()
        messages.success(request, 'Website deleted successfully!')
        return redirect('website_list')

    return render(
        request,
        'monitor/delete_website.html',
        {'website': website}
    )


# ======================
# All Monitoring Logs
# ======================
@login_required
def logs(request):

    logs = MonitorLog.objects.all().order_by('-checked_at')

    return render(
        request,
        'monitor/logs.html',
        {'logs': logs}
    )


# ======================
# Single Website Logs
# ======================
@login_required
def website_logs(request, pk):

    website = get_object_or_404(
        Website,
        pk=pk
    )

    logs = MonitorLog.objects.filter(
        website=website
    ).order_by('-checked_at')

    return render(
        request,
        'monitor/website_logs.html',
        {
            'website': website,
            'logs': logs
        }
    )


# ======================
# Notifications
# ======================
@login_required
def notifications_list(request):

    notifications = Notification.objects.all()[:20]

    return render(
        request,
        'monitor/notifications.html',
        {'notifications': notifications}
    )


@login_required
def mark_notification_read(request, pk):

    notification = get_object_or_404(
        Notification,
        pk=pk
    )
    notification.is_read = True
    notification.save()

    return JsonResponse({'status': 'ok'})


@login_required
def mark_all_read(request):

    Notification.objects.filter(
        is_read=False
    ).update(is_read=True)

    return JsonResponse({'status': 'ok'})


@login_required
def notification_count(request):

    count = Notification.objects.filter(
        is_read=False
    ).count()

    return JsonResponse({'count': count})