from flask import Flask, request, render_template, redirect, url_for
from google.cloud import storage
import functions_framework  # type: ignore
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
import time

# Triggered by a change in a storage bucket
@functions_framework.cloud_event
def handle_gcs_event(cloud_event):
    data = cloud_event.data

    event_id = cloud_event["id"]
    event_type = cloud_event["type"]

    bucket = data["bucket"]
    filename = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print(f"Event ID: {event_id}")
    print(f"Event type: {event_type}")
    print(f"Bucket: {bucket}")
    print(f"File: {filename}")
    print(f"Metageneration: {metageneration}")
    print(f"Created: {timeCreated}")
    print(f"Updated: {updated}")

    # Load data into BigQuery
    load_data_to_bq(filename)

# dataset and table names
dataset_name = 'new_sales_data'
table_name = 'new_orders'

def load_data_to_bq(filename):
    """Load the uploaded file into the BigQuery table."""
    client = bigquery.Client()

    # Get the BigQuery table reference
    table_ref = client.dataset(dataset_name).table(table_name)

    # Configure the load job
    job_config = LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1  # Skip header row in CSV
    job_config.autodetect = True  # Let BigQuery infer the schema

    # Construct the URI for the uploaded file in Cloud Storage
    uri = f'gs://e-commerce_data_bucket/{filename}'

    # Load the CSV file into BigQuery
    load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)

    # Wait for the load job to complete
    load_job.result()

    # Log the number of rows loaded
    num_rows = load_job.output_rows
    print(f"{num_rows} rows loaded into {dataset_name}.{table_name}.")

    # Add a delay to avoid overwhelming the system
    time.sleep(10)
