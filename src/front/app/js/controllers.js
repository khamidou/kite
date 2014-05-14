'use strict';

/* Controllers */

angular.module('KiteMail.controllers', ['KiteMail.services']).
  controller('InboxesListController', function($scope) {
        $scope.inboxes = [
            {"name": "Inbox", },
            {"name": "Trash", },
            {"name": "Spam",  },];
            
}).controller('MailsListController', ['$scope', 'Emails', 'Auth', function($scope, Emails, Auth) {
        console.log(Auth.username());
        $scope.threads = Emails.threads({username: Auth.username()});
}]).controller('LoginController', ['$scope', '$location', 'Auth', function($scope, $location, Auth) {
    $scope.doLogin = function(isValid) {
        if(isValid) {
            var success = function() {
                $location.path("/mail");
            };
            
            var failure = function() {
                console.log("FAILURE");
            };

            Auth.doLogin($scope.username, $scope.password, success, failure); 
        }
    }    
}]).controller('ThreadController', ['$scope', '$routeParams', '$sce', 'Emails', 'Auth', function($scope, $routeParams, $sce, Emails, Auth) {
    $scope.thread = Emails.thread({username: Auth.username(), "id": $routeParams.id});
    $scope.trustHTML = function(html_code) {
        return $sce.trustAsHtml(html_code);
    };
}]);
