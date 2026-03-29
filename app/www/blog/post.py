"""
Blog Post Route Handler (Dynamic)
"""
from datetime import datetime

def get_context(context):
    context['title'] = "Blog Post"
    
    posts = {
        "post-1": {
            "title": "First Post",
            "content": "This is the content of the first blog post. It can contain **markdown** or HTML.",
            "author": "Alice",
            "date": "2024-01-15",
        },
        "post-2": {
            "title": "Second Post",
            "content": "Content of the second post. You can add images, code blocks, and more!",
            "author": "Bob",
            "date": "2024-01-20",
        },
        "post-3": {
            "title": "Third Post",
            "content": "Third post content. Each post can have unique styling and layout.",
            "author": "Charlie",
            "date": "2024-01-25",
        },
    }
    
    post_slug = context.get("post_slug", "post-1")
    context['post'] = posts.get(post_slug)
    
    if not context['post']:
        context['error'] = "Post not found"
    
    return context
