document.getElementByIda("upload").onclick = async () => {
  const file =  document.getElementById("pdf").files[0];
  if(!file) return;

  const formData = new FormData();
  formData.append("pdf",file)

  const res = await fetch("/uploads",{
    method:"POST",
    body: formData
  });

  const data =await res.json();
  document.getElementById("output").textContent = data.text;
};