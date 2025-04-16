
# Settings
import pandas as pd
from pynytimes import NYTAPI

# Initialize API with your key
nyt = NYTAPI("gXwtcT0f6RY3tXtqNAboQGePxCTGBDOq", parse_dates=True)


# Top Stories
top_stories = nyt.top_stories()

# Get all the top stories from a specific category
top_climate_stories = nyt.top_stories(section = "climate")


df_top_stories = pd.DataFrame(top_stories)
df_top_climate_stories = pd.DataFrame(top_climate_stories)



# Most Viewed
most_viewed = nyt.most_viewed()

# Get most viewed articles of last 7 or 30 days
most_viewed = nyt.most_viewed(days = 7)
most_viewed = nyt.most_viewed(days = 30)


from datetime import datetime

# Define the date range
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)

# Search articles related to climate within a date range
  # This return only up to 10 articles.
articles = nyt.article_search(
    query="climate",
    dates={"begin": start, "end": end},
)