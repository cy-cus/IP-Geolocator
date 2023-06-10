import requests
import argparse
import sys

def geolocate_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"

    try:
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            city = data.get("city")
            region = data.get("regionName")
            country = data.get("country")
            zip_code = data.get("zip")
            latitude = data.get("lat")
            longitude = data.get("lon")
            isp = data.get("isp")
            org = data.get("org")
            as_name = data.get("as")

            maps_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

            print("\nGeolocation Details:")
            print(f"IP Address: {ip_address}")
            print(f"City: {city}")
            print(f"Region: {region}")
            print(f"Country: {country}")
            print(f"ZIP Code: {zip_code}")
            print(f"Latitude: {latitude} (view on Google Maps: {maps_url})")
            print(f"Longitude: {longitude} (view on Google Maps: {maps_url})")
            print(f"ISP: {isp}")
            print(f"Organization: {org}")
            print(f"AS Name: {as_name}")

        else:
            print("Failed to retrieve geolocation data.")
            print(f"Error message: {data.get('message')}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(prog="locateip.py", description="IP Geolocation Tool")
    parser.add_argument("ip_address", help="IP address to geolocate")
    args = parser.parse_args()

    geolocate_ip(args.ip_address)

if __name__ == "__main__":
    main()
