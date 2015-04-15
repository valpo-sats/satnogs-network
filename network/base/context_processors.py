from django.conf import settings
from django.template.loader import render_to_string


def analytics(request):
    """Returns analytics code."""
    if settings.ENVIRONMENT == 'production':
        return {'analytics_code': render_to_string('includes/analytics.html',
                {'google_analytics_key': settings.GOOGLE_ANALYTICS_KEY,
                 'user': request.user})}
    else:
        return {'analytics_code': ''}
