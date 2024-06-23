import network

# Function to set up ESP32 as an Access Point
def setup_access_point(ap_ssid, ap_password):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ap_ssid, authmode=network.AUTH_WPA2_PSK, password=ap_password)
    print("Access Point SSID:", ap_ssid)
    print("Access Point Password:", ap_password)
    print("Access Point IP Address:", ap.ifconfig()[0])

# Main code execution
if __name__ == "__main__":

    # Define credentials for the Access Point (ESP32 AP)
    esp_ap_ssid = "ESP32-AP"
    esp_ap_password = "your_password"

    # Set up ESP32 as an Access Point
    setup_access_point(esp_ap_ssid, esp_ap_password)