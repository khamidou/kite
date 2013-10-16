'use strict';

/* Controllers */

angular.module('KiteMail.controllers', []).
  controller('InboxesListController', function($scope) {
        $scope.inboxes = [
            {"name": "Inbox", },
            {"name": "Trash", },
            {"name": "Spam",  },];
            
}).controller('MailsListController', ['$scope', 'Emails', function($scope, Emails) {
        $scope.mails = Emails.query(); /*[
            {"from": "random.spam@spam.com",
             "to": "you",
             "subject": "-50% promo on everything !",
             "contents": "Everything must go !",
             "date": new Date(),
            },
 
            {"from": "nigerian.prince@spam.com",
             "to": "user@mail.com",
             "subject": "I need your urgent help",
             "contents": "Hi my dear friend. I need your help urgently in a matter of financial problems.",
             "date": new Date(1992, 4, 24),
            },
            {"from": "team@kitemail",
             "name": "Kite team",
             "to": "user@mail.com",
             "subject": "Welcome to Kite !",
             "contents": "This is the basic inbox page. As you can see, it looks a lot like a famous email service.",
             "date": new Date(),
            }]; */
}]).controller('LoginController', function($scope) {
    
    
}).controller('ThreadController', function($scope) {
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
