function toggleSession() {
    const isLoggedIn = document.body.classList.toggle('logged-in');
    alert(isLoggedIn ? 'Sesión iniciada' : 'Sesión cerrada');
    // Aquí puedes agregar más lógica para manejar el estado de la sesión.
}
