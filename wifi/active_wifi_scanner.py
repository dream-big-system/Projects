import time
import pywifi
from pywifi import const

def scan_and_connect(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    # Scan for available WiFi networks
    iface.scan()
    time.sleep(1)

    # Get scan results
    scan_results = iface.scan_results()

    # Find the target network
    target_network = None
    for network in scan_results:
        if network.ssid == ssid:
            target_network = network
            break
    
    if target_network is None:
        print(f"Target network {ssid} not found.")
        return False

    # Connect to the target network
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)

    # Wait for connection status
    while iface.status() != const.IFACE_CONNECTED:
        time.sleep(1)

    print("Connected to the target network.")
    return True

if __name__ == "__main__":
    ssid = input("Enter the SSID of the network you want to connect to: ")
    password = input("Enter the password for the network: ")
    scan_and_connect(ssid, password)
