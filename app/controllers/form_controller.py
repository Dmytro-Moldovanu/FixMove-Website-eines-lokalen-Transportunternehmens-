"""
Controller for processing submitted forms
"""
from flask import Blueprint, request, current_app, redirect, url_for, flash, render_template, jsonify
from app.models.form_data import ContactFormData

# Create Blueprint for form processing
form_bp = Blueprint('form', __name__)

@form_bp.route('/submit', methods=['POST'])
def submit():
    """
    Form submission handler
    
    Returns:
        str: Success message
    """
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')  # Get email (can be empty)
        description = request.form.get('description')
        pickup_address = request.form.get('pickup_address')
        delivery_address = request.form.get('delivery_address')
        pickup_date = request.form.get('pickup_date')
        pickup_time = request.form.get('pickup_time')
        loader = bool(request.form.get('loader'))
        notes = request.form.get('notes')
        
        # Create form data object
        form_data = ContactFormData(
            name=name,
            phone=phone,
            email=email,
            description=description,
            pickup_address=pickup_address,
            delivery_address=delivery_address,
            pickup_date=pickup_date,
            pickup_time=pickup_time,
            loader=loader,
            notes=notes
        )
        
        # Log data for debugging
        print(f"Received data from {form_data.name} ({form_data.phone})")
        if form_data.email:
            print(f"Contact email: {form_data.email}")
        print(f"Transport from {form_data.pickup_address} to {form_data.delivery_address}")
        print(f"Date and time: {form_data.pickup_date} {form_data.pickup_time}")
        
        # Email is now sent via JavaScript, so we only save the data here
        # Here you can add database storage if needed
        
        return "Anfrage erfolgreich verarbeitet!" 