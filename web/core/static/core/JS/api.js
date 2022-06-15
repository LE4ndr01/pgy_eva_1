let url = "https://maps.googleapis.com/maps/api/js?key=AIzaSyC9XHaM2yer6dlEGYKoA5jyQkp-8f2Kvc4&callback=initMap&libraries=&v=weekly"
$.get(url, function(respuesta){

    console.log(respuesta)
}, "json")