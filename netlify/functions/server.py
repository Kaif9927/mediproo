"""
Netlify serverless function for Flask app
This function handles all Flask routes through Netlify Functions
"""
import sys
import os

# Add parent directories to path
base_dir = os.path.join(os.path.dirname(__file__), '../..')
sys.path.insert(0, os.path.abspath(base_dir))

# Set environment variable for Netlify
os.environ['NETLIFY'] = 'true'

# Import the Flask app
from app import app, create_tables

# Initialize database on first import (in serverless, this happens per invocation)
# Note: SQLite in /tmp won't persist between invocations
try:
    with app.app_context():
        create_tables()
except Exception as e:
    print(f"Database initialization note: {e}")

def handler(event, context):
    """
    Netlify serverless function handler
    Uses serverless-wsgi to adapt Flask to Netlify Functions
    """
    try:
        from serverless_wsgi import handle_request
        return handle_request(app, event, context)
    except ImportError as e:
        # Fallback if serverless-wsgi is not available
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/plain'},
            'body': f'serverless-wsgi package is required. Error: {str(e)}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/plain'},
            'body': f'Server error: {str(e)}'
        }

