document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('ingresosEgresosChart').getContext('2d');
    
    const ingresos = JSON.parse(document.getElementById('ingresos-data').textContent);
    const egresos = JSON.parse(document.getElementById('egresos-data').textContent);

    const ingresosEgresosChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Ingresos', 'Egresos'],
            datasets: [{
                label: 'Transacciones',
                data: [ingresos, egresos],
                backgroundColor: ['#4CAF50', '#FF6347']
            }]
        }
    });
});