/* app.mock.js - support mocks for online demo */
'use strict';


// Declare app level module which depends on filters, and services
angular.module('KiteMail', ['ngMockE2E', 'ngRoute', 'KiteMail.filters', 'KiteMail.services', 'KiteMail.directives', 'KiteMail.controllers']).
  config(['$routeProvider', function($routeProvider) {

    $routeProvider.when('/mail', {templateUrl: 'partials/mailbox.html', controller: 'InboxesListController'});
    $routeProvider.when('/login', {templateUrl: 'partials/login.html', controller: 'LoginController'});
    $routeProvider.when('/thread/:id', {templateUrl: 'partials/thread.html', controller: 'ThreadController'});
    $routeProvider.otherwise({redirectTo: '/login'});
  }]).run(function($httpBackend) {
    $httpBackend.whenGET(/^partials\//).passThrough();
    $httpBackend.whenGET(/^css\//).passThrough();
    $httpBackend.whenGET(/^fonts\//).passThrough();
    $httpBackend.whenGET(/^img\//).passThrough();
    var mails = [
    {   "from": "Karim Hamidou",
        "to": "You (user@kiteapp.com)",
        "subject": "Welcome to Kite !",
        "contents": "This is a very basic demo of kite.\nAs you can see, there isn't a lot working. But displaying emails works!",
        "date": "Fri, 1 Nov 2013 14:27:06 +0000 (UTC)",
        "id": "1"
    }, 
    {   "from": "Nigerian Prince",
        "to": "You (user@kiteapp.com)",
        "subject": "My dear friend, this is an urgent, private matter...",
        "contents": "I need your help for this particular endeavour of mine. I need to transfer a large sum of money out of my country.",
        "date": "Fri, 1 Nov 2012 14:27:06 +0000 (UTC)",
        "id": "2"
    }];

    $httpBackend.whenGET('/kite/karim/mail').respond(200, angular.toJson(mails));
    $httpBackend.whenGET('/kite/karim/mail/1').respond(200, angular.toJson([mails[0]]));
    $httpBackend.whenGET('/kite/karim/mail/2').respond(200, angular.toJson([mails[1]]));

});
