var titulo = document.querySelector(".titulo");
titulo.textContent = "Nutri Matheus";

var pacientes = document.querySelectorAll(".paciente");

for (var i = 0; i < pacientes.length; i++){

    var paciente = pacientes[i];

    var pdPeso = paciente.querySelector(".info-peso");
    var Peso = pdPeso.textContent;

    var pdAltura = paciente.querySelector(".info-altura");
    var Altura = pdAltura.textContent;

    var AlturaValida = true;
    var PesoValido = true;
    var pdImc = paciente.querySelector(".info-imc");

    if (Peso <=0 || Peso >= 1000){
        console.log("Peso inválido.");
        PesoValido = false;
        pdImc.textContent = "PESO INVÁLIDO!";
        paciente.style.backgroundColor = "Lightcoral";
    }
    if (Altura <=0 || Altura >=3){
        console.log("Altura inválida.")
        AlturaValida = false;
        pdImc.textContent = "ALTURA INVÁLIDA!";
        paciente.style.backgroundColor = "Lightcoral";
    }
    if (AlturaValida && PesoValido){
        var imc = Peso / (Altura * Altura);
        pdImc.textContent = imc.toFixed(2);
    }

}
