'use strict';


// Declare app level module which depends on filters, and services
angular.module('KiteMail', ['ngRoute', 'ngCookies', 'KiteMail.filters', 'KiteMail.services', 'KiteMail.directives', 'KiteMail.controllers']).
  config(['$routeProvider', '$httpProvider', function($routeProvider, $httpProvider) {
    $routeProvider.when('/mail', {templateUrl: 'partials/mailbox.html', controller: 'InboxesListController'});
    $routeProvider.when('/login', {templateUrl: 'partials/login.html', controller: 'LoginController'});
    $routeProvider.when('/thread/:id', {templateUrl: 'partials/thread.html', controller: 'ThreadController'});
    $routeProvider.otherwise({redirectTo: '/login'});

    var interceptor = ['$rootScope', '$q', '$location', function (scope, $q, $location) {
        function success(response) {
            var status = response.status;
            // user is unauthorized.
            if (status == 401) {
                //window.location = "/account/login?redirectUrl=" + Base64.encode(document.URL);
                $location.path("/login");
                return;
            }

            return response;
        }
        function error(response) {
                        // otherwise
            return $q.reject(response);
        }
        return function (promise) {
            return promise.then(success, error);
        }
    }];
    $httpProvider.responseInterceptors.push(interceptor);

  }]).run(['$rootScope', '$location', 'Auth', function($rootScope, $location, Auth) { 
/*   $rootScope.$on( "$routeChangeStart", function(event, next, current) {
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
*/
  }]);
