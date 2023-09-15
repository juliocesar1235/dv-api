import pandas as pd
import requests
import time

# Define the API endpoint
api_endpoint = 'http://159.65.232.163:8000//api/zipcode/'

# Load the Excel file and specify the sheet name or index (index starts from 0)
excel_file = 'FILE_NAME.xlsx'  
sheet_name = 1

# Read the Excel file into a DataFrame, skipping the first row
df = pd.read_excel(excel_file, sheet_name=sheet_name)

def send_post_request_with_retry(data, max_retries=3):
    for retry in range(max_retries):
        try:
            response = requests.post(api_endpoint, json=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error on attempt {retry + 1}: {e}")
            time.sleep(5)

    print(f"Failed to send data after {max_retries} retries.")
    return None

for index, row in df.iterrows():
    if row.isna().all():
        break

    data = row.to_dict()
    for key, value in data.items():
        if pd.isna(value):
            data[key] = None
    print("data", data)

    response = send_post_request_with_retry(data)

    if response is not None:
        if response.status_code == 200 or response.status_code == 201:
            print(f"Row {index + 2} sent successfully.")
        else:
            print(f"Row {index + 2} failed to send. Status code: {response.status_code}")

print("Data sending completed.")
