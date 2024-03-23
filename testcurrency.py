"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Iddo Barnoon
Date:   03/16/2024
"""
import introcs
import currency


def test_before_space():
    """
    Test procedure for before_space
    """
    print('Testing before_space')
    result = currency.before_space('Apple Pie')
    introcs.assert_equals('Apple', result)

    result = currency.before_space('Pecan  Pie')
    introcs.assert_equals('Pecan', result)

    result = currency.before_space('25 Pecan Pies')
    introcs.assert_equals('25', result)

    result = currency.before_space(' Pies')
    introcs.assert_equals('', result)


def test_after_space():
    """
    Test procedure for after_space
    """
    print('Testing after_space')
    result = currency.after_space('Apple Pie')
    introcs.assert_equals('Pie', result)

    result = currency.after_space('Apple  Pie')
    introcs.assert_equals(' Pie', result)

    result = currency.after_space('25 Pecan Pies')
    introcs.assert_equals('Pecan Pies', result)

    result = currency.after_space('Pies ')
    introcs.assert_equals('', result)


def test_first_inside_quotes():
    """
    Test procedure for first_inside_quotes
    """
    print('Testing first_inside_quotes')
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)

    result = currency.first_inside_quotes('"" A B C')
    introcs.assert_equals('', result)

    result = currency.first_inside_quotes("\"A 'B' C\"")
    introcs.assert_equals('A \'B\' C', result)


def test_get_src():
    """
    Test procedure for get_src
    """
    print('Testing get_src')
    result = currency.get_src('{"success": true, "src": "2 United States Dollars", \
                              "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)

    result = currency.get_src('{"success":false,"src":"",\
                              "dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    result = currency.get_src('{"success":true, "src":"2 United States Dollars", \
                              "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars', result)
    
    result = currency.get_src('{"success": false, "src": "", \
                              "dst": "", "error": "Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_get_dst():
    """
    Test procedure for get_dst
    """
    print('Testing get_dst')
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars", \
                              "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

    result = currency.get_dst('{"success":false,"src":"",\
                              "dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    result = currency.get_dst('{"success":true, "src":"2 United States Dollars", \
                              "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros', result)
    
    result = currency.get_dst('{"success": false, "src": "", \
                              "dst": "", "error": "Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_has_error():
    """
    Test procedure for has_error
    """
    print('Testing has_error')
    result = currency.has_error('{"success": true, "src": "2 United States Dollars", \
                              "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(result)

    result = currency.has_error('{"success":false,"src":"",\
                              "dst":"","error":"Source currency code is invalid."}')
    introcs.assert_true(result)

    result = currency.has_error('{"success":true, "src":"2 United States Dollars", \
                              "dst":"1.772814 Euros", "error":""}')
    introcs.assert_false(result)
    
    result = currency.has_error('{"success": false, "src": "", \
                              "dst": "", "error": "Source currency code is invalid."}')
    introcs.assert_true(result)


def test_service_response():
    """
    Test procedure for service_response
    """
    print('Testing service_response')
    result = currency.service_response('USD', 'EUR', 2.5)
    introcs.assert_equals(('{"success": true, "src": "2.5 United States Dollars",'+
                           ' "dst": "2.2160175 Euros", "error": ""}'), result)
    
    result = currency.service_response('USD', 'ISR', 25)
    introcs.assert_equals(('{"success": false, "src": "", "dst": "", '+
                           '"error": "The rate for currency ISR is not present."}'), result)

    result = currency.service_response('ISR', 'USD', 25)
    introcs.assert_equals(('{"success": false, "src": "", "dst": "",'+
                           ' "error": "The rate for currency ISR is not present."}'), result)

    result = currency.service_response('USD', 'EUR', 0)
    introcs.assert_equals(('{"success": true, "src": "0.0 United States Dollars",'+
                           ' "dst": "0.0 Euros", "error": ""}'), result)

    result = currency.service_response('XXZ', 'XXX', 0)
    introcs.assert_equals(('{"success": false, "src": "", "dst": "",'+
                           ' "error": "The rate for currency XXZ is not present."}'), result)

    result = currency.service_response('USD', 'GBP', -1)
    introcs.assert_equals(('{"success": true, "src": "-1.0 United States Dollar", '+
                           '"dst": "-0.79542 British Pounds Sterling", "error": ""}'), result)


def test_iscurrency():
    """
    Test procedure for iscurrency
    """
    print('Testing iscurrency')
    result = currency.iscurrency('USD')
    introcs.assert_equals(True, result)

    result = currency.iscurrency('XXX')
    introcs.assert_equals(False, result)


def test_exchange():
    """
    Test procedure for exchange
    """
    print('Testing exchange')
    result = currency.exchange('USD', 'EUR', 2)
    introcs.assert_floats_equal(1.772814, result)

    result = currency.exchange('USD', 'EUR', -2.0)
    introcs.assert_floats_equal(-1.772814, result)


# Function calls below
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print("All tests completed successfully")