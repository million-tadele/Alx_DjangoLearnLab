Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # settings.py
... AUTH_USER_MODEL = 'your_app_name.CustomUser'


from django.conf import settings

# Example usage in a foreign key
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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
