var seleccionado = document.getElementById("id_esp");
var precioInput = document.getElementById("precio_ate");
var bono_ate = document.getElementById("bono_ate");
var monto_boleta = document.getElementById("monto_boleta")
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
            monto_boleta.value = data.precio;
        })
})



