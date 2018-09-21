# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
#import lxml.html
from lxml import html
#


# # Read in a page

product_id = "sssdtosxg51tbpci"
product_name = "Toshiba XG5"

cexurl = "https://uk.webuy.com/product-detail/?id="

#html = scraperwiki.scrape("https://uk.webuy.com/product-detail/?id=sssdtosxg51tbpci")

#url = "https://uk.webuy.com/product-detail/?id=sssdtosxg51tbpc"
#doc_text = scraperwiki.scrape(url)
#doc = html.fromstring(doc_text)

# # Find something on the page using css selectors


#root = lxml.html.fromstring(html)
#root.cssselect("<span style="line-height: 17px !important; margin: 1px 1px 3px;")
#
# # Write out to the sqlite database using scraperwiki library

#scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})

url = "http://www-news.iaea.org/EventList.aspx"
doc_text = scraperwiki.scrape(url)
doc = html.fromstring(doc_text)
               
for row in doc.cssselect("#tblEvents tr"):
    link_in_header = row.cssselect("h4 a").pop()
    event_title = link_in_header.text
    print event_title               
               
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
