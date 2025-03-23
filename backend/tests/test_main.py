import pytest
from fastapi.testclient import TestClient
from backend.main import app  # Import your FastAPI app

client = TestClient(app)

# def test_root():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Contract Data Extraction API"}


def test_upload_valid_contract():
    files = {"file": ("sample_contract.pdf", open("sample_contract.pdf", "rb"), "application/pdf")}
    response = client.post("/extract_contract/", files=files)
    assert response.status_code == 200
    json_response = response.json()
    assert "Contract ID" in json_response  # Example key validation


def test_upload_invalid_file():
    files = {"file": ("invalid.txt", b"This is not a PDF", "text/plain")}
    response = client.post("/extract_contract/", files=files)
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid file format. Only PDFs are allowed."}
