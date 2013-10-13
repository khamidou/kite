'use strict';

/* Services */

angular.module('KiteMail.services', ['ngResource']).
factory('Emails', ['$resource',
    function($resource) {
        return $resource(':user/mail/', {}, {
            query: {method:'GET', params:{user: "karim"}, isArray:true}   
        });
    }
]);


