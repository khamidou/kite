'use strict';

/* jasmine specs for controllers go here */

describe('controllers', function(){
    beforeEach(
    function() {
        module('KiteMail.controllers');
    });

    
    describe('MailsListController', function() {
        it('should call Email.query service to query mails', inject(function($controller, $rootScope) {
            var locals = {
                $scope: $rootScope,
                Emails: jasmine.createSpyObj('Emails', ['threads']),
            };
            
            var ctrl = $controller("MailsListController", locals)
            expect(locals.Emails.threads).toHaveBeenCalled();
        }));

        it('should ....', inject(function() {
        //spec body
        }));
    });
});
