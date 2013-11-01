'use strict';

/* jasmine specs for services go here */

describe('service', function() {
    var mockResource, $httpBackend;
    beforeEach(angular.mock.module('KiteMail.services'));
    
    beforeEach(function() {
        inject(function($injector) {
            /*
            $httpBackend = $injector.get('$httpBackend');
            mockResource = $injector.get('Emails');
            */
        });
    });

    describe('EmailsService', function() {
    it('should do an ajax request to get the list of emails', inject(function(Emails, $httpBackend) {
        var mockResponse = [
            {"subject": "Hi",
             "contents": "We haven't spoke in a long time !",
             "name": "Michel De Test",
             "from": "michel@example.com",
             "to": "gerard@example.com",
             "date": new Date(1992, 4, 24),
            }
        ];

        $httpBackend.expectGET('/kite/test/mail').respond(mockResponse);
        var result = Emails.emails({username: "test"});
        console.log(result);
        expect(result == mockResponse).toBe(true);

    }))});
});
