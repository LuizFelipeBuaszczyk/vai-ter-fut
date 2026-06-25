const API_URL = "http://localhost:8000";

document
  .getElementById("form-post-tree")
  .addEventListener("submit", (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    send_form(formData);
  });

async function send_form(formData) {
  const formValues = Object.fromEntries(formData);

  const submitBtn = document.getElementById("submit-btn");
  const resultSection = document.getElementById("result-section");
  const resultDisplay = document.getElementById("result-display");

  submitBtn.disabled = true;
  submitBtn.innerText = "Enviando...";
  resultSection.style.display = "none";

  const payload = {
    temperature: Number(formValues.temperature),
    humidity: Number(formValues.humidity),
    is_raining: formValues.is_raining == "on",
  };

  try {
    const response = await fetch(`${API_URL}/tree`, {
      method: "POST",
      body: JSON.stringify(payload),
      headers: {
        "Content-Type": "application/json",
      },
    });

    const data = await response.json();

    if (data.can_play) {
      resultDisplay.innerText = "Vai ter fut!";
      resultDisplay.className = "result-success";
    } else {
      resultDisplay.innerText = "Sem fut :(";
      resultDisplay.className = "result-error";
    }

    resultSection.style.display = "block";
  } catch (error) {
    console.log(error);
    resultDisplay.innerText = "Erro ao buscar resposta da API.";
    resultDisplay.className = "result-error";
    resultSection.style.display = "block";
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerText = "Enviar";
  }
}
