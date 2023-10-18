var seleccionado = document.getElementById("esp_select");
var precioInput = document.getElementById("precio_ate");
console.log(precioInput);

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



