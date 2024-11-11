# Automated GCP Data Pipeline

This project sets up an automated data pipeline in Google Cloud Platform (GCP) that allows users to upload CSV files to a Google Cloud Storage (GCS) bucket, and automatically loads the data from the uploaded files into a BigQuery table. The system uses Flask for a web interface and Google Cloud services like Cloud Storage and BigQuery to handle file storage and data processing.

## Features

- **File Upload Interface**: A user-friendly web interface to upload files to Google Cloud Storage via a simple drag-and-drop or file browsing mechanism.
- **Google Cloud Storage Integration**: Files uploaded through the web interface are stored in a GCS bucket.
- **BigQuery Integration**: Automatically loads the uploaded files into a BigQuery table upon upload to the GCS bucket.
- **Progress Bar**: The web interface features a progress bar that simulates the file upload process.

## Code Explanation

**`index.html`**
- A simple HTML page with CSS styling for a clean and responsive interface.
- Allows users to drag-and-drop or browse files for uploading.
- Displays a progress bar during the file upload process.

**`app.py`**
- A Flask application with a single route (/) for handling file uploads.
- The uploaded file is stored in a pre-configured GCS bucket.
- The server uses Flask's render_template to serve the index.html file for the frontend.

**`gcs_to_bq.py`**
- Google Cloud Function that is triggered by new file uploads in the GCS bucket.
- It loads the file data into a BigQuery table using the BigQuery API.
- The script reads the CSV file from the GCS bucket and loads it into a specified dataset and table in BigQuery.

## Prerequisites

- Python 3.x
- Flask
- Google Cloud SDK
- Google Cloud Storage Bucket
- BigQuery Dataset and Table



## License
This project is licensed under the MIT License - see the LICENSE file for details. 
