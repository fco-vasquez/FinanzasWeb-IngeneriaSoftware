document.addEventListener('DOMContentLoaded', function () {
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
                // Renderizar las tasas de cambio en el DOM
                resultDiv.innerHTML = `
                    <ul>
                        <li><strong>USD:</strong> ${data.result.USD}</li>
                        <li><strong>EUR:</strong> ${data.result.EUR}</li>
                        <li><strong>GBP:</strong> ${data.result.GBP}</li>
                        <li><strong>JPY:</strong> ${data.result.JPY}</li>
                        <li><strong>AUD:</strong> ${data.result.AUD}</li>
                        <li><strong>CAD:</strong> ${data.result.CAD}</li>
                        <li><strong>CNY:</strong> ${data.result.CNY}</li>
                        <li><strong>BRL:</strong> ${data.result.BRL}</li>
                        <li><strong>MXN:</strong> ${data.result.MXN}</li>
                        <li><strong>KRW:</strong> ${data.result.KRW}</li>
                        <li id="CLPTrans"><strong>CLP:</strong> ${data.result.CLP}</li>
                    </ul>
                `;

                // Obtener los valores desde los elementos renderizados
                const ingresosText = document.getElementById("ingresostransf")?.innerText || '0';
                const egresosText = document.getElementById("egresostransf")?.innerText || '0';
                const divisaCLP = document.getElementById("CLPTrans")?.innerText || '1'; // Evitar división por 0

                // Función para convertir el texto a número
                const parseCLP = (text) => parseFloat(text.replace(/[^\d.-]/g, '') || '0');

                // Convertir los textos a números
                const totalIngresos = parseCLP(ingresosText);
                const totalEgresos = parseCLP(egresosText);
                const totalCLPDIV = parseCLP(divisaCLP);

                // Hacer un cálculo (por ejemplo, balance)
                const balance = totalIngresos - totalEgresos;
                const USDBalance = balance / totalCLPDIV;

                // Actualizar el contenido de los spans dinámicamente
                document.getElementById("egresos-span2").innerText = `$${balance.toLocaleString()} CLP`;
                document.getElementById("egresos-span3").innerText = `$${USDBalance.toLocaleString()} USD`;
            } else {
                resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            }
        })
        .catch(error => console.error('Error:', error));
});
