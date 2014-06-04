'use strict';


// Declare app level module which depends on filters, and services
angular.module('KiteMail', ['ngRoute', 'ngCookies', 'KiteMail.filters', 'KiteMail.services', 'KiteMail.directives', 'KiteMail.controllers']).
  factory('errorInterceptor', ['$rootScope', '$q', '$location', function (scope, $q, $location) {
        return {
            response: function (response) {
                if (response && response.status === 401) {
                    $location.path("/login");
                    return $q.reject(response);
                }

                return response || $q.when(response);
            },
    }; 
  }]).config(['$routeProvider','$httpProvider', function($routeProvider, $httpProvider) {

    $routeProvider.when('/mail', {templateUrl: 'partials/mailbox.html', controller: 'InboxesListController'});
    $routeProvider.when('/login', {templateUrl: 'partials/login.html', controller: 'LoginController'});
    $routeProvider.when('/thread/:id', {templateUrl: 'partials/thread.html', controller: 'ThreadController'});
    $routeProvider.otherwise({redirectTo: '/login'});

    $httpProvider.interceptors.push('errorInterceptor');

  }]).run(['$rootScope', '$location', 'Auth', function($rootScope, $location, Auth) { 
  }]);
