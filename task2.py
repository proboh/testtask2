import subprocess
import uuid
import datetime
import socket

# Function to generate CoT message
def generate_cot_message(lat, lon, target_description):
    event_uid = str(uuid.uuid4())  # Unique identifier for each event
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # CoT XML structure
    cot_message = f"""
    <event version="2.0" uid="{event_uid}" type="a-f-G-U-C" time="{timestamp}" start="{timestamp}" stale="2024-11-26T12:10:00Z">
        <point lat="{lat}" lon="{lon}" />
        <detail>
            <type>{target_description}</type>
        </detail>
    </event>
    """
    return cot_message

# Function to send message using Signal-CLI
def send_signal_message(phone_number, cot_message):
    try:
        subprocess.run(['./bin/signal-cli', '-u', '+380123456789', 'send', '-m', cot_message, phone_number], check=True)
        print(f"Message sent to {phone_number}")
    except subprocess.CalledProcessError as e:
        print(f"Error sending message: {e}")

# Function to send CoT message
def send_cot_message(cot_message, atak_ip, port=8443):
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(cot_message.encode('utf-8'), (atak_ip, port))
        print(f"Sent CoT message to {atak_ip}:{port}")

# Example usage
lat = 48.567123
lon = 39.87897
target_description = "tank"
cot_message = generate_cot_message(lat, lon, target_description)

# Replace with the recipient's phone number
recipient_phone_number = "+380123456789"
atak_ip = ""

send_signal_message(recipient_phone_number, cot_message)
send_cot_message(cot_message, atak_ip)
