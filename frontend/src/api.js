import axios from "axios";

export const extractContract = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return await axios.post("http://127.0.0.1:8000/extract_contract/", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};
