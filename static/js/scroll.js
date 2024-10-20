document.getElementById("deslizar-aservicio").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("services").scrollIntoView({
        behavior: "smooth",  // Desplazamiento suave
        block: "start"       // Alinea al inicio de la sección
    });
});

document.getElementById("deslizar-acontacto").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("contact").scrollIntoView({
        behavior: "smooth",  // Desplazamiento suave
        block: "start"       // Alinea al inicio de la sección
    });
});

document.getElementById("deslizar-ainformacion").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("information").scrollIntoView({
        behavior: "smooth",  // Desplazamiento suave
        block: "start"       // Alinea al inicio de la sección
    });
});
