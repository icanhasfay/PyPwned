PyPwned
======
[![Build Status](https://travis-ci.org/icanhasfay/PyPwned.svg)](https://travis-ci.org/icanhasfay/PyPwned)

A Python client for the HaveIBeenPwned REST API. https://haveibeenpwned.com/

Installation
-----
```pip install pypwned```

Requires
-----
  * requests
  * pyOpenSSL
  * ndg-httpsclient
  * pyasn1

Usage
-----

### Breaches


#### Getting all breaches for an account

##### Get all breaches for an account across all domains. 

```
import pypwned
print pypwned.getAllBreachesForAccount(email="foo@bar.com")
```

##### Get all breaches for an account across a specific domain. 

```
import pypwned
print pypwned.getAllBreachesForAccount(email="foo@bar.com",domain="adobe.com")
```


#### Getting all breached sites in the system

##### Return the details of each breach in the system.

```
import pypwned
print pypwned.getAllBreaches()
```

##### Return the details of each breach associated with a specific domain.

```
import pypwned
print pypwned.getAllBreaches(domain="adobe.com")
```

#### Getting a single breached site

Return the details of a single breach, by breach name.

```
import pypwned
print pypwned.getSingleBreachedSite(name="adobe")
```

#### Getting all data classes in the system

Return the different types of data classes that are associated with a record in a breach. E.G, Email addresses and passwords

```
import pypwned
print pypwned.getAllDataClasses()
```

### Pastes


#### Getting all pastes for an account

Return any pastes that contain the given email address

```
import pypwned
print pypwned.getAllPastesForAccount(account="foo@bar.com")
```

