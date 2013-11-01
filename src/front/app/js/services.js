'use strict';

/* Services */

angular.module('KiteMail.services', ['ngResource']).
factory('Emails', ['$resource',
    function($resource) {
        var res = $resource('/kite/:username/mail/', {}, {
            emails: {
                method:'GET',
                params:{username: "@username"},
                isArray:true,
                transformResponse: function(data) {
                    var data = angular.fromJson(data);

                    debugger;
                    // convert date string to js date objects
                    for(var i = 0; i < data.length; i++) {
                        data[i]["date"] = new Date(data[i]["date"]);
                    }

                    return data;
                },
                
            },
       });
        
        return res;
    }
]);


