import re
import time

from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
from tripadvisorbot.items import *
from tripadvisorbot.spiders.crawlerhelper import *


MAX_REVIEWS_PAGES = 1000
class TripAdvisorAttractionsBaseSpider(BaseSpider):
    name = 'tripadvisor-attraction'


    allowed_domains = ["tripadvisor.com"]
    base_uri = "http://www.tripadvisor.com"
    start_urls = [
          base_uri + "/Attractions-g60805-Activities-Jacksonville_Florida.html",
          base_uri + "/Attractions-g60805-Activities-oa30-Jacksonville_Florida.html",
          base_uri + "/Attractions-g60805-Activities-oa60-Jacksonville_Florida.html",
          base_uri + "/Attractions-g60805-Activities-oa90-Jacksonville_Florida.html",
          base_uri + "/Attractions-g60805-Activities-oa120-Jacksonville_Florida.html"
    ]



    # Entry point for BaseSpider.
    # Page type: /Attractions
    def parse(self, response):
        tripadvisor_items = []
        sel = Selector(response)
        snode_attractions = sel.xpath('//div[@id="FILTERED_LIST"]/div/div[@class="element_wrap"]')
        print "Fetching data from:" + response.url
        #inspect_response(response, self)
        for snode in snode_attractions:
            tripadvisor_item = TripAdvisorItem()
            tripadvisor_item['url'] = self.base_uri + clean_parsed_string(get_parsed_string( snode, './/div[@class="property_title"]/a/@href'))
            tripadvisor_item['name'] = clean_parsed_string(get_parsed_string(snode, './/div[@class="property_title"]/a/text()'))
            tripadvisor_item['itype'] = "attractions"
            snode_restaurant_item_avg_stars = clean_parsed_string(get_parsed_string(snode, './/img[@class="sprite-ratings"]/@alt'))
            tripadvisor_item['avg_stars'] = snode_restaurant_item_avg_stars
            #re.match(r'(\S+)', snode_restaurant_item_avg_stars).group()
            yield Request(url=tripadvisor_item['url'], meta={'tripadvisor_item': tripadvisor_item}, callback=self.parse_attraction_page)
            tripadvisor_items.append(tripadvisor_item)


    def parse_attraction_page(self, response):

        print "Fetching data from:" + response.url
        tripadvisor_item = response.meta['tripadvisor_item']
        sel = Selector(response)
        #inspect_response(response, self)
        tripadvisor_address_item = TripAdvisorAddressItem()
        tripadvisor_address_item['street'] = clean_parsed_string(get_parsed_string(sel, '//address/span/span[@class="format_address"]/span[@class="street-address"]/text()'))
        tripadvisor_address_item['extended_add'] = clean_parsed_string(get_parsed_string(sel, '//address/span/span[@class="format_address"]/span[@class="extended-address"]/text()'))
        snode_address_postal_code = clean_parsed_string(get_parsed_string(sel, '//address/span/span[@class="format_address"]/span[@class="locality"]/span[@property="postalCode"]/text()'))
        if snode_address_postal_code:
            tripadvisor_address_item['postal_code'] = snode_address_postal_code

        snode_address_region = clean_parsed_string(get_parsed_string(sel, '//address/span/span[@class="format_address"]/span[@class="locality"]/span[@property="addressRegion"]/text()'))
        if snode_address_region:
            tripadvisor_address_item['region'] = snode_address_region

        tripadvisor_item['address'] = tripadvisor_address_item
        tripadvisor_item['tags'] = ",".join(response.selector.xpath('//div[@id="HEADING_GROUP"]//div[@class="detail"]/a/text()').extract())
        tripadvisor_item['reviews'] = []

        expanded_review_url = clean_parsed_string(get_parsed_string(sel, '//div[contains(@class, "review basic")]//a/@href'))
        if expanded_review_url:
            yield Request(url=self.base_uri + expanded_review_url, meta={'tripadvisor_item': tripadvisor_item, 'counter_page_review' : 0}, callback=self.parse_fetch_review)



    def parse_fetch_review(self, response):
        print "Fetching data from:" + response.url
        tripadvisor_item = response.meta['tripadvisor_item']
        sel = Selector(response)
        counter_page_review = response.meta['counter_page_review']
        #inspect_response(response, self)
        # Limit max reviews pages to crawl.
        if counter_page_review < MAX_REVIEWS_PAGES:
            counter_page_review = counter_page_review + 1

            # TripAdvisor reviews for item.
            snode_reviews = sel.xpath('//div[@id="REVIEWS"]/div/div[contains(@class, "review")]/div[@class="col2of2"]/div[@class="innerBubble"]')

            # Reviews for item.
            for snode_review in snode_reviews:
                tripadvisor_review_item = TripAdvisorReviewItem()

                tripadvisor_review_item['title'] = clean_parsed_string(get_parsed_string(snode_review, 'div[@class="quote"]/text()'))

                # Review item description is a list of strings.
                # Strings in list are generated parsing user intentional newline. DOM: <br>
                tripadvisor_review_item['description'] = get_parsed_string_multiple(snode_review, 'div[@class="entry"]/p/text()')
                # Cleaning string and taking only the first part before whitespace.
                snode_review_item_stars = clean_parsed_string(get_parsed_string(snode_review, 'div[@class="rating reviewItemInline"]/span[starts-with(@class, "rate")]/img/@alt'))
                tripadvisor_review_item['stars'] = re.match(r'(\S+)', snode_review_item_stars).group()

                snode_review_item_date = clean_parsed_string(get_parsed_string(snode_review, 'div[@class="rating reviewItemInline"]/span[@class="ratingDate"]/text()'))
                if snode_review_item_date:
                    snode_review_item_date = re.sub(r'Reviewed ', '', snode_review_item_date, flags=re.IGNORECASE)
                    snode_review_item_date = time.strptime(snode_review_item_date, '%B %d, %Y') if snode_review_item_date else None
                    tripadvisor_review_item['date'] = time.strftime('%Y-%m-%d', snode_review_item_date) if snode_review_item_date else None
                else:
                    tripadvisor_review_item['date'] = 'NONE'
                tripadvisor_item['reviews'].append(tripadvisor_review_item)


            # Find the next page link if available and go on.
            next_page_url = clean_parsed_string(get_parsed_string(sel, '//div[@class="unified pagination "]/a[contains(@class, "next")]/@href'))
            if next_page_url and len(next_page_url) > 0:
                yield Request(url=self.base_uri + next_page_url, meta={'tripadvisor_item': tripadvisor_item, 'counter_page_review' : counter_page_review}, callback=self.parse_fetch_review)
            else:
                yield tripadvisor_item
        #Limitatore numero di pagine di review da passare. Totale review circa 5*N.
        else:
            yield tripadvisor_item


    def parse_userDetauls(self, response):
        tripadvisor_item = response.meta['tripadvisor_item']
        sel = Selector(response)
        
        name = clean_parsed_string("".join(sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]//span[contains(@class, "nameText")]/text()').extract()[0]))
        location = clean_parsed_string("".join(sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]//div[contains(@class, "hometown")]/p/text()').extract()[0]))
        reviews = clean_parsed_string("".join(sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]//div[contains(@class, "member-points")]//a[@name="reviews"]/text()').extract()[0]))
        num_reviews = re.match('[0-9]*', reviews).group(0)
        ratings_str = clean_parsed_string("".join(sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]//div[contains(@class, "member-points")]//a[@name="ratings"]/text()').extract()[0]))
        num_ratings = re.match('[0-9]*', ratings_str)
        tags = sel.xpath('//div[@id="MODULES_MEMBER_CENTER"]//div[contains(@class, "tagBlock")]//div[contains(@class,"tagBubble")]/text()').extract()
        clean_tags = map(lambda tag: clean_parsed_string(tag), tags)
        
        user_item = UserItem()
        
        user_item['profileURL'] = response.url
        if name:
            user_item['name'] = name
        
        if location:
            user_item['location'] = location
        
        if num_reviews:
            user_item['numReviews'] = num_reviews
        
            
        if num_ratings:
            user_item['numRatings'] = num_ratings
        
        if clean_tags:
            user_item['style'] = clean_tags
            
        tripadvisor_item['user'].append(user_item)
        
        yield tripadvisor_item
        
        
