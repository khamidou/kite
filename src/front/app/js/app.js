'use strict';


// Declare app level module which depends on filters, and services
angular.module('KiteMail', ['KiteMail.filters', 'KiteMail.services', 'KiteMail.directives', 'KiteMail.controllers']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/mail', {templateUrl: 'partials/mailbox.html', controller: 'InboxesListController'});
    $routeProvider.when('/login', {templateUrl: 'partials/login.html', controller: 'LoginController'});
    $routeProvider.when('/thread', {templateUrl: 'partials/thread.html', controller: 'ThreadController'});
    $routeProvider.otherwise({redirectTo: '/login'});
  }]);
