function showDoc(sectionId) {
    // 1. Ocultar todas las secciones de doc
    const sections = document.querySelectorAll('.doc-section');
    sections.forEach(sec => sec.style.display = 'none');

    // 2. Mostrar la seleccionada
    // (Aquí podrías expandir con un switch o cargando datos dinámicos)
    document.getElementById(sectionId).style.display = 'block';

    // 3. Cambiar estado activo de los botones
    const buttons = document.querySelectorAll('.doc-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    event.currentTarget.classList.add('active');
}