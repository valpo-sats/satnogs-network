$(document).ready(function() {
    //Reading data for station
    var station_info = $('#station-info').data();

    //Init the map
    L.mapbox.accessToken = 'pk.eyJ1IjoicGllcnJvcyIsImEiOiJhTVZyWmE4In0.kl2j9fi24LDXfB3MNdN76w';
    var map = L.mapbox.map('map-station', 'pierros.jbf6la1j',{
        zoomControl: false
    }).setView([station_info.lat, station_info.lng], 6);

    //Add a marker
    L.mapbox.featureLayer({
        type: 'Feature',
        geometry: {
            type: 'Point',
            coordinates: [
              parseFloat(station_info.lng),
              parseFloat(station_info.lat)
            ]
        },
        properties: {
            title: station_info.name,
            'marker-size': 'large',
            'marker-color': '#666',
        }
    }).addTo(map);
});
