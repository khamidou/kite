'use strict';


// Declare app level module which depends on filters, and services
angular.module('KiteMail', ['KiteMail.filters', 'KiteMail.services', 'KiteMail.directives', 'KiteMail.controllers']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {templateUrl: 'partials/mailbox.html', controller: 'InboxListController'});
    $routeProvider.when('/login', {templateUrl: 'partials/login.html', controller: 'LoginController'});
    $routeProvider.otherwise({redirectTo: '/'});
  }]);
