# LinkedIn API - Find Jobs by Filtering

Wrapper for linkedin-api by [tomquirk](https://github.com/tomquirk).
Contains helper functions for Linkedin API for the job search, allows you to filter by title.

## Installation

Using **Python >= 3.6**, we will need to install both linkedin-jobs-filter and linkedin-api libraries:
```
$ pip install -e git+https://github.com/kais-viz/linkedin-jobs-filter.git
```
*temporary: loading linkedin-api from kais-viz copy as it contains the search_jobs function*
```
$ pip install -e git+https://github.com/kais-viz/linkedin-api.git
```

### Example usage

```python
from linkedin_jobs import * as lj
from linkedin_api import Linkedin

# Authenticate using any Linkedin account credentials
api = Linkedin('reedhoffman@linkedin.com', 'iheartmicrosoft')

# Do a job search using linkedin_api library
jobs = api.search_jobs("data scientist OR data analyst", 
						location = "Germany", 
						count = 5)

# Clean the json data returned
clean_jobs = lj.get_jobs_list(jobs)
```

*In development, code coming soon.*
