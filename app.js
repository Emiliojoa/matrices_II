const prompt = require("prompt-sync")();

const personas = [];
let iteracion = true;

while (iteracion) {
    const peticion = prompt(`Por favor ingrese qué tipo de acción quiere realizar:
        1. Ingresar nueva persona
        2. Mostrar todos los datos
        3. Filtrar por DNI
        4. Salir del programa
    : `);

    if (peticion === "1") {
        const nombre = prompt("Ingrese el nombre de la persona: ");
        const apellido = prompt("Ingrese el apellido de la persona: ");
        const dni = prompt("Ingrese el DNI de la persona: ");
        const telefonos = []
        let iteracion2 = true

        while (iteracion2) {
            const telefono = prompt("Ingrese los teléfonos de la persona: ")
            telefonos.push(telefono)
            const continuar = prompt("Desea ingresar otro teléfono? (s/n): ")
            if (continuar === "n") {
                iteracion2 = false
            }
        } 

        const hijos = prompt("Ingrese los hijos de la persona separados por coma: ").split(",");

        personas.push([nombre, apellido, dni, telefonos, hijos]);
        console.log(personas)
    
    } else if (peticion === "2") {
        console.log("Lista de personas:");
        console.log(personas)

    } else if (peticion === "3") {
        const dniBuscado = prompt("Ingrese el DNI de la persona que desea buscar:");
        const personaEncontrada = personas.find(persona => persona[2] === dniBuscado);

        if (personaEncontrada) {
            console.log("Persona encontrada: ",personaEncontrada);
        } else {
            console.log("No se encontró ninguna persona con ese DNI.");
        }

    } else if (peticion === "4") {
        iteracion = false;
        console.log("Saliendo del programa...");
    
    } else {
        console.log("Opción no válida.");
    }
}

console.log(personas)
