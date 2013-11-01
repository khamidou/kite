'use strict';

/* Services */

angular.module('KiteMail.services', ['ngResource']).
factory('Emails', ['$resource',
    function($resource) {
        var processThread = function(data) {
            var data = angular.fromJson(data);

            // convert date string to js date objects
            for(var i = 0; i < data.length; i++) {
                data[i]["date"] = new Date(data[i]["date"]);
            }

            return data;
        }

        var res = $resource('/kite/:username/mail/:id', {}, {
            threads: {
                method:'GET',
                params:{username: "@username"},
                isArray:true,
                transformResponse: processThread,
            },

            thread: {
                method:'GET',
                params:{username: "@username", id: "@id"},
                isArray: true,
                transformResponse: processThread, 
            },
       });
        
        return res;
    }
]).factory('Utils', function() {
    return {
         date2array: function(date) {
            return (date+'').split(' ');
        }
    };   
});


