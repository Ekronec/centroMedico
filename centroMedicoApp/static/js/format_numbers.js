document.addEventListener('DOMContentLoaded', function() {
    const rutElement = document.getElementById('formatted-rut');
    if (rutElement) {
        const rutValue = rutElement.innerText;
        const formattedRut = rutValue.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
        rutElement.innerText = formattedRut;
    }
});