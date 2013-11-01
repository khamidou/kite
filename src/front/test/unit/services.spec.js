'use strict';

/* jasmine specs for services go here */

describe('Emails service', function() {
    var mockResource, $httpBackend;
    beforeEach(angular.mock.module('KiteMail.services'));
    
    describe('EmailsService', function() {
    it('should do an ajax request to get the list of emails', inject(function(Emails, $httpBackend) {
        var mockResponse = [
            {"subject": "Hi",
             "contents": "We haven't spoke in a long time !",
             "name": "Michel De Test",
             "from": "michel@example.com",
             "to": "gerard@example.com",
             "date": "September 24 2013"
            }
        ];

        $httpBackend.expectGET('/kite/test/mail').respond(mockResponse);
        var result = Emails.emails({username: "test"});
        $httpBackend.flush();
        var date = result[0]["date"];
        expect(date instanceof Date).toBe(true);
        expect(date.getDate() == 24).toBe(true);
        expect(date.getMonth() == 8).toBe(true);
        expect(date.getFullYear() == 2013).toBe(true);

    }))});
});

describe('Utils service', function() {
    beforeEach(angular.mock.module('KiteMail.services'));
    
    describe('date2array', function() {
    it("should convert dates to arrays", inject(function(Utils) {
        var date = new Date("May 30 2013");
        var array = Utils.date2array(date);
        expect(array[1]).toEqual("May");
        expect(array[2]).toEqual("30");
        expect(array[3]).toEqual("2013");
    }))});
});
