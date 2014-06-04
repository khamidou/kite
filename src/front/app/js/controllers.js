'use strict';

/* Controllers */

angular.module('KiteMail.controllers', ['KiteMail.services'])
.controller('InboxesListController', ['$scope', function($scope) {
        $scope.inboxes = ["Inbox"]; 

}]).controller('MailsListController', ['$scope', 'Emails', 'Auth', function($scope, Emails, Auth) {

        $scope.threads = Emails.threads({username: Auth.username()});

}]).controller('ThreadController', ['$scope', '$routeParams', '$sce', 'Emails', 'Auth', function($scope, $routeParams, $sce, Emails, Auth) {
    $scope.thread = Emails.thread({username: Auth.username(), "id": $routeParams.id});
    $scope.trustHTML = function(html_code) {
        return $sce.trustAsHtml(html_code);
    };
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
}]).controller('LogoutController', ['$scope', '$location', 'Auth', function($scope, $location, Auth) {
    $scope.doLogout = function() {
        Auth.doLogout();        
        $location.path("/login");
    };
}]);
