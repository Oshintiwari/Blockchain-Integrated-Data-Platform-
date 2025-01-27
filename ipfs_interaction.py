import requests

IPFS_API = "http://127.0.0.1:5001/api/v0"

def upload_to_ipfs(file_path):
    with open(file_path, 'rb') as file:
        response = requests.post(f"{IPFS_API}/add", files={"file": file})
        if response.status_code == 200:
            hash_value = response.json()["Hash"]
            print(f"File uploaded to IPFS with hash: {hash_value}")
            return hash_value
        else:
            raise Exception("Failed to upload to IPFS.")

def retrieve_from_ipfs(hash_value):
    response = requests.get(f"{IPFS_API}/cat?arg={hash_value}")
    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Failed to retrieve data from IPFS.")
