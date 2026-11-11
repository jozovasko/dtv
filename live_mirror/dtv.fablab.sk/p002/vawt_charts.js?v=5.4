function initCharts() {
    var ctxTel = document.getElementById('canvas-telemetry').getContext('2d');
    chartTelemetry = new Chart(ctxTel, {
        type: 'line',
        data: {
            labels: timeHistory,
            datasets: [
                { label: 'RPM', borderColor: '#e74c3c', data: rpmHistory, yAxisID: 'y', tension: 0.2, pointRadius: 0 },
                { label: 'Moment (Nm)', borderColor: '#27ae60', data: torqueHistory, yAxisID: 'y1', tension: 0.2, pointRadius: 0 },
                { label: 'Vietor (m/s)', borderColor: '#3498db', data: windHistory, yAxisID: 'y2', tension: 0.2, pointRadius: 0, borderDash: [5, 5] },
                { label: 'Výkon (W)', borderColor: '#f39c12', data: wattsHistory, yAxisID: 'y3', tension: 0.2, pointRadius: 0 }
            ]
        },
        options: {
            responsive: true, maintainAspectRatio: false, animation: false,
            interaction: { mode: 'index', intersect: false },
            scales: {
                x: { display: false }, 
                y: { type: 'linear', display: true, position: 'left', title: { display: true, text: 'RPM' } },
                y1: { type: 'linear', display: true, position: 'right', title: { display: true, text: 'Moment (Nm)' }, grid: { drawOnChartArea: false } },
                y2: { type: 'linear', display: true, position: 'right', title: { display: true, text: 'Vietor (m/s)' }, grid: { drawOnChartArea: false }, min: 0, max: 40 },
                y3: { type: 'linear', display: true, position: 'right', title: { display: true, text: 'Výkon (W)' }, grid: { drawOnChartArea: false } }
            },
            plugins: { legend: { position: 'top' } }
        }
    });

    var ctxPar = document.getElementById('canvas-params').getContext('2d');
    chartParams = new Chart(ctxPar, {
        type: 'radar',
        data: {
            labels: ['Polomer', 'Výška', 'Páka', 'Hmota', 'Tlmič'],
            datasets: [{
                label: 'Aktuálna štruktúra',
                data: [0, 0, 0, 0, 0],
                backgroundColor: 'rgba(52, 152, 219, 0.2)', borderColor: '#2980b9', pointBackgroundColor: '#2c3e50'
            }]
        },
        options: {
            responsive: true, maintainAspectRatio: false,
            scales: { r: { min: 0, max: 100, ticks: { display: false } } },
            plugins: { legend: { display: false } }
        }
    });
}

function updateCharts(rpm, torque, wind, watts, rad, h, lev, mass, damp) {
    chartUpdateCounter++;
    if (chartUpdateCounter % 15 !== 0) return;

    var timeStamp = new Date().toLocaleTimeString();
    timeHistory.push(timeStamp);
    rpmHistory.push(rpm);
    torqueHistory.push(torque);
    windHistory.push(wind);
    wattsHistory.push(watts);

    if (timeHistory.length > 50) {
        timeHistory.shift(); rpmHistory.shift(); torqueHistory.shift(); windHistory.shift(); wattsHistory.shift();
    }
    if(chartTelemetry) chartTelemetry.update();

    if(chartParams) {
        chartParams.data.datasets[0].data = [
            ((rad - 0.8) / 1.7) * 100, ((h - 1.0) / 2.0) * 100, 
            ((lev - 0.1) / 0.3) * 100, ((mass - 1) / 14) * 100, ((damp - 1) / 9) * 100
        ];
        chartParams.update();
    }
}