import network

# Function to connect to an existing WiFi network
def connect_to_wifi(ssid, password):
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect(ssid, password)

    while not sta.isconnected():
        pass
    print("Connected to WiFi:", sta.ifconfig())

# Main code execution
if __name__ == "__main__":
    # Define credentials for existing WiFi network
    existing_wifi_ssid = "Your-wifi-SSID"
    existing_wifi_password = "You-wifi-passwd"

    # Connect ESP32 to the existing WiFi network
    connect_to_wifi(existing_wifi_ssid, existing_wifi_password)