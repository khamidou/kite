'use strict';

/* jasmine specs for controllers go here */

describe('controllers', function(){
    beforeEach(module('KiteMail.controllers'));

    
    describe('MailsListController', function() {
        it('should do an ajax request to query mails', inject(function($injector) {
            var $httpBackend = $injector.get('$httpBackend');
            $httpBackend.expectGET('/karim/mail', 200);

            var $rootScope = $injector.get('$rootScope');
            var ctrl = $injector.get("MailsListController", {$scope: $rootScope})
            this.$httpBackend.flush();
        }));

        it('should ....', inject(function() {
        //spec body
        }));
    });
});
