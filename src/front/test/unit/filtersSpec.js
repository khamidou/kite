'use strict';

/* jasmine specs for filters go here */

describe('filter', function() {
    beforeEach(module('KiteMail.filters'));


    describe('setup suite', function() {
        beforeEach(module(function($provide) {
    }));


    it('should truncate text', inject(function(truncateFilter) {
        var testStr = "This is a long string with a lot of chars";
        var resStr = "This is a long string with a lot of" + "...";
        expect(truncateFilter(testStr)).toEqual(resStr);
    }));

    it('should format a date', inject(function(formatDateFilter) {
        var date = new Date(2013, 9, 13);
        expect(formatDateFilter(date)).toEqual("Oct, 13");
    }));

    it('should have the year in the string if the date is not from this year', inject(function(formatDateFilter) {
        var date = new Date(2009, 9, 13);
        expect(formatDateFilter(date)).toEqual("Oct, 13, 2009");
    }));


  });
});
