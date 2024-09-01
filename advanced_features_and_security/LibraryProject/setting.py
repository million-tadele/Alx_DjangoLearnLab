Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # settings.py
... AUTH_USER_MODEL = 'your_app_name.CustomUser'
DEBUG = False
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS protection in supported browsers
X_FRAME_OPTIONS = 'DENY'  # Prevent clickjacking by not allowing your site to be embedded in frames
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing

CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are sent over HTTPS only
SESSION_COOKIE_SECURE = True  # Ensure session cookies are sent over HTTPS only

SECURE_HSTS_SECONDS = 3600  # Enable HTTP Strict Transport Security for 1 hour
SECURE_SSL_REDIRECT = True  # Redirect all non-HTTPS requests to HTTPS


INSTALLED_APPS = [
    ...
    'csp',
]

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", 'https://trustedscripts.example.com')
CSP_STYLE_SRC = ("'self'", 'https://trustedstyles.example.com')

from django.utils.deprecation import MiddlewareMixin

class ContentSecurityPolicyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self';"
        return response
MIDDLEWARE = [
    ...
    'your_app.middleware.ContentSecurityPolicyMiddleware',
]

# Enforce XSS protection in browsers
SECURE_BROWSER_XSS_FILTER = True

# Prevent the application from being embedded in an iframe
X_FRAME_OPTIONS = 'DENY'

# Prevent MIME type sniffing by browsers
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER", "X_FRAME_OPTIONS", "SECURE_CONTENT_TYPE_NOSNIFF", "CSRF_COOKIE_SECURE", "SESSION_COOKIE_SECURE"


"SECURE_PROXY_SSL_HEADER", "HTTP_X_FORWARDED_PROTO"
