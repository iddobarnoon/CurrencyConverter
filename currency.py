"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Iddo Barnoon
Date:   03/16/2024
"""
import introcs
APIKEY = 'GXANbCLftkPNvt5DpEYldH7LiVUdCVphhWRNEpZ3HPse'

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.
    
    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, repr(s) + ' is not a string'
    assert ' ' in s, repr(s) + ' does not include a space'
    space = introcs.find_str(s, ' ')
    return s[:space]


def after_space(s):
    """
    Returns the substring of s after the first space
    
    Example: after_space('Hello World') returns 'World'
    
    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, repr(s) + ' is not a string'
    assert ' ' in s, repr(s) + ' does not include a space'
    space = introcs.find_str(s, ' ')
    return s[space+1:]


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert type(s) == str, repr(s) + ' is not a string'
    assert introcs.count_str(s, '"') >= 2, repr(s) + (' does not contain \
                                                      enough double quotes')
    quoteOne = introcs.find_str(s, '"')
    quoteTwo = introcs.find_str(s, '"', quoteOne+1)
    return s[quoteOne+1:quoteTwo]


def get_src(json):
    """
    Returns the src value in the response to a currency query.
    
    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'
    
    then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
    On the other hand if the json is 
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'
    
    then this function returns the empty string.
    
    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
        
    is also valid (in addition to the examples above).
    
    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str
    start = introcs.find_str(json, '"src"')
    src = first_inside_quotes(json[start+5:])
    return src


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.
    
    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is
       
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'
    
    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is 
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str
    start = introcs.find_str(json, '"dst"')
    dst = first_inside_quotes(json[start+5:])
    return dst


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.
    
    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is
        
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'
    
    then this function returns True (It does NOT return the error message 
    'Source currency code is invalid'). On the other hand if the json is 
        
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'
    
    then this function returns False.
    
    The web server does NOT specify the number of spaces after the colons. The JSON
        
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
        
    is also valid (in addition to the examples above).
    
    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str
    return 'false' in json


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.
    
    A currency query converts amt money in currency src to the currency dst. The response 
    should be a string of the form
    
    '{"success": true, "src": "<src-amount>", "dst": "<dst-amount>", "error": ""}'
        
    where the values src-amount and dst-amount contain the value and name for the src 
    and dst currencies, respectively. If the query is invalid, both src-amount and 
    dst-amount will be empty, and the error message will not be empty.
    
    There may or may not be spaces after the colon.  To test this function, you should
    choose specific examples from your web browser.
    
    Parameter src: the currency on hand
    Precondition: src is a nonempty string with only letters
    
    Parameter dst: the currency to convert to
    Precondition: dst is a nonempty string with only letters
    
    Parameter amt: amount of currency to convert
    Precondition: amt is a float or int
    """
    assert type(src) == str, repr(src) + ' is not a string'
    assert type(dst) == str, repr(dst) + ' is not a string'
    assert type(amt) == float or type(amt) == int, repr(amt) + (' is not a \
                                                                float or int')
    assert len(src) > 0, repr(src) + ' is an empty string'
    assert len(dst) > 0, repr(dst) + ' is an empty string' 
    assert introcs.isalpha(src) == True, repr(src) + ' contains numbers'
    assert introcs.isalpha(dst) == True, repr(dst) + ' contains numbers'
    query = ('https://ecpyfac.ecornell.com/python/currency/fixed?src='+src+
             '&dst='+dst+'&amt='+str(amt)+'&key='+APIKEY)
    return introcs.urlread(query)


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert currency != '', repr(currency) + ' is not populated'
    assert introcs.isalpha(currency) == True, repr(currency) + ' contains numbers'
    query = ('https://ecpyfac.ecornell.com/python/currency/fixed?src='+currency+
             '&dst='+currency+'&amt=0&key='+APIKEY)
    query_return = introcs.urlread(query)
    return 'true' in query_return


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.
    
    In this exchange, the user is changing amt money in currency src to the currency 
    dst. The value returned represents the amount in currency currency_to.
    
    The value returned has type float.
    
    Parameter src: the currency on hand
    Precondition: src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition: dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float or int
    """
    assert type(amt) == float or type(amt) == int, repr(amt) + (' is not a \
                                                                float or int')
    assert type(src) == str, repr(src) + ' is not a string'
    assert type(dst) == str, repr(dst) + ' is not a string'
    assert iscurrency(src), repr(src) + ' is not a valid currency code'
    assert iscurrency(dst), repr(dst) + ' is not a valid currency code'
    response = service_response(src, dst, amt)
    destination = get_dst(response)
    return float(before_space(destination))