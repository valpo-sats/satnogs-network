$(document).ready(function() {
    'use strict';

    var button = $('#collapseFilters > button');

    $(button).click(function() {
        $(this).toggleClass('active');
    });
});
