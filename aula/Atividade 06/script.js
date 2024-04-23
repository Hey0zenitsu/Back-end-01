function mostrarSegundaTela() {
    var mainContainer = document.getElementById('main-container');
    var segundaTela = document.getElementById('segunda-tela');

    mainContainer.style.display = 'none';
    segundaTela.style.display = 'block';
}

function voltarParaPrimeiraTela() {
    var mainContainer = document.getElementById('main-container');
    var segundaTela = document.getElementById('segunda-tela');

    mainContainer.style.display = 'block';
    segundaTela.style.display = 'none';
}