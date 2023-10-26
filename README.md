LIMSClient Python Module Documentation 📄
Table of Contents 📑
Introduction
Features and Methods 💡
Installation and Usage 🛠️
Understanding the Design 🧠
Contribution & Issues 🤝
1. Introduction 🎉
The LIMSClient Python module provides an efficient and Pythonic interface to interact with the LIMS (Laboratory Information Management System) API. By abstracting the API's endpoints into intuitive Python methods, developers can effortlessly fetch, add, update, or delete samples in the LIMS system.

2. Features and Methods 💡
Initialization: Configure the client using your LIMS API's base URL and authentication details. 🔒
Fetching samples: Retrieve samples based on certain criteria. 🔎
Adding new samples: Easily add new samples into the system. ➕
Extensibility: The design allows for easy addition of more methods, such as updating or deleting samples. ⚙️
3. Installation and Usage 🛠️
Installation:
Ensure you have the requests library installed:

Copy code
pip install requests
Usage:

python
Copy code
from LIMSClient import LIMSClient

# Initialize the LIMS client
lims = LIMSClient(base_url="http://your-lims-api-url", username="your_username", password="your_password")

# Fetch samples
criteria = "ENTITY_TYPE_NAME=='DNA_TEST' AND (STATUS=='Completed' OR STATUS=='Authorized' OR STATUS=='In Progress')"
samples = lims.get_samples(criteria=criteria)

# Print samples
print(samples)
4. Understanding the Design 🧠
Why this design?

Simplicity: The module abstracts away the complexity of the underlying LIMS API, making it easy for Python developers to interact with the system without having to dive deep into the API's specifics. 🎯

Modularity: The design is modular, allowing for easy addition of methods and endpoints as the LIMS system evolves. 🔧

Error Handling: The module gracefully handles common HTTP errors and provides clear feedback, enabling seamless troubleshooting. ❌

How does it work?

HTTP Requests: The module leverages the requests library to make HTTP requests to the LIMS API. Depending on the method called, it will make a GET or POST request. 🌐

Authentication: Basic Authentication is used to authenticate API requests. 🔑

Data Retrieval & Posting: Depending on the method used, the module can retrieve data based on specific criteria or send data to the LIMS API to add new samples. 💼

5. Contribution & Issues 🤝
Contributions to enhance the module are welcome! Please ensure to test your changes thoroughly. 👩‍💻👨‍💻

For any issues or suggestions, please open a new issue with a detailed description, and we'll address it promptly. 🚀
