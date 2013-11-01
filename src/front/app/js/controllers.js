'use strict';

/* Controllers */

angular.module('KiteMail.controllers', []).
  controller('InboxesListController', function($scope) {
        $scope.inboxes = [
            {"name": "Inbox", },
            {"name": "Trash", },
            {"name": "Spam",  },];
            
}).controller('MailsListController', ['$scope', 'Emails', function($scope, Emails) {
        $scope.mails = Emails.emails();
}]).controller('LoginController', function($scope) {
    
    
}).controller('ThreadController', function($scope, $routeParams) {
    $scope.thread = [
        {"subject": "Hi",
         "contents": "We haven't spoke in a long time !",
         "name": "Michel De Test",
         "from": "michel@example.com",
         "to": "gerard@example.com",
         "date": new Date(1992, 4, 24),
        },
        {"subject": "Hi",
         "contents": "We haven't spoke in a long time !",
         "from": "michel@example.com",
         "to": "gerard@example.com",
         "name": "Gerard Le Test",
         "date": new Date(),
        }
    ]
});
