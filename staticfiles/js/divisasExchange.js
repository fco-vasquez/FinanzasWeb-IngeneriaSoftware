document.getElementById('currency-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Evita que se recargue la página

    const form = event.target;
    const formData = new FormData(form);  // Captura los datos del formulario
    const csrfToken = formData.get('csrfmiddlewaretoken');

    fetch('/actualizar/currency-conversion/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'X-Requested-With': 'XMLHttpRequest'  // Indica que es una solicitud AJAX
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('conversion-results');
        if (data.success) {
            resultDiv.innerHTML = `
                <ul>
                    <li>USD: ${data.result.USD}</li>
                    <li>EUR: ${data.result.EUR}</li>
                    <li>GBP: ${data.result.GBP}</li>
                    <li>JPY: ${data.result.JPY}</li>
                </ul>
            `;
        } else {
            resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
        }
    })
    .catch(error => console.error('Error:', error));
});
