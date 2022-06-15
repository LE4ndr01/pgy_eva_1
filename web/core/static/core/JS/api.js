let url = "https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap&libraries=&v=weekly"
$.get(url, function(respuesta){

    console.log(respuesta)
}, "json")