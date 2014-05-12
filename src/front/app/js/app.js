'use strict';


// Declare app level module which depends on filters, and services
angular.module('KiteMail', ['ngRoute', 'ngCookies', 'KiteMail.filters', 'KiteMail.services', 'KiteMail.directives', 'KiteMail.controllers']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/mail', {templateUrl: 'partials/mailbox.html', controller: 'InboxesListController'});
    $routeProvider.when('/login', {templateUrl: 'partials/login.html', controller: 'LoginController'});
    $routeProvider.when('/thread/:id', {templateUrl: 'partials/thread.html', controller: 'ThreadController'});
    $routeProvider.otherwise({redirectTo: '/login'});
  }]).run(['$rootScope', '$location', 'Auth', function($rootScope, $location, Auth) { 
   $rootScope.$on( "$routeChangeStart", function(event, next, current) {
        console.log(Auth.loggedIn());
        if (!Auth.loggedIn()) {
            // no logged user, redirect to /login
            if (next.templateUrl != "partials/login.html") {
                $location.path("/login");
            }
        } else { // already loggedin
            if (next.templateUrl == "partials/login.html") {
                $location.path("/mail");
            }
        }
    }); 
  }]);
