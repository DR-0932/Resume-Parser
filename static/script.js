const form = document.getElementById("uploadForm");
const fileInput = document.getElementById("fileInput");
const output = document.getElementById("output");
const downloadBtn = document.getElementById("downloadBtn");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  if (!fileInput.files.length) {
    alert("Please select a PDF file");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  output.textContent = "Uploading and parsing resume...";
  downloadBtn.disabled = true;

  try {
    const response = await fetch("/upload", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    output.textContent = JSON.stringify(data, null, 2);

    downloadBtn.disabled = false;
  } catch (error) {
    output.textContent = "Error: " + error.message;
  }
});

downloadBtn.addEventListener("click", () => {
  window.location.href = "/download";
});
