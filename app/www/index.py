"""
Homepage Route Handler (Frappe-style)
"""
from datetime import datetime

def get_context(context):
    """Returns context data for index.html template"""
    context['title'] = "Home"
    context['current_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    context['featured_items'] = [
        {"name": "Product A", "price": 99.99},
        {"name": "Product B", "price": 149.99},
        {"name": "Product C", "price": 199.99},
    ]
    context['visitor_count'] = 1234
    context['show_banner'] = True
    return context
