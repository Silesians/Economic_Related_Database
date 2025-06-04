import requests
import os

def download_file(url, local_filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {local_filename}")
    else:
        print("Failed to download file")

def main():
    url = "https://www.federalreserve.gov/paymentsystems/account-and-access-disclosure/holder-data.csv"
    local_filename = "holder-data.csv"  # Update with the correct filename if needed
    download_file(url, local_filename)

if __name__ == "__main__":
    main()
