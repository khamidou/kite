'use strict';

/* Filters */

angular.module('KiteMail.filters', ['KiteMail.services']).
    filter('truncate', function() {
            return function(text) {
            return text.slice(0, 35) + "...";
        }
    }).
    
    /* takes a date object and returns a formatted object */
    filter('formatDate', function(Utils) {
        return function(date) {
            var today = Utils.date2array(new Date(Date.now()));
            var da = Utils.date2array(date);

            if(da[3] == today[3]) {
                return da[1] + ", " + da[2];
            } else {
                return da[1] + ", " + da[2] + ", " + da[3];
            }
        }  
    });
