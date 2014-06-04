'use strict';

/* Services */

angular.module('KiteMail.services', ['ngResource', 'ngCookies']).
factory('Emails', ['$resource', 'Utils',
    function($resource, Utils) {
        /* FIXME: maybe move this code to a response interceptor? */
        var processThreads = function(data) {
            var data = angular.fromJson(data);
            return Utils.cleanDates(data);
            };
        
        var processThread = function(data) {
            var data = angular.fromJson(data);
            data.messages = Utils.cleanDates(data.messages);
            debugger;
            return data;
        };

        var res = $resource('/kite/:username/mail/:id', {}, {
            threads: {
                method:'GET',
                params:{username: "@username"},
                isArray:true,
                transformResponse: processThreads,
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
        },
        
         /* cleandates: transform every field named "date" to a js Date object */
         cleanDates: function(data) {
            for(var i = 0; i < data.length; i++) {
                data[i]["date"] = new Date(data[i]["date"]);
            }
            return data;
        },
    };   
}).factory('Auth', ['$cookies', '$http', 
    function($cookies, $http) {
        var _isAuth = false;
        var _username = null;
        var _cookies = $cookies;
        return {
            loggedIn: function() { return _isAuth; },
            username: function() { return _username; },
            doLogout: function() { _isAuth = false; _username = null; },
            doLogin: function(username, password, success, failure) {
                $http({url: '/kite/auth', method:'POST',  data: {"username": username, "password": password}}).
                            success(function(data, status, headers, config) {
                                _username = username;
                                _isAuth = true;
                                success(data);
                            });
            },

        };
    }]);


