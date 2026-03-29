"""
App Installation Script (Frappe-style)
"""
from setuptools import setup, find_packages

setup(
    name="my_fastapi_app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "jinja2>=3.1.2",
        "python-multipart>=0.0.6",
    ],
)
