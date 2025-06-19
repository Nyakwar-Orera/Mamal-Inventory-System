from flask import current_app
from flask_mail import Message
from app import mail
from app.models import Stationery
from datetime import datetime

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def check_low_stock(app):
    with app.app_context():
        low_stock_items = Stationery.query.filter(
            Stationery.quantity < Stationery.threshold
        ).all()
        
        if low_stock_items:
            subject = "Low Stock Alert"
            sender = current_app.config['ADMINS'][0]
            recipients = [current_app.config['ADMINS'][0]]  # Add more recipients as needed
            
            text_body = "The following items are low on stock:\n\n"
            html_body = "<h2>Low Stock Alert</h2><ul>"
            
            for item in low_stock_items:
                text_body += f"{item.item_type}: {item.quantity} {item.unit} remaining (Threshold: {item.threshold})\n"
                html_body += f"<li>{item.item_type}: {item.quantity} {item.unit} remaining (Threshold: {item.threshold})</li>"
            
            html_body += "</ul>"
            
            send_email(subject, sender, recipients, text_body, html_body)

def generate_qr_code(asset_id, asset_name, serial_number):
    import qrcode
    from io import BytesIO
    import base64
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    data = f"Asset ID: {asset_id}\nName: {asset_name}\nSerial: {serial_number}"
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return f"data:image/png;base64,{img_str}"