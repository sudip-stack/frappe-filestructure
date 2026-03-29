"""
App Configuration & Hooks (Frappe-style)
"""

app_name = "my_fastapi_app"
app_title = "My FastAPI App"
app_publisher = "Your Name"
app_version = "1.0.0"

website_route_rules = [
    {"from_route": "/blog/<post>", "to_route": "blog/post"},
]

global_context = {
    "app_name": "My FastAPI App",
    "brand_html": '<span class="brand">My App</span>',
}

jinja = {
    "methods": [
        "app.utils.format_date",
        "app.utils.format_currency",
    ],
    "filters": [
        "app.utils.slugify",
    ],
}
