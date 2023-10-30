function actualizarHoras() {
    const fechaInput = document.getElementById('fecha_ate');
    const horaSelect = document.getElementById('hora_ate');

    horaSelect.innerHTML = ''; // Limpia las opciones existentes


    if (fechaInput.value) {
        const fechaSeleccionada = new Date(fechaInput.value);
        const horaInicial = 8; // Hora de inicio (por ejemplo, 8:00 AM)
        const horaFinal = 18; // Hora de finalización (por ejemplo, 6:00 PM)

        for (let hora = horaInicial; hora <= horaFinal; hora++) {
            const horaTexto = hora < 10 ? `0${hora}:00` : `${hora}:00`;
            const option = document.createElement('option');
            option.value = horaTexto;
            option.textContent = horaTexto;
            horaSelect.appendChild(option);
        }
    }
}