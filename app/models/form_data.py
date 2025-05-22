"""
Contact form data model
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class ContactFormData:
    """
    Class for storing contact form data
    """
    name: str
    phone: str
    description: str
    pickup_address: str
    delivery_address: str
    pickup_date: str
    pickup_time: str
    loader: bool
    email: Optional[str] = None
    notes: Optional[str] = None
    
    def to_dict(self) -> dict:
        """
        Convert form data to dictionary for storage or sending
        
        Returns:
            dict: Dictionary with form data
        """
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'description': self.description,
            'pickup_address': self.pickup_address,
            'delivery_address': self.delivery_address,
            'pickup_date': self.pickup_date,
            'pickup_time': self.pickup_time,
            'loader': self.loader,
            'notes': self.notes
        } 