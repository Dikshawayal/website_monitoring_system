from django.utils import timezone

CSS = """
body{margin:0;padding:0;background-color:#f4f6fa;font-family:'Segoe UI',Arial,Helvetica,sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}
.email-wrapper{max-width:700px;margin:0 auto;padding:32px 20px}
.email-card{background:#ffffff;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,0.07),0 2px 8px rgba(0,0,0,0.04);overflow:hidden}
.logo-row{padding:24px 36px 0 36px;text-align:center}
.logo-text{font-size:18px;font-weight:800;color:#1e1e2f;letter-spacing:-0.4px}
.logo-dot{color:#0d6efd;font-size:22px}
.banner-red{background:linear-gradient(135deg,#dc3545 0%,#a71d2a 100%);padding:28px 36px;text-align:center}
.banner-green{background:linear-gradient(135deg,#198754 0%,#116a3e 100%);padding:28px 36px;text-align:center}
.banner-orange{background:linear-gradient(135deg,#fd7e14 0%,#cc5f0a 100%);padding:28px 36px;text-align:center}
.banner-icon{font-size:42px;line-height:1}
.banner-title{color:#ffffff;font-size:24px;font-weight:700;margin:10px 0 4px 0;letter-spacing:-0.4px}
.banner-sub{color:rgba(255,255,255,0.88);font-size:14px;margin:0;line-height:1.5}
.body-content{padding:32px 36px}
.section-head{font-size:14px;font-weight:700;color:#1e1e2f;margin:28px 0 14px 0;padding-bottom:8px;border-bottom:2px solid #eef1f6;letter-spacing:-0.2px}
.data-table{width:100%;border-collapse:collapse;margin:0 0 4px 0;border-radius:10px;overflow:hidden}
.data-table td{padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6}
.data-table .lbl{color:#6b7280;font-weight:600;width:44%;background:#fafbfd}
.data-table .val{color:#1e1e2f;font-weight:500;width:56%}
.badge{display:inline-block;padding:5px 16px;border-radius:20px;font-size:12px;font-weight:700;letter-spacing:0.4px;text-transform:uppercase}
.badge-red{background:#fce8e8;color:#b91c1c}
.badge-green{background:#e3f5eb;color:#0c6b3e}
.badge-orange{background:#fff1e0;color:#bd5b00}
.alert-box{padding:14px 20px;border-radius:10px;margin:0 0 18px 0;font-size:13.5px;line-height:1.6}
.alert-red{background:#fef2f2;border:1px solid #fecaca;color:#991b1b}
.alert-green{background:#f0fdf4;border:1px solid #bbf7d0;color:#166534}
.alert-orange{background:#fff7ed;border:1px solid #fed7aa;color:#9a3412}
.action-item{padding:7px 0;font-size:13.5px;color:#374151;line-height:1.6}
.action-check{color:#198754;font-weight:700;margin-right:8px}
.action-cross{color:#dc3545;margin-right:8px}
.btn-row{text-align:center;padding:22px 0 6px 0}
.btn{display:inline-block;padding:13px 32px;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;text-align:center;letter-spacing:0.2px;border:none}
.btn-red{background:#dc3545;color:#ffffff}
.btn-green{background:#198754;color:#ffffff}
.btn-orange{background:#fd7e14;color:#ffffff}
.btn-sec{background:#ffffff;color:#374151;border:2px solid #dce0e8;margin-left:8px}
.footer-row{background:#f8fafd;padding:24px 36px;text-align:center;border-top:1px solid #eef1f6}
.footer-name{font-size:16px;font-weight:700;color:#1e1e2f;letter-spacing:-0.3px}
.footer-tag{font-size:12px;color:#9ca3af;margin:4px 0 16px 0}
.footer-links{font-size:12px;color:#9ca3af;line-height:1.8}
.footer-links a{color:#0d6efd;text-decoration:none}
.footer-copy{font-size:11px;color:#b8bfcc;margin-top:12px}
.divider{height:1px;background:#eef1f6;margin:24px 0}
"""


def website_down_email(website, result):
    now = timezone.now().strftime("%d %b %Y, %I:%M:%S %p")
    rtime = result.get('response_time', 'N/A')
    scode = result.get('status_code', 'N/A')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>{CSS}</style>
</head>
<body>
<table class="email-wrapper" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:700px;margin:0 auto;padding:32px 20px;background:#f4f6fa;">
<tr><td align="center">

<table class="email-card" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,0.07),0 2px 8px rgba(0,0,0,0.04);max-width:700px;">
<tr><td>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="logo-row" style="padding:24px 36px 0 36px;text-align:center;">
<span class="logo-text" style="font-size:18px;font-weight:800;color:#1e1e2f;letter-spacing:-0.4px;"><span class="logo-dot" style="color:#0d6efd;font-size:22px;">&#9679;</span> WEBSITE MONITORING SYSTEM</span>
</td></tr>
</table>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="banner-red" style="background:linear-gradient(135deg,#dc3545 0%,#a71d2a 100%);padding:28px 36px;text-align:center;">
<div class="banner-icon" style="font-size:42px;line-height:1;">&#128680;</div>
<h1 class="banner-title" style="color:#ffffff;font-size:24px;font-weight:700;margin:10px 0 4px 0;letter-spacing:-0.4px;">Critical Website Down Alert</h1>
<p class="banner-sub" style="color:rgba(255,255,255,0.88);font-size:14px;margin:0;line-height:1.5;">Immediate attention required &mdash; a monitored website is unavailable</p>
</td></tr>
</table>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="body-content" style="padding:32px 36px;">

<div class="alert-box alert-red" style="padding:14px 20px;border-radius:10px;margin:0 0 18px 0;font-size:13.5px;line-height:1.6;background:#fef2f2;border:1px solid #fecaca;color:#991b1b;">
<strong style="font-size:15px;">&#9888; Critical Alert</strong><br>
Our monitoring platform has detected that <strong>{website.name}</strong> is currently unavailable. The website failed to respond within the expected timeframe.
</div>

<div class="section-head" style="font-size:14px;font-weight:700;color:#1e1e2f;margin:28px 0 14px 0;padding-bottom:8px;border-bottom:2px solid #eef1f6;letter-spacing:-0.2px;">&#128203; Incident Summary</div>

<table class="data-table" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:0 0 4px 0;border-radius:10px;overflow:hidden;">
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Website Name</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{website.name}</td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Website URL</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;"><a href="{website.url}" style="color:#dc3545;text-decoration:none;font-weight:600;">{website.url}</a></td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Current Status</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;"><span class="badge badge-red" style="display:inline-block;padding:5px 16px;border-radius:20px;font-size:12px;font-weight:700;letter-spacing:0.4px;text-transform:uppercase;background:#fce8e8;color:#b91c1c;">&#128308; DOWN</span></td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Response Time</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{rtime} ms</td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">HTTP Status Code</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{scode}</td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Server Status</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;"><span style="color:#dc3545;font-weight:700;">&#10060; Unreachable</span></td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Date &amp; Time</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{now}</td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Monitoring Region</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">Primary (Auto)</td></tr>
</table>

<div class="section-head" style="font-size:14px;font-weight:700;color:#1e1e2f;margin:28px 0 14px 0;padding-bottom:8px;border-bottom:2px solid #eef1f6;letter-spacing:-0.2px;">&#128220; Recommended Actions</div>
<div class="action-item" style="padding:7px 0;font-size:13.5px;color:#374151;line-height:1.6;"><span class="action-check" style="color:#198754;font-weight:700;margin-right:8px;">&#10003;</span> Check server health and resource usage</div>
<div class="action-item" style="padding:7px 0;font-size:13.5px;color:#374151;line-height:1.6;"><span class="action-check" style="color:#198754;font-weight:700;margin-right:8px;">&#10003;</span> Verify DNS resolution and propagation</div>
<div class="action-item" style="padding:7px 0;font-size:13.5px;color:#374151;line-height:1.6;"><span class="action-check" style="color:#198754;font-weight:700;margin-right:8px;">&#10003;</span> Review web server and application error logs</div>
<div class="action-item" style="padding:7px 0;font-size:13.5px;color:#374151;line-height:1.6;"><span class="action-check" style="color:#198754;font-weight:700;margin-right:8px;">&#10003;</span> Validate SSL certificate expiration date</div>
<div class="action-item" style="padding:7px 0;font-size:13.5px;color:#374151;line-height:1.6;"><span class="action-check" style="color:#198754;font-weight:700;margin-right:8px;">&#10003;</span> Confirm hosting provider has no active outage</div>

<div class="btn-row" style="text-align:center;padding:22px 0 6px 0;">
<a href="#" class="btn btn-red" style="display:inline-block;padding:13px 32px;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;text-align:center;letter-spacing:0.2px;border:none;background:#dc3545;color:#ffffff;">&#128269; View Dashboard</a>
<a href="#" class="btn btn-sec" style="display:inline-block;padding:13px 32px;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;text-align:center;letter-spacing:0.2px;border:none;background:#ffffff;color:#374151;border:2px solid #dce0e8;margin-left:8px;">&#128196; Open Incident</a>
</div>

</td></tr>
</table>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="footer-row" style="background:#f8fafd;padding:24px 36px;text-align:center;border-top:1px solid #eef1f6;">
<div class="footer-name" style="font-size:16px;font-weight:700;color:#1e1e2f;letter-spacing:-0.3px;"><span style="color:#0d6efd;">&#9679;</span> Website Monitoring System</div>
<div class="footer-tag" style="font-size:12px;color:#9ca3af;margin:4px 0 16px 0;">Automated Infrastructure Monitoring Platform</div>
<div class="footer-links" style="font-size:12px;color:#9ca3af;line-height:1.8;">
This alert was automatically generated by Website Monitoring System.<br>
You will receive another notification once the service is restored.<br><br>
<strong>Need assistance?</strong> <a href="mailto:support@example.com" style="color:#0d6efd;text-decoration:none;">support@example.com</a>
</div>
<div class="footer-copy" style="font-size:11px;color:#b8bfcc;margin-top:12px;">&copy; 2026 Website Monitoring System. All rights reserved.</div>
</td></tr>
</table>

</td></tr>
</table>

</td></tr>
</table>
</body>
</html>"""


def website_up_email(website, result, prev_status="DOWN", downtime_duration=None):
    now = timezone.now().strftime("%d %b %Y, %I:%M:%S %p")
    rtime = result.get('response_time', 'N/A')
    downtime_html = ""
    if downtime_duration:
        downtime_html = f"""<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Downtime Duration</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{downtime_duration}</td></tr>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>{CSS}</style>
</head>
<body>
<table class="email-wrapper" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:700px;margin:0 auto;padding:32px 20px;background:#f4f6fa;">
<tr><td align="center">

<table class="email-card" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,0.07),0 2px 8px rgba(0,0,0,0.04);max-width:700px;">
<tr><td>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="logo-row" style="padding:24px 36px 0 36px;text-align:center;">
<span class="logo-text" style="font-size:18px;font-weight:800;color:#1e1e2f;letter-spacing:-0.4px;"><span class="logo-dot" style="color:#0d6efd;font-size:22px;">&#9679;</span> WEBSITE MONITORING SYSTEM</span>
</td></tr>
</table>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="banner-green" style="background:linear-gradient(135deg,#198754 0%,#116a3e 100%);padding:28px 36px;text-align:center;">
<div class="banner-icon" style="font-size:42px;line-height:1;">&#9989;</div>
<h1 class="banner-title" style="color:#ffffff;font-size:24px;font-weight:700;margin:10px 0 4px 0;letter-spacing:-0.4px;">Website Restored Successfully</h1>
<p class="banner-sub" style="color:rgba(255,255,255,0.88);font-size:14px;margin:0;line-height:1.5;">Your website is back online and responding to requests normally</p>
</td></tr>
</table>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="body-content" style="padding:32px 36px;">

<div class="alert-box alert-green" style="padding:14px 20px;border-radius:10px;margin:0 0 18px 0;font-size:13.5px;line-height:1.6;background:#f0fdf4;border:1px solid #bbf7d0;color:#166534;">
<strong style="font-size:15px;">&#128994; Service Restored</strong><br>
Our monitoring platform has confirmed that <strong>{website.name}</strong> is responding normally again. No further action is required.
</div>

<div class="section-head" style="font-size:14px;font-weight:700;color:#1e1e2f;margin:28px 0 14px 0;padding-bottom:8px;border-bottom:2px solid #eef1f6;letter-spacing:-0.2px;">&#128203; Recovery Summary</div>

<table class="data-table" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:0 0 4px 0;border-radius:10px;overflow:hidden;">
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Website Name</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{website.name}</td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Website URL</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;"><a href="{website.url}" style="color:#198754;text-decoration:none;font-weight:600;">{website.url}</a></td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Previous Status</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;"><span style="color:#dc3545;font-weight:600;">{prev_status}</span></td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Current Status</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;"><span class="badge badge-green" style="display:inline-block;padding:5px 16px;border-radius:20px;font-size:12px;font-weight:700;letter-spacing:0.4px;text-transform:uppercase;background:#e3f5eb;color:#0c6b3e;">&#128994; OPERATIONAL</span></td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Response Time</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{rtime} ms</td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Recovery Time</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{now}</td></tr>
{downtime_html}
</table>

<div style="text-align:center;padding:18px 0 4px 0;">
<table align="center" role="presentation" cellpadding="0" cellspacing="0" style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;">
<tr><td style="padding:14px 28px;font-size:15px;font-weight:600;color:#166534;">
&#9989; Downtime Resolved &mdash; No further action required
</td></tr>
</table>
</div>

<div class="btn-row" style="text-align:center;padding:22px 0 6px 0;">
<a href="#" class="btn btn-green" style="display:inline-block;padding:13px 32px;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;text-align:center;letter-spacing:0.2px;border:none;background:#198754;color:#ffffff;">&#128202; View Dashboard</a>
<a href="#" class="btn btn-sec" style="display:inline-block;padding:13px 32px;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;text-align:center;letter-spacing:0.2px;border:none;background:#ffffff;color:#374151;border:2px solid #dce0e8;margin-left:8px;">&#128196; View Logs</a>
</div>

</td></tr>
</table>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="footer-row" style="background:#f8fafd;padding:24px 36px;text-align:center;border-top:1px solid #eef1f6;">
<div class="footer-name" style="font-size:16px;font-weight:700;color:#1e1e2f;letter-spacing:-0.3px;"><span style="color:#0d6efd;">&#9679;</span> Website Monitoring System</div>
<div class="footer-tag" style="font-size:12px;color:#9ca3af;margin:4px 0 16px 0;">Automated Infrastructure Monitoring Platform</div>
<div class="footer-links" style="font-size:12px;color:#9ca3af;line-height:1.8;">
This notification was sent by Website Monitoring System.<br>
Monitoring timestamp: {now}<br><br>
<strong>Need assistance?</strong> <a href="mailto:support@example.com" style="color:#0d6efd;text-decoration:none;">support@example.com</a>
</div>
<div class="footer-copy" style="font-size:11px;color:#b8bfcc;margin-top:12px;">&copy; 2026 Website Monitoring System. All rights reserved.</div>
</td></tr>
</table>

</td></tr>
</table>

</td></tr>
</table>
</body>
</html>"""


def website_slow_email(website, result, threshold):
    now = timezone.now().strftime("%d %b %Y, %I:%M:%S %p")
    rtime = result.get('response_time', 'N/A')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>{CSS}</style>
</head>
<body>
<table class="email-wrapper" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:700px;margin:0 auto;padding:32px 20px;background:#f4f6fa;">
<tr><td align="center">

<table class="email-card" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,0.07),0 2px 8px rgba(0,0,0,0.04);max-width:700px;">
<tr><td>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="logo-row" style="padding:24px 36px 0 36px;text-align:center;">
<span class="logo-text" style="font-size:18px;font-weight:800;color:#1e1e2f;letter-spacing:-0.4px;"><span class="logo-dot" style="color:#0d6efd;font-size:22px;">&#9679;</span> WEBSITE MONITORING SYSTEM</span>
</td></tr>
</table>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="banner-orange" style="background:linear-gradient(135deg,#fd7e14 0%,#cc5f0a 100%);padding:28px 36px;text-align:center;">
<div class="banner-icon" style="font-size:42px;line-height:1;">&#9888;</div>
<h1 class="banner-title" style="color:#ffffff;font-size:24px;font-weight:700;margin:10px 0 4px 0;letter-spacing:-0.4px;">High Response Time Detected</h1>
<p class="banner-sub" style="color:rgba(255,255,255,0.88);font-size:14px;margin:0;line-height:1.5;">The website is reachable but response time has exceeded the configured threshold</p>
</td></tr>
</table>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="body-content" style="padding:32px 36px;">

<div class="alert-box alert-orange" style="padding:14px 20px;border-radius:10px;margin:0 0 18px 0;font-size:13.5px;line-height:1.6;background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;">
<strong style="font-size:15px;">&#9888; Performance Alert</strong><br>
<strong>{website.name}</strong> is responding slowly. Current response time <strong>{rtime} ms</strong> exceeds the threshold of <strong>{threshold} ms</strong>.
</div>

<div class="section-head" style="font-size:14px;font-weight:700;color:#1e1e2f;margin:28px 0 14px 0;padding-bottom:8px;border-bottom:2px solid #eef1f6;letter-spacing:-0.2px;">&#128202; Performance Details</div>

<table class="data-table" role="presentation" width="100%" cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:0 0 4px 0;border-radius:10px;overflow:hidden;">
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Website Name</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{website.name}</td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Website URL</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;"><a href="{website.url}" style="color:#fd7e14;text-decoration:none;font-weight:600;">{website.url}</a></td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Current Response Time</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;"><strong style="color:#fd7e14;font-size:16px;">{rtime} ms</strong></td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Configured Threshold</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{threshold} ms</td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Status</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;"><span class="badge badge-orange" style="display:inline-block;padding:5px 16px;border-radius:20px;font-size:12px;font-weight:700;letter-spacing:0.4px;text-transform:uppercase;background:#fff1e0;color:#bd5b00;">&#128992; DEGRADED</span></td></tr>
<tr><td class="lbl" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#6b7280;font-weight:600;width:44%;background:#fafbfd;">Monitoring Time</td><td class="val" style="padding:11px 16px;font-size:13.5px;border-bottom:1px solid #eef1f6;color:#1e1e2f;font-weight:500;width:56%;">{now}</td></tr>
</table>

<div class="section-head" style="font-size:14px;font-weight:700;color:#1e1e2f;margin:28px 0 14px 0;padding-bottom:8px;border-bottom:2px solid #eef1f6;letter-spacing:-0.2px;">&#128295; Performance Recommendations</div>
<div class="action-item" style="padding:7px 0;font-size:13.5px;color:#374151;line-height:1.6;"><span class="action-check" style="color:#198754;font-weight:700;margin-right:8px;">&#10003;</span> Review server CPU and memory utilization</div>
<div class="action-item" style="padding:7px 0;font-size:13.5px;color:#374151;line-height:1.6;"><span class="action-check" style="color:#198754;font-weight:700;margin-right:8px;">&#10003;</span> Optimize database queries and connection pooling</div>
<div class="action-item" style="padding:7px 0;font-size:13.5px;color:#374151;line-height:1.6;"><span class="action-check" style="color:#198754;font-weight:700;margin-right:8px;">&#10003;</span> Check for application-level bottlenecks in error logs</div>
<div class="action-item" style="padding:7px 0;font-size:13.5px;color:#374151;line-height:1.6;"><span class="action-check" style="color:#198754;font-weight:700;margin-right:8px;">&#10003;</span> Monitor network latency and CDN performance</div>

<div class="btn-row" style="text-align:center;padding:22px 0 6px 0;">
<a href="#" class="btn btn-orange" style="display:inline-block;padding:13px 32px;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;text-align:center;letter-spacing:0.2px;border:none;background:#fd7e14;color:#ffffff;">&#128202; View Dashboard</a>
<a href="#" class="btn btn-sec" style="display:inline-block;padding:13px 32px;border-radius:8px;font-size:14px;font-weight:600;text-decoration:none;text-align:center;letter-spacing:0.2px;border:none;background:#ffffff;color:#374151;border:2px solid #dce0e8;margin-left:8px;">&#128196; View Logs</a>
</div>

</td></tr>
</table>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0">
<tr><td class="footer-row" style="background:#f8fafd;padding:24px 36px;text-align:center;border-top:1px solid #eef1f6;">
<div class="footer-name" style="font-size:16px;font-weight:700;color:#1e1e2f;letter-spacing:-0.3px;"><span style="color:#0d6efd;">&#9679;</span> Website Monitoring System</div>
<div class="footer-tag" style="font-size:12px;color:#9ca3af;margin:4px 0 16px 0;">Automated Infrastructure Monitoring Platform</div>
<div class="footer-links" style="font-size:12px;color:#9ca3af;line-height:1.8;">
This notification was sent by Website Monitoring System.<br>
Monitoring timestamp: {now}<br><br>
<strong>Need assistance?</strong> <a href="mailto:support@example.com" style="color:#0d6efd;text-decoration:none;">support@example.com</a>
</div>
<div class="footer-copy" style="font-size:11px;color:#b8bfcc;margin-top:12px;">&copy; 2026 Website Monitoring System. All rights reserved.</div>
</td></tr>
</table>

</td></tr>
</table>

</td></tr>
</table>
</body>
</html>"""
