'use strict';

/* Controllers */

angular.module('KiteMail.controllers', []).
  controller('InboxListController', function($scope) {
        $scope.inboxes = [
            {"name": "Inbox", },
            {"name": "Trash", },
            {"name": "Spam",  },];
            
}).controller('LoginController', function($scope) {
    
    
});
