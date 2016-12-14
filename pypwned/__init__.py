__author__ = 'Eric Fay'
__version__ = "0.1.5"


import requests
import json
import re

baseAPIURL = "https://haveibeenpwned.com/api/v2/"


fourHundredString = "400 - Bad request - the account does not comply with an acceptable format (i.e. it's an empty string)"
fourOThreeString = "403 - Forbidden - no user agent has been specified in the request"
fourOFourString = "404 - Not found - the account could not be found and has therefore not been pwned"
fourTwentyNineString = "Rate limit exceeded, refer to acceptable use of the API: https://haveibeenpwned.com/API/v2#AcceptableUse"
fiveHundredString = "A server error occurred on haveibeenpwned.com. Please try again later."
emailFormatString = "The provided string is not an email address"


def getAllBreachesForAccount(email, domain=""):
    # Pattern is a derivation of RFC-5322
    # Grabbed from http://www.regular-expressions.info/email.html
    pattern = re.compile(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
    if not pattern.match(email):
        return emailFormatString
    urlEndpoint = "breachedAccount/"
    if domain == "":
        urlToFetch = baseAPIURL+urlEndpoint+email
        r = requests.get(urlToFetch, verify=True)
        if r.status_code == 400:
            return fourHundredString
        elif r.status_code == 403:
            return fourOThreeString
        elif r.status_code == 404:
            return fourOFourString
        elif r.status_code == 429:
            return fourTwentyNineString
        elif r.status_code >= 500:
            return fiveHundredString
        else:
            return r.json()
    else:
        domainParams = "?domain="+domain
        urlToFetch = baseAPIURL+urlEndpoint+email+domainParams
        r = requests.get(urlToFetch, verify=True)
        if r.status_code == 400:
            return fourHundredString
        elif r.status_code == 403:
            return fourOThreeString
        elif r.status_code == 404:
            return fourOFourString
        elif r.status_code == 429:
            return fourTwentyNineString
        elif r.status_code >= 500:
            return fiveHundredString
        else:
            return r.json()


def getAllBreaches(domain=""):
    urlEndpoint = "breaches/"
    if domain == "":
        urlToFetch = baseAPIURL+urlEndpoint
        r = requests.get(urlToFetch, verify=True)
        return r.json()
    else:
        domainParams = "?domain="+domain
        urlToFetch = baseAPIURL+urlEndpoint+domainParams
        r = requests.get(urlToFetch, verify=True)
        if r.status_code == 400:
            return fourHundredString
        elif r.status_code == 403:
            return fourOThreeString
        elif r.status_code == 404:
            return fourOFourString
        elif r.status_code == 429:
            return fourTwentyNineString
        elif r.status_code >= 500:
            return fiveHundredString
        else:
            return r.json()


def getSingleBreachedSite(name):
    urlEndpoint = "breach/"
    urlToFetch = baseAPIURL+urlEndpoint+name
    r = requests.get(urlToFetch, verify=True)
    if r.status_code == 400:
        return fourHundredString
    elif r.status_code == 403:
        return fourOThreeString
    elif r.status_code == 404:
        return fourOFourString
    elif r.status_code == 429:
        return fourTwentyNineString
    elif r.status_code >= 500:
        return fiveHundredString
    else:
        return r.json()


def getAllDataClasses():
    urlEndpoint = "dataclasses/"
    urlToFetch = baseAPIURL+urlEndpoint
    r = requests.get(urlToFetch, verify=True)
    if r.status_code == 400:
        return fourHundredString
    elif r.status_code == 403:
        return fourOThreeString
    elif r.status_code == 404:
        return fourOFourString
    elif r.status_code == 429:
        return fourTwentyNineString
    elif r.status_code >= 500:
        return fiveHundredString
    else:
        return r.json()


def getAllPastesForAccount(account):
    urlEndpoint = "pasteaccount/"
    urlToFetch = baseAPIURL+urlEndpoint+account
    r = requests.get(urlToFetch, verify=True)
    if r.status_code == 400:
        return fourHundredString
    elif r.status_code == 403:
        return fourOThreeString
    elif r.status_code == 404:
        return fourOFourString
    elif r.status_code == 429:
        return fourTwentyNineString
    elif r.status_code >= 500:
        return fiveHundredString
    else:
        return r.json()
