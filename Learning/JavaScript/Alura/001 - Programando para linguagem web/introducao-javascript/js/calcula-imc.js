var titulo = document.querySelector(".titulo");
titulo.textContent = "Nutri Matheus";

var pacientes = document.querySelectorAll(".paciente");

for (var i = 0; i < pacientes.length; i++){

    var paciente = pacientes[i];

    var pdPeso = paciente.querySelector(".info-peso");
    var peso = pdPeso.textContent;

    var pdAltura = paciente.querySelector(".info-altura");
    var altura = pdAltura.textContent;

    var AlturaValida = validaAltura(altura);
    var PesoValido = validaPeso(peso);
    var pdImc = paciente.querySelector(".info-imc");

    if (!PesoValido){
        console.log("Peso inválido.");
        PesoValido = false;
        pdImc.textContent = "PESO INVÁLIDO!";
        paciente.classList.add("paciente-invalido")
    }
    if (!AlturaValida){
        console.log("Altura inválida.")
        AlturaValida = false;
        pdImc.textContent = "ALTURA INVÁLIDA!";
        paciente.classList.add("paciente-invalido")
    }
    if (AlturaValida && PesoValido){
        var imc = calculaImc(peso,altura);
        pdImc.textContent = imc;
    }

}
function validaPeso(peso){
    if (peso >= 0 && peso <= 500){
        return true;
    }else{
        return false;
    }
}
function validaAltura(altura){
    if (altura > 0 && altura <3){
        return true;
    }else{
        return false;
    }
}

function calculaImc(peso,altura){
    var imc = 0;
    imc = peso / (altura * altura);
    return imc.toFixed(2);
}