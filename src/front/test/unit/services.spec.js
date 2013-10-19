'use strict';

/* jasmine specs for services go here */

describe('service', function() {
    beforeEach(module('KiteMail.services'));

    describe('EmailsService', function() {
    it('should do an ajax request to get the list of services', inject(function($service) {
        var resourceMock = jasmine.createSpy('$resource').andReturn([{"subject": "mock", "date": "2013-04-23"}]);
        var service = $service("EmailsService", resourceMock);
        expect(resourceMock).toHaveBeenCalled()
        
    }))});
});
