"""
Contact Page Route Handler
"""
from datetime import datetime

def get_context(context):
    context['title'] = "Contact Us"
    return context

def on_form_submit(form_data):
    """Called when contact form is submitted"""
    name = form_data.get('name')
    email = form_data.get('email')
    message = form_data.get('message')
    print(f"📩 Contact form submitted: {name} ({email})")
    return {
        "success": True,
        "message": f"Thank you {name}! We received your message."
    }
