L.mapbox.accessToken = 'pk.eyJ1IjoicGllcnJvcyIsImEiOiJhTVZyWmE4In0.kl2j9fi24LDXfB3MNdN76w';
var map = L.mapbox.map('map', 'pierros.jbf6la1j',{
    zoomControl: false
}).setView([40, 0], 3);

$(document).ready(function() {

    $('#successful a').click(function (e) {
        e.preventDefault()
        $(this).tab('show')
    })

    $.ajax({
        url: "/stations/json"
        }).done(function(data) {
            data.forEach(function(m) {
                L.mapbox.featureLayer({
                    type: 'Feature',
                    geometry: {
                        type: 'Point',
                        coordinates: [
                          parseFloat(m.fields.lng),
                          parseFloat(m.fields.lat)
                        ]
                    },
                    properties: {
                        title: m.fields.name,
                        'marker-size': 'large',
                        'marker-color': '#666',
                    }
                }).addTo(map);
            });
        });
});
