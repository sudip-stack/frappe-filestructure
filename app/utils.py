"""
Utility functions available in templates
"""
from datetime import datetime
import re

def format_date(date_str=None, format="%Y-%m-%d"):
    if date_str:
        return datetime.strptime(date_str, format).strftime("%B %d, %Y")
    return datetime.now().strftime("%B %d, %Y")

def format_currency(amount, currency="$"):
    return f"{currency}{amount:,.2f}"

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text
