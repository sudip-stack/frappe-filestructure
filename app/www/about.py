"""
About Page Route Handler
"""
from datetime import datetime

def get_context(context):
    context['title'] = "About Us"
    context['team'] = [
        {"name": "Alice", "role": "CEO"},
        {"name": "Bob", "role": "CTO"},
        {"name": "Charlie", "role": "Designer"},
    ]
    return context
