import subprocess
import re

def get_ipv4_address():
    try:
        # Run ipconfig command
        ipconfig_result = subprocess.run(['ipconfig'], capture_output=True, text=True)
        ipconfig_output = ipconfig_result.stdout
        
        # Use regular expression to find IPv4 address
        ipv4_pattern = r'IPv4 Address[.\s]*:\s*([\d.]+)'
        match = re.search(ipv4_pattern, ipconfig_output, re.IGNORECASE)
        
        if match:
            ipv4_address = match.group(1)
            return ipv4_address
        else:
            return None

    except Exception as e:
        print("An error occurred:", e)
        return None

# Call the function to get the IPv4 address
ipv4_address = get_ipv4_address()

if ipv4_address:
    print("IPv4 Address:", ipv4_address)
else:
    print("IPv4 Address not found.")
