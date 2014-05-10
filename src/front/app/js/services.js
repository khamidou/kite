'use strict';

/* Services */

angular.module('KiteMail.services', ['ngResource']).
factory('Emails', ['$resource',
    function($resource) {
        var processThread = function(data) {
            var data = angular.fromJson(data);

            // convert date string to js date objects
            for(var i = 0; i < data.length; i++) {
                console.log(data[i]["date"]);
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
                isArray: false,
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
}).factory('Auth', ['$http', function($http) {
    var _isAuth = false;
    var _username = null
    return {
        loggedOn: function() { return _isAuth },
        username: _username,
        doLogin: function(username, password, success, failure) {
            _username = username;
            $http({url: '/kite/auth', method:'POST',  data: {"username": username, "password": password}}).
                        success(function(data, status, headers, config) {
                            _isAuth = true;
                            success(data);
                        });
        },

    };
    
}]);


