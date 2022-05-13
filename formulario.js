const name = document.getElementById("name")
const password = document.getElementById("password")
const form = document.getElementsByName("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", e=> {
    e.preventDefault()
    let warnings = ""
    let entrar = false
    if(name.value.lenght <6){
        warnings += 'El nombre es muy corto <br>'
        entrar = true
    }
    if(password.value.lenght <8){
        warnings += 'La contraseña no es valida <br>'
        entrar = true
    }
    if(entrar){
        parrafo.innerHTML = warnings
    }
})