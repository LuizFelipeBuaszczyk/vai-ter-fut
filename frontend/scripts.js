

document.getElementById("form-post-tree")
    .addEventListener("submit", (event) => {
        event.preventDefault();
        const formData = new FormData(event.target);

        send_form(formData);
    });

function send_form(formData) {

    const formValues = Object.fromEntries(formData);
    
}