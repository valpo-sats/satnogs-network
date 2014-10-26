$(function () {
  $('#datetimepicker-start').datetimepicker();
  $('#datetimepicker-end').datetimepicker();

  $('#satellite-selection').change( function() {
    var norad = $(this).find(':selected').data("norad");
    $('#transponder-selection').prop("disabled", false);
    $('#transponder-selection option').hide();
    $('#transponder-selection option[data-satellite="'+norad+'"]').show().prop("selected", true);
    if($('#transponder-selection option:visible').length === 0) {
      $('#transponder-selection').prop("disabled", true);
      $('#transponder-selection option[id="no-transponder"]').show().prop("selected", true);
    }
  });
});

$( document ).ready( function(){
  $('#calculate-observation').click( function(){
    var satellite = $('#satellite-selection').val();
    var start_time = $('#datetimepicker-start input').val();
    var end_time = $('#datetimepicker-end input').val();

    $.ajax({
      url: '/prediction_windows/'+satellite+'/'+start_time+'/'+end_time
      }).done(function(data) {
        var suggested_data = [];
        $.each(data, function( i,k ){
          label = k.id + " - " + k.name;
          var times = [];
          console.log(k);
          $.each(k.window, function( m,n ){
            var starting_time = moment(n.start).valueOf();
            var ending_time = moment(n.end).valueOf();
            times.push({starting_time: starting_time, ending_time: ending_time})
          });
          suggested_data.push({label : label, times : times});
          //console.log(k);
          //console.log(k.name);
        });
        
        /*data.each(function( index ){
          var data_groundstation = $(this).data('groundstation');
          var data_time_start = 1000 * $(this).data('start');
          var data_time_end = 1000 * $(this).data('end');
          observation_data.push({label : data_groundstation, times : [{starting_time: data_time_start, ending_time: data_time_end}]});
        });*/
        timeline_init(start_time, end_time, suggested_data);
      });

  });
});

function timeline_init( start, end, payload ){
  var start_time_timeline = moment(start).valueOf();
  var end_time_timeline = moment(end).valueOf();

  $('#timeline').empty();

  var chart = d3.timeline()
              .stack()
              .beginning(start_time_timeline)
              .ending(end_time_timeline)
              .hover(function (d, i, datum) {
                // d is the current rendering object
                // i is the index during d3 rendering
                // datum is the id object
                var div = $('#hoverRes');
                var colors = chart.colors();
                div.find('.coloredDiv').css('background-color', colors(i))
                div.find('#name').text(datum.label);
              })
              .margin({left:140, right:10, top:0, bottom:50})
              .tickFormat({format: d3.time.format("%H:%M"), tickTime: d3.time.minutes, tickInterval: 30, tickSize: 6})
              ;

  var svg = d3.select("#timeline").append("svg").attr("width", 1140)
    .datum(payload).call(chart);
}