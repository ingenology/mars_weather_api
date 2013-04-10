from django.conf import settings

def constants(request):
    """
    Adds selected constants to the context.
    """
    return {
        'PROJECT_NAME': getattr(settings, 'PROJECT_NAME', ''),
        'PROJECT_AUTHOR': getattr(settings, 'PROJECT_AUTHOR', ''),
    }

