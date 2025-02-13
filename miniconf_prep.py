from scripts.calendar_csv2ics import calendar_csv2ics
from scripts.calendar_ics2json import calendar_ics2json
from scripts.remove_private_details import remove_author_contacts

# Step1: Create Slack channels and zoom meetings

# Step2: Create sitedata for miniconf without author/presenter credentials.
remove_author_contacts()

# Step3: Prepare for calendar
# If links from schedule are not redirecting to the right page, check this code
calendar_csv2ics()
calendar_ics2json()

# Prepare for tutorials
# 1. Go to /static/tutorials
# 2. Update the tutorial content as seen in the tut_X.md files.
# 3. Add/Remove tut_X.md files as necessary. Make sure they are consecutive in number



