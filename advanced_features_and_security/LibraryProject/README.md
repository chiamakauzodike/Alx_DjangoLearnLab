# Permissions and Groups in Django 
## Custom Permissions 
The `Post` model includes the following custom permissions: 
- `can_view`: Allows viewing posts. 
- `can_create`: Allows creating posts. 
- `can_edit`: Allows editing posts. 
- `can_delete`: Allows deleting posts. 

## Groups 
The application defines the following groups: 
- `Viewers`: Assigned `can_view` permission. 
- `Editors`: Assigned `can_view`, `can_create`, and `can_edit` permissions. 
- `Admins`: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`). 

## How to Test 
1. Create test users and assign them to groups using the admin interface. 
2. Log in as these users and verify their access: 
- Viewers can only view posts. 
- Editors can view, create, and edit posts. 
- Admins can perform all actions, including deleting posts.

# Securing the Application with HTTPS
## Overview
The application is configured to enforce HTTPS and implement secure headers and cookies to ensure secure communication between the client and the server.
### Django Settings
- **SECURE_SSL_REDIRECT**: Redirects all HTTP requests to HTTPS.
- **SECURE_HSTS_SECONDS**: Enforces HTTP Strict Transport Security (HSTS) for one year.
- **SECURE_HSTS_INCLUDE_SUBDOMAINS**: Ensures HSTS applies to all subdomains.
- **SECURE_HSTS_PRELOAD**: Allows the site to be preloaded into browsers for HSTS.
- **SESSION_COOKIE_SECURE** and **CSRF_COOKIE_SECURE**: Ensure cookies are only sent over HTTPS.
- **X_FRAME_OPTIONS**: Prevents clickjacking attacks by disallowing framing of the site. - **SECURE_CONTENT_TYPE_NOSNIFF**: Disables MIME-sniffing for enhanced security.
- **SECURE_BROWSER_XSS_FILTER**: Enables browser-level XSS filtering.

### Web Server Configuration
- **SSL/TLS Certificates**: SSL certificates are required to enable HTTPS. Use services like Let’s Encrypt for free certificates.
- **Nginx/Apache**: Configured to support HTTPS and redirect HTTP to HTTPS.

### Testing and Verification 
- Verify HTTPS using browser developer tools.
- Run security checks using tools like:
    - [SSL Labs SSL Test](https://www.ssllabs.com/ssltest/)
    - [Mozilla Observatory](https://observatory.mozilla.org/)