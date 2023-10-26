import requests
import json

class LIMSClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password

    def _make_request(self, endpoint, method="GET", data=None):
        """Internal method to make API requests."""
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/json"}

        try:
            if method == "GET":
                response = requests.get(url, headers=headers, auth=(self.username, self.password))
            elif method == "POST":
                response = requests.post(url, headers=headers, auth=(self.username, self.password), json=data)
            # Add more methods as needed

            response.raise_for_status()
            if response.content:
                return response.json()
            return None

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            print(f"HTTP Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")
            return None


    def get_samples(self, criteria=None):
        """Fetch samples based on given criteria."""
        endpoint = "mobile/browses/sample"
        if criteria:
            endpoint += f"?criteria={criteria}"
        return self._make_request(endpoint)

    def add_sample(self, sample_data):
        """Add a new sample."""
        endpoint = "mobile/add/sample"
        return self._make_request(endpoint, method="POST", data=sample_data)

    # Add more methods as needed, such as update_sample, delete_sample, etc.

if __name__ == "__main__":
    # Initialize the LIMS client
    lims = LIMSClient(base_url="http://localhost:56105", username="system", password=" ")

    # Example usage
    dna_test_criteria = "ENTITY_TYPE_NAME=='DNA_TEST' AND (STATUS=='Completed' OR STATUS=='Authorized' OR STATUS=='In Progress')"
    dna_samples = lims.get_samples(criteria=dna_test_criteria)

    if dna_samples:
        print(json.dumps(dna_samples, indent=2))
    else:
        print("Failed to fetch DNA test data.")
