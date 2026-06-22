const API_URL = "http://localhost:8000"

document.getElementById("form-post-tree")
    .addEventListener("submit", (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);

        send_form(formData);
    });

async function send_form(formData) {
    const formValues = Object.fromEntries(formData);

    const payload = {
        "temperature": formValues.temperature,
        "humidity": formValues.humidity,
        "is_raining": formValues.is_raining == "on",
    }
    try {
        response = await fetch(`${API_URL}/tree`, {
            method: 'POST',
            body: JSON.stringify(payload),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log(await response.json());
    } catch (error) {
        console.log(error);
    }
}
