"""
Serverless adapter for Flask app on Netlify
This file adapts the Flask app to work with Netlify Functions
"""
import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(__file__))

from app import app

def handler(event, context):
    """
    Netlify serverless function handler
    """
    from serverless_wsgi import handle_request
    return handle_request(app, event, context)

