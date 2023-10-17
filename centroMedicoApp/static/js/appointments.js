var seleccionado = document.getElementById("esp_select");
var precioInput = document.getElementById("precio_ate");
/*
seleccionado.addEventListener('change', function(){
    especialidad = seleccionado.value;
    console.log(especialidad);
    var url = 'get_precio/' + especialidad + '/';
    console.log(url);
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // Asigna el precio al input
            precioInput.value = data.precio;
        })
})
*/
seleccionado.addEventListener('change', function() {
    especialidad = seleccionado.value;
    console.log(especialidad);

    if (precioInput) {
        precioInput.value = especialidad;  // O establece el valor que desees aquí
    } else {
        console.error('Elemento con ID "precio_ate" no encontrado.');
    }
});



