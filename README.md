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
> Note: The below examples assume you have loaded the envrionment variable HIBP_API_KEY with your appropriate Have I Been Pwned API key.
More details here, https://haveibeenpwned.com/API/Key.

### Breaches


#### Getting all breaches for an account

##### Get all breaches for an account across all domains. 

```
import pypwned, os
your_hibp_key = os.environ.get("HIBP_API_KEY")
pwny = pypwned.pwned(your_hibp_key)
pwny.getAllBreachesForAccount(email="foo@bar.com")
```

##### Get all breaches for an account across a specific domain. 

```
import pypwned, os
your_hibp_key = os.environ.get("HIBP_API_KEY")
pwny = pypwned.pwned(your_hibp_key)
pwny.getAllBreachesForAccount(email="foo@bar.com",domain="adobe.com")
```


#### Getting all breached sites in the system

##### Return the details of each breach in the system.

```
import pypwned, os
your_hibp_key = os.environ.get("HIBP_API_KEY")
pwny = pypwned.pwned(your_hibp_key)
pwny.getAllBreaches()
```

##### Return the details of each breach associated with a specific domain.

```
import pypwned, os
your_hibp_key = os.environ.get("HIBP_API_KEY")
pwny = pypwned.pwned(your_hibp_key)
pwny.getAllBreaches(domain="adobe.com")
```

#### Getting a single breached site

Return the details of a single breach, by breach name.

```
import pypwned, os
your_hibp_key = os.environ.get("HIBP_API_KEY")
pwny = pypwned.pwned(your_hibp_key)
pwny.getSingleBreachedSite(name="adobe")
```

#### Getting all data classes in the system

Return the different types of data classes that are associated with a record in a breach. E.G, Email addresses and passwords

```
import pypwned, os
your_hibp_key = os.environ.get("HIBP_API_KEY")
pwny = pypwned.pwned(your_hibp_key)
pwny.getAllDataClasses()
```

### Pastes


#### Getting all pastes for an account

Return any pastes that contain the given email address

```
import pypwned, os
your_hibp_key = os.environ.get("HIBP_API_KEY")
pwny = pypwned.pwned(your_hibp_key)
pwny.getAllPastesForAccount(account="foo@bar.com")
```

