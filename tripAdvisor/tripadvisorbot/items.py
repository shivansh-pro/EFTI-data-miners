from scrapy.item import Item, Field

# Default item
class Website(Item):

	name = Field()
	description = Field()
	url = Field()


# TripAdvisor items
class TripAdvisorItem(Item):
    
    itype = Field()
    url = Field()
    name = Field()
    address = Field()
    avg_stars = Field()
    photos = Field()
    reviews = Field() 
    tags = Field()
    user = Field()

class TripAdvisorAddressItem(Item):
    region = Field()
    extended_add = Field()
    street = Field()
    postal_code = Field()
    locality = Field()
    country = Field()


class TripAdvisorPhotoItem(Item):
	# URL to image.
	url = Field()
	
class TripAdvisorReviewItem(Item):

	date = Field()
	title = Field()
	description = Field()
	stars = Field()
	helpful_votes = Field()
	user = Field()

class TripAdvisorUserItem(Item):

	url = Field()
	name = Field()
	address = Field()
 
class UserItem(Item):
    name = Field()
    profileURL = Field()
    location = Field()
    numReviews = Field()
    numRatings = Field()
    age = Field()
    gender = Field()
    style = Field()
        
    
