'use strict';

/* Controllers */

angular.module('KiteMail.controllers', []).
  controller('InboxesListController', function($scope) {
        $scope.inboxes = [
            {"name": "Inbox", },
            {"name": "Trash", },
            {"name": "Spam",  },];
            
}).controller('MailsListController', function($scope) {
        $scope.mails = [
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
            }];
    
    
}).controller('LoginController', function($scope) {
    
    
});
