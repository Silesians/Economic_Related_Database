import requests
import logging

def setup_logging():
    logging.basicConfig(
        filename='data_update.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def download_file(url, local_filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (4xx, 5xx)
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        logging.info(f"Downloaded: {local_filename}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download {local_filename}: {e}")

def main():
    setup_logging()

    holder_data_url = "https://www.federalreserve.gov/paymentsystems/account-and-access-disclosure/holder-data.csv"
    requestor_data_url = "https://www.federalreserve.gov/paymentsystems/account-and-access-disclosure/requestor-data.csv"

    download_file(holder_data_url, "holder-data.csv")
    download_file(requestor_data_url, "requestor-data.csv")

if __name__ == "__main__":
    main()
