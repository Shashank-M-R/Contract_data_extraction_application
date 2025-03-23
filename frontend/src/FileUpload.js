import React, { useState } from "react";
import axios from "axios";

function FileUpload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [extractedData, setExtractedData] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
        const response = await axios.post(
            "http://127.0.0.1:8000/extract_contract/",
            formData,
            { headers: { "Content-Type": "multipart/form-data" } }
          );

      setExtractedData(JSON.parse(response.data));
    } catch (error) {
      console.error("Error extracting data:", error);
      alert("Failed to extract contract details.");
    }
  };

  return (
    <div>
      <input type="file" accept="application/pdf" onChange={handleFileChange} />
      <button onClick={handleUpload}>Extract</button>

      {extractedData && (
        <div>
          <h3>Extracted Contract Details</h3>
          <table border="1" cellPadding="5" style={{ borderCollapse: "collapse", width: "50%" }}>
            <tbody>
              {Object.entries(extractedData).map(([key, value]) => (
                <tr key={key}>
                  <td><strong>{key}</strong></td>
                  <td>{value}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default FileUpload;
