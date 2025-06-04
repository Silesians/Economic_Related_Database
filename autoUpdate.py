import requests

def download_file(url, local_filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {local_filename}")
    else:
        print(f"Failed to download {local_filename}")

def main():
    holder_data_url = "https://www.federalreserve.gov/paymentsystems/account-and-access-disclosure/holder-data.csv"
    requestor_data_url = "https://www.federalreserve.gov/paymentsystems/account-and-access-disclosure/requestor-data.csv"

    download_file(holder_data_url, "holder-data.csv")
    download_file(requestor_data_url, "requestor-data.csv")

if __name__ == "__main__":
    main()
