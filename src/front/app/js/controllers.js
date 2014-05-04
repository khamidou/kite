'use strict';

/* Controllers */

angular.module('KiteMail.controllers', []).
  controller('InboxesListController', function($scope) {
        $scope.inboxes = [
            {"name": "Inbox", },
            {"name": "Trash", },
            {"name": "Spam",  },];
            
}).controller('MailsListController', ['$scope', 'Emails', function($scope, Emails) {
        $scope.threads = Emails.threads({username: "testuser"});
}]).controller('LoginController', function($scope) {
    
}).controller('ThreadController', ['$scope', '$routeParams', '$sce', 'Emails', function($scope, $routeParams, $sce, Emails) {
    $scope.thread = Emails.thread({username: "testuser", "id": $routeParams.id});
    console.log("YOLO");
    $scope.trustHTML = function(html_code) {
        console.log("called");
        return $sce.trustAsHtml(html_code);
    };
}]);
