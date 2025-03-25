import frappe
from minio import Minio

def test_s3_connection():
    doc_name = 'DFP.ES.moo-coding-dev.250220.01'
    doc = frappe.get_doc('DFP External Storage', doc_name)

    print("Configuration:")
    print(f"Type: {doc.type}")
    print(f"Endpoint: {doc.endpoint}")
    print(f"Region: {doc.region}")
    print(f"Bucket: {doc.bucket_name}")
    print(f"Enabled: {doc.enabled}")

    # Try to initialize client manually
    try:
        client = Minio(
            doc.endpoint.replace('https://', ''),
            access_key=doc.access_key,
            secret_key=doc.get_password('secret_key'),
            secure=True,
            region=doc.region
        )
        print("\nManual client initialization successful!")
        
        # Test listing objects
        objects = client.list_objects(doc.bucket_name)
        for obj in objects:
            print(f"Found object: {obj.object_name}")
    except Exception as e:
        print(f"\nError initializing client: {e}")
