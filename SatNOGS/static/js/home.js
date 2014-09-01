L.mapbox.accessToken = 'pk.eyJ1IjoicGllcnJvcyIsImEiOiJhTVZyWmE4In0.kl2j9fi24LDXfB3MNdN76w';
var map = L.mapbox.map('map', 'pierros.jbf6la1j').setView([40, 0], 3);

$('#successful a').click(function (e) {
e.preventDefault()
$(this).tab('show')
})