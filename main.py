import subprocess
import requests
import json

# Replace '<YOUR WEBHOOK HERE>' with your Discord Webhook
webhook_url = '<YOUR WEBHOOK HERE>'

# Replace the '<ENTER YOUR SCRIPT HERE>' with your desired script
multiline_script = '''
print("hello")
'''

def send_discord_message(webhook_url, message):
    data = {
        'content': message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print('Successfully sent output to your Discord Webhook!')
    else:
        print(f'Failed to send output. Status code: {response.status_code}')

# Saving the script to a temporary file
script_file = 'temp_script.py'
with open(script_file, 'w') as file:
    file.write(multiline_script)

# Executing the script and capturing the output
try:
    result = subprocess.run(['python', script_file], capture_output=True, text=True)
    output = result.stdout.strip() + '\n' + result.stderr.strip()
except Exception as e:
    output = str(e)

# Send the output to the Discord Webhook you provided
send_discord_message(webhook_url, output)

# Remove the temporary script file
import os
os.remove(script_file)