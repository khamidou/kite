'use strict';

/* Filters */

angular.module('KiteMail.filters', []).
    filter('truncate', function() {
            return function(text) {
            return text.slice(0, 35) + "...";
        }
    }).
    
    /* takes a date object and returns a formatted object */
    filter('formatDate', function() {
        return function(date) {
            var date2array = function(date) {
                return (date+'').split(' ');
            }

            var today = date2array(new Date(Date.now()));
            var da = date2array(date);

            if(da[3] == today[3]) {
                return da[1] + ", " + da[2];
            } else {
                return da[1] + ", " + da[2] + ", " + da[3];
            }
        }  
    });
