"""
Controller for handling main application routes
"""
from flask import Blueprint, render_template

# Create Blueprint for main routes
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """
    Handler for the home page
    
    Returns:
        str: Rendered HTML template of the home page
    """
    return render_template('index.html') 