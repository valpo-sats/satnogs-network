/* global L */

$(document).ready(function() {
    'use strict';

    // Render Station success rate
    var success_rate = $('.progress-bar-success').data('success-rate');
    var percentagerest = $('.progress-bar-danger').data('percentagerest');
    $('.progress-bar-success').css('width', success_rate + '%');
    $('.progress-bar-danger').css('width', percentagerest + '%');

    // Reading data for station
    var station_info = $('#station-info').data();

    // Confirm station deletion
    var message = 'Do you really want to delete this Ground Station?';
    var actions = $('#station-delete');
    if (actions.length) {
        actions[0].addEventListener('click', function(e) {
            if (! confirm(message)) {
                e.preventDefault();
            }
        });
    }

    // Init the map
    var mapboxid = $('div#map-station').data('mapboxid');
    var mapboxtoken = $('div#map-station').data('mapboxtoken');

    L.mapbox.accessToken = mapboxtoken;
    L.mapbox.config.FORCE_HTTPS = true;
    var map = L.mapbox.map('map-station', mapboxid,{
        zoomControl: false
    }).setView([station_info.lat, station_info.lng], 6);

    // Add a marker
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
