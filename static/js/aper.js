document.addEventListener('DOMContentLoaded', () => {
    // Función para mostrar una vista previa de la foto de perfil
    const fotoInput = document.querySelector('input[name="foto_perfil"]');
    const fotoPreview = document.createElement('img');
    fotoPreview.style.maxWidth = '200px';
    fotoPreview.style.marginTop = '1rem';
    fotoPreview.style.display = 'none';  // Inicialmente oculto
    document.querySelector('.form-group').appendChild(fotoPreview);

    if (fotoInput) {
        fotoInput.addEventListener('change', () => {
            const file = fotoInput.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = () => {
                    fotoPreview.src = reader.result;
                    fotoPreview.style.display = 'block';  // Mostrar vista previa
                };
                reader.readAsDataURL(file);
            } else {
                fotoPreview.style.display = 'none';  // Ocultar vista previa si no hay archivo
            }
        });
    }
});

//mensajes estilo de animacion



