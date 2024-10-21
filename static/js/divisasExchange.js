document.addEventListener('DOMContentLoaded', function() {
    // Solicitud automática para obtener las tasas de divisas cuando se carga la página
    fetch('/actualizar/currency-conversion/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('conversion-results');
        if (data.success) {
            resultDiv.innerHTML = `
                <ul>
                    <li><strong>USD:</strong> ${data.result.USD}</li>
                    <li><strong>EUR:</strong> ${data.result.EUR}</li>
                    <li><strong>GBP:</strong> ${data.result.GBP}</li>
                    <li><strong>JPY:</strong> ${data.result.JPY}</li>
                    <li><strong>CLP:</strong> ${data.result.CLP}</li>
                </ul>
            `;
        } else {
            resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
        }
    })
    .catch(error => console.error('Error:', error));
});
