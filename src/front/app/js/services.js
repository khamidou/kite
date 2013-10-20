'use strict';

/* Services */

angular.module('KiteMail.services', ['ngResource']).
factory('Emails', ['$resource',
    function($resource) {
        var data = $resource('/kite/:user/mail/', {}, {
            query: {
                method:'GET',
                params:{user: "karim"},
                isArray:true,
                transformResponse: function(data) {
                    var data = angular.fromJson(data);

                    // convert date string to js date objects
                    for(var i = 0; i < data.length; i++) {
                        data[i]["date"] = new Date(data[i]["date"]);
                    }

                    return data;
                },
                
            },
       });

    }
]);


