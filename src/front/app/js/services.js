'use strict';

/* Services */

angular.module('KiteMail.services', ['ngResource', 'ngCookies']).
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
}).factory('Auth', ['$cookies', '$http', 
    function($cookies, $http) {
        var _isAuth = false;
        var _username = null
        var _cookies = $cookies;
        return {
            loggedIn: function() { return _isAuth; },
            username: _username,
            doLogin: function(username, password, success, failure) {
                _username = username;
                $http({url: '/kite/auth', method:'POST',  data: {"username": username, "password": password}}).
                            success(function(data, status, headers, config) {
                                _isAuth = true;
                                $http.defaults.headers.common["X-XSRF-TOKEN"] = "BLAH";
                                success(data);
                            });
            },

        };
    }]);


