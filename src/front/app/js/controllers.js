'use strict';

/* Controllers */

angular.module('KiteMail.controllers', []).
  controller('InboxesListController', function($scope) {
        $scope.inboxes = [
            {"name": "Inbox", },
            {"name": "Trash", },
            {"name": "Spam",  },];
            
}).controller('MailsListController', ['$scope', 'Emails', function($scope, Emails) {
        $scope.mails = Emails.threads({username: "karim"});
}]).controller('LoginController', function($scope) {
    
    
}).controller('ThreadController', function($scope, $routeParams, Emails) {
    console.log($routeParams.id);
    $scope.thread = Emails.thread({username: "karim", "id": $routeParams.id});
});
