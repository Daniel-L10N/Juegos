// Función para generar un número aleatorio dentro de un rango
function generarNumeroAleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Función para realizar el juego de sumas
function juegoDeSumas() {
    let numeroDeSumas = parseInt(prompt("¿Cuántas sumas seguidas quieres realizar?"));
    
    while (isNaN(numeroDeSumas) || numeroDeSumas <= 0) {
        numeroDeSumas = parseInt(prompt("Por favor, ingresa un número válido de sumas:"));
    }

    let rangoMin = parseInt(prompt("Ingresa el número mínimo del rango:"));
    while (isNaN(rangoMin)) {
        rangoMin = parseInt(prompt("Por favor, ingresa un número válido para el mínimo del rango:"));
    }

    let rangoMax = parseInt(prompt("Ingresa el número máximo del rango:"));
    while (isNaN(rangoMax) || rangoMax < rangoMin) {
        rangoMax = parseInt(prompt("Por favor, ingresa un número válido (mayor que el mínimo) para el máximo del rango:"));
    }

    let aciertos = 0;

    // Bucle que se ejecuta tantas veces como el número de sumas definidas por el usuario
    for (let i = 1; i <= numeroDeSumas; i++) {
        let numero1 = generarNumeroAleatorio(rangoMin, rangoMax);
        let numero2 = generarNumeroAleatorio(rangoMin, rangoMax);
        let sumaCorrecta = numero1 + numero2;

        // Pedir al usuario que ingrese el resultado de la suma
        let respuestaUsuario = parseInt(prompt(`Suma estos números: ${numero1} + ${numero2} = ?`));

        // Verificar si el resultado del usuario es correcto
        if (respuestaUsuario === sumaCorrecta) {
            alert("¡Correcto!");
            aciertos++;
        } else {
            alert(`Incorrecto. La respuesta correcta es: ${sumaCorrecta}`);
        }
    }

    // Calcular y mostrar el porcentaje de aciertos
    let porcentajeAciertos = (aciertos / numeroDeSumas) * 100;
    alert(`Has terminado el juego. Tu porcentaje de aciertos es: ${porcentajeAciertos.toFixed(2)}%`);
}

// Iniciar el juego
juegoDeSumas();
