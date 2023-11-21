document.getElementById('id_esp').addEventListener('change', function() {
    // Obtener el valor seleccionado de la especialidad
    var selectedEspecialidad = this.value;

    // Obtener el campo de selección de médico
    var selectMedico = document.getElementById('rut_med');

    // Limpiar las opciones existentes
    selectMedico.innerHTML = '';

    // Obtener la lista de médicos asociados a la especialidad seleccionada
    obtenerMedicosPorEspecialidad(selectedEspecialidad);  // Corregir el nombre del argumento aquí
});

function obtenerMedicosPorEspecialidad(especialidadId) {
    var url = 'obtener_medicos_por_especialidad/' + especialidadId + '/';
     return fetch(url)
    .then(response => response.json())
        .then(data => {
            // Procesar los datos recibidos y actualizar el campo de selección de médico
            var selectMedico = document.getElementById('rut_med');
            data.medicos.forEach(function(medico) {
                var option = document.createElement('option');
                option.value = medico.rut_med;
                option.text = medico.pnombre_med + ' ' + medico.apaterno_med;
                selectMedico.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error al obtener médicos:', error);
        });
}

//Horarios disponibles de medicos
document.getElementById('rut_med').addEventListener('change', function() {
    var selectedMedico = this.value;
    var url2 = 'obtener_fechas_disponibles/' + selectedMedico + '/';
    // Realizar una solicitud con fetch para obtener las fechas disponibles del médico seleccionado
    fetch(url2)
        .then(response => response.json())
        .then(data => {
            var selectFecha = document.getElementById('fecha_ate');
            // Limpiar las opciones existentes
            selectFecha.innerHTML = '';

            // Agregar las nuevas opciones al campo de selección de fechas
            data.fechas.forEach(function(fecha) {
                var option = document.createElement('option');
                option.value = fecha;
                option.text = fecha;
                selectFecha.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error al obtener fechas disponibles:', error);
        });
});