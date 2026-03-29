"""
Privacy Policy Page Logic
"""
from datetime import datetime

def get_context(context):
    """
    Returns context data for policy.html template
    """
    context['title'] = "Privacy"
    context['last_updated'] = datetime.now().strftime("%B %d, %Y")
    context['contact_email'] = "privacy@myapp.com"
    context['contact_phone'] = "+1 (555) 123-4567"
    context['company_address'] = "123 Main Street, City, State 12345"
    context['year'] = datetime.now().year
    return context