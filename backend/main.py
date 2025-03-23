from fastapi import FastAPI, UploadFile, File
import pdfplumber
import re
import json
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (update with frontend URL if needed)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_contract_details(pdf_path):
    contract_data = {}
    
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    
    patterns = {
        "Contract ID": r"Contract ID:\s*(.*)",
        "Beneficiary Name": r"Beneficiary Name:\s*(.*)",
        "Address": r"Address:\s*(.*)",
        "Contact Number": r"Contact Number:\s*(.*)",
        "Contract Value": r"Contract Value:\s*(.*)",
        "Contract Start Date": r"Contract Start Date:\s*(.*)",
        "Contract End Date": r"Contract End Date:\s*(.*)",
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        contract_data[key] = match.group(1).strip() if match else "Not Found"
    
    return contract_data

@app.post("/extract_contract/")
async def extract_contract(file: UploadFile = File(...)):
    temp_file = f"temp_{file.filename}"
    
    with open(temp_file, "wb") as buffer:
        buffer.write(await file.read())

    extracted_data = extract_contract_details(temp_file)
    
    return json.dumps(extracted_data, indent=4)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
