"""
Blog List Page Route Handler
"""
from datetime import datetime

def get_context(context):
    context['title'] = "Blog"
    context['posts'] = [
        {"slug": "post-1", "title": "First Post", "date": "2024-01-15", "author": "Alice"},
        {"slug": "post-2", "title": "Second Post", "date": "2024-01-20", "author": "Bob"},
        {"slug": "post-3", "title": "Third Post", "date": "2024-01-25", "author": "Charlie"},
    ]
    return context
