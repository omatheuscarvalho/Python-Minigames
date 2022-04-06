var botaoAdicionar = document.querySelector("#adicionar-paciente");
botaoAdicionar.addEventListener("click", function(event) {
    event.preventDefault();

    var form = document.querySelector("#form-adiciona");
    // extraindo informações do paciente do form    
    var paciente = obtemPacienteDoFormulario(form);

    // cria tr e td
    var pacienteTr = montaTr(paciente);

    // adiciona paciente na tabela
    if(validaPaciente(paciente)){
        var tabela = document.querySelector("#tabela-pacientes")
        tabela.appendChild(pacienteTr)
        form.reset();
    }else{
        alert("Paciente inválido!")
    }
    
    
});

function obtemPacienteDoFormulario(form){
    var paciente = {
        nome: form.nome.value,
        peso: form.peso.value,
        altura: form.altura.value,
        gordura: form.gordura.value,
        imc: calculaImc(form.peso.value, form.altura.value)
    }
    return paciente;
}
function montaTr(paciente){
    var pacienteTr = document.createElement("tr");
    pacienteTr.classList.add("paciente");

    pacienteTr.appendChild(montaTd(paciente.nome, "info-nome"));
    pacienteTr.appendChild(montaTd(paciente.peso, "info-peso"));
    pacienteTr.appendChild(montaTd(paciente.altura, "info-altura"));
    pacienteTr.appendChild(montaTd(paciente.gordura, "info-gordura"));
    pacienteTr.appendChild(montaTd(paciente.imc, "info-imc"));

    return pacienteTr;
}
function montaTd(dado,classe){
    var td = document.createElement("td")
    td.textContent = dado;
    td.classList.add(classe);
    return td;
}
function validaPaciente(paciente){
    if(validaAltura(paciente.altura) && validaPeso(paciente.peso)){
        return true;
    }else{
        return false;
    }
}