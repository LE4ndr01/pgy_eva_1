const nombre = document.getElementById("Nombre")
const contraseña = document.getElementById("Contraseña")
const form = document.getElementsByName("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", e=> {
    e.preventDefault()
    let warnings = ""
    let entrar = false
    if(nombre.value.lenght <6){
        warnings += 'El nombre es muy corto <br>'
        entrar = true
    }
    if(contraseña.value.lenght <8){
        warnings += 'La contraseña no es valida <br>'
        entrar = true
    }
    if(entrar){
        parrafo.innerHTML = warnings
    }
})