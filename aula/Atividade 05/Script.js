document.getElementById("characterForm").addEventListener("submit", function(event) {
event.preventDefault(); // Evita que o formulário seja enviado

// Obtenção dos valores dos campos
var name = document.getElementById("name").value;
var age = document.getElementById("age").value;
var profession = document.getElementById("profession").value;
var hobbies = document.getElementById("hobbies").value;
var favoriteFood = document.getElementById("favoriteFood").value;

// Construção da string com as informações do personagem
var characterInfo = "Nome: " + name + "<br>" +
"Idade: " + age + "<br>" +

"Profissão: " + profession + "<br>" +
"O que gosta de fazer: " + hobbies + "<br>" +
"Comida Preferida: " + favoriteFood;

// Exibir as informações do personagem
document.getElementById("characterInfo").innerHTML = characterInfo;

// Limpar o formulário
document.getElementById("characterForm").reset();
});