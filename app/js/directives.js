'use strict';

/* Directives */


angular.module('KiteMail.directives', []).
  directive('baseLayout', function() {
    return {
     restrict: 'A',
     scope: {
         title: '@',
     },
     transclude: true,
     replace: true,
     templateUrl: 'partials/baselayout.html',
    }
});
