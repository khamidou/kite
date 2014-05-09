'use strict';

/* Controllers */

angular.module('KiteMail.controllers', []).
  controller('InboxesListController', function($scope) {
        $scope.inboxes = [
            {"name": "Inbox", },
            {"name": "Trash", },
            {"name": "Spam",  },];
            
}).controller('MailsListController', ['$scope', 'Emails', 'Auth', function($scope, Emails, Auth) {
        $scope.threads = Emails.threads({username: "testuser"});
}]).controller('LoginController', ['$scope', 'Auth', function($scope, Auth) {
    $scope.doLogin = function(isValid) {
        if(isValid) {
            var success = function() {
                console.log("SUCCESS");
            };
            
            var failure = function() {
                console.log("FAILURE");
            };

            Auth.doLogin($scope.username, $scope.password, success, failure); 
            console.log("PASS" + $scope.password);            
        }
    }    
}]).controller('ThreadController', ['$scope', '$routeParams', '$sce', 'Emails', function($scope, $routeParams, $sce, Emails) {
    $scope.thread = Emails.thread({username: "testuser", "id": $routeParams.id});
    $scope.trustHTML = function(html_code) {
        return $sce.trustAsHtml(html_code);
    };
}]);
