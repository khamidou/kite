'use strict';

/* jasmine specs for controllers go here */

describe('controllers', function(){
    beforeEach(module('KiteMail.controllers'));

    describe('MailsListController', function() {
        it('should do an ajax request to query mails', inject(function($controller, $httpBackend) {
            var scope = {};
            this.$httpBackend.expectGET('/karim/mail', 200);
            var ctrl = $controller("MailsListController", {$scope: scope})
            this.$httpBackend.flush();
        }));

        it('should ....', inject(function() {
        //spec body
        }));
    });
});
