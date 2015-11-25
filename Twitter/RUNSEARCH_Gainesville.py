from twitter_KR_V2_0 import searchTwitter
FileOut="/home/satbeer/twitter/twitGainesville"

Qs = [u'Gainesville', u'Cellon Oak Park', u'Stage 7 KTV', u'Living History Farm at Morningside Nature Center', u'Alachua County Visitors & Convention Bureau', u'Matheson Museum', u'Florida National Scenic Trail', u'Prairie Creek Preserve', u'Dogwood Park', u'Bluefield Estate Winery', u'Auto-Plus Raceway', u'The Oaks Mall', u'Historic Haile Homestead', u'Sweetwater Wetlands Park', u'Stephen C. O\'Connell Center', u'Kanapaha Park', u'Thomas Center', u'Swamp Head Brewery', u'Santa Fe College Teaching Zoo', u'Samuel P. Harn Museum of Art', u'Ben Hill Griffin Stadium', u'University of Florida', u'Paynes Prairie', u'University of Florida Bat House', u'Kanapaha Botanical Gardens', u'Devil\'s Millhopper Geological State Park', u'Florida Museum of Natural History', u'Butterfly Rainforest', u'Metro Diner', u'Papa John\'s', u'Arby\'s', u'New China Restaurant', u'Beque Holic', u'Cracker Barrel', u'Chomps Sports Grill', u'Mark\'s Prime Steakhouse', u'Northwest Grille', u'Bakery Mill and Deli', u'Ballyhoo Grill', u'Hogan\'s Great Sandwiches', u'David\'s Real Pit BBQ', u'Bubbaques', u'Big Lou\'s Pizzeria', u'BillyBobz BarBQ', u'Subway', u'Croutons', u'Hardee\'s', u'Moe\'s Southwest Grill', u'Durty Nelly\'s Irish Pub', u'Balls', u'Wingstop', u'Pizza Hut', u'BurgerFi', u'Panda Express', u'Heavenly Ham', u'The Red Onion Neighborhood Grill', u'First Wok', u'Panda Express', u'Clock Restaurant', u'Georges at Phil-Nicks', u'Chunky\'s Grill & Fry Co.', u'Szechuan Panda II', u'McDonald\'s', u'El Indio', u'Shands Terace Cafe', u'El Indio', u'Hot Wok', u'Wendy\'s', u'Good Fortune', u'Domino\'s Pizza', u'Wendy\'s', u'The Pita Pit', u'Subway', u'Ihop', u'Bagels & Noodles', u'Subway', u'McDonald\'s', u'Curia On The Drag', u'Pizza Hut', u'Shands', u'Perkins Family Restaurant & Bakery', u'Gator Tales', u'The Atlantic', u'Larry\'s Giant Subs', u'Asian Wok & Grill', u'Cheese Daddy', u'Stevi B\'s Pizza Buffet', u'China King', u'Caribbean Spice Inc', u'have only had one thing there,', u'but it\'s great', u'Caribbean Spice Inc', u'Chick-fil-A', u'Waffle House', u'Einstein Bros', u'The Coop', u'Fuji Sushi', u'Asian Chao', u'Steamers', u'Sub Stop Cafe', u'IHOP', u'Asian Star', u'Tailwinds', u'Wendy\'s', u'Cacciatore Pizza', u'Burgers4u', u'California Chicken Grill', u'Maki of Japan', u'Cheese Daddy', u'TGI Friday\'s', u'Arredondo Room', u'Golden Budda Restaurant', u'Zaxby\'s', u'Firehouse Subs', u'Charleys Philly Steaks', u'Cafe Colette', u'Lunch Box', u'The Laboratory', u'Tatu', u'Saigon Legend Restaurant', u'China 88 Restaurant', u'Falafel King Sandwiches', u'Applebee\'s', u'Burger King', u'Panda Express', u'Hungry Howie\'s Pizza', u'Wing Zone', u'Designer Greens', u'Domino\'s Pizza', u'Marco\'s Pizza', u'Wendy\'s', u'Papa John\'s', u'Court Of Heros', u'Shuck', u'Bella Caffe North Florida Regional', u'Arby\'s', u'China I', u'Munchies 420 Cafe', u'New China', u'El Norteno', u'KFC', u'Ker\'s Winghouse', u'McDonald\'s', u'Saigon Cafe', u'Definitely my favorite restaurant in Gainesville.', u'Saigon Cafe', u'Sonic Drive-In', u'Emiliano\'s Cafe', u'Adam\'s Rib Company', u'Southern Charm Kitchen', u'Yummy House Gainesville', u'Gator Suyaki', u'La Tienda Latina', u'Harry\'s Seafood Bar & Grille', u'Cymply Fresh', u'Blue Gill', u'Swamp Head Brewery', u'East End Eatery', u'Francesca\'s Trattoria', u'Napolatano\'s', u'Pomodoro Cafe', u'Dragonfly Sushi & Sake Co Incorporated', u'Amelia\'s', u'Blaze Pizza', u'Reggae Shack Cafe', u'La Pasadita', u'The Hyppo Gourmet Ice Pops', u'Satchel\'s Pizza', u'Manuel\'s Vintage Room', u'Bangkok Square', u'La Fiesta Mexican Restaurant', u'Daily Green', u'Piesano\'s Stone Fired Pizza', u'101 Downtown', u'Sonny\'s BBQ', u'Embers Wood Grill', u'Copper Monkey Restaurant', u'Paramount Grill', u'43rd Street Deli', u'The HoneyBaked Ham Company', u'Bageland', u'Sababa UF', u'Sweet Mel\'s', u'McAlister\'s Deli', u'Sandwich Inn', u'Bistro 1245', u'Fork & Pasta', u'Cairo Grille', u'Vellos Historic Brickstreet Grill', u'Moe\'s Southwest Grill', u'Maui Teriyaki', u'Burrito Brothers Taco Co.', u'Mac\'s Drive Thru', u'New Deal Cafe', u'Leonardo\'s Pizza In A Pan', u'Sushi Chao', u'Tall Paul\'s Brew House', u'Andaz Indian Restaurant', u'Jason\'s Deli', u'Mildred\'s Big City Food', u'Chop Stix Bistro', u'McAlister\'s Deli', u'Bento Cafe', u'Pho Ha Noi', u'Hong Kong Deli', u'2-Bits Lounge', u'Popeyes Louisiana Kitchen', u'Miraku Japanese Steakhouse', u'Outback Steakhouse', u'Gator Dockside', u'Maude\'s Classic Cafe', u'Haile Village Bistro', u'Metro Diner', u'La Fiesta Mexican Restaurant', u'Mother\'s Pub & Grill', u'The Pita Pit', u'Gyro Plus', u'Boca Fiesta', u'Warehouse Restaurant', u'Wholly Bbq', u'Five Guys', u'Sawamura Japanese Steakhouse', u'Chipotle Mexican Grill', u'Papa John\'s', u'Larry\'s Giant Subs', u'Oak', u'Taste of Saigon II', u'Ruby\'s', u'Gainesville House of Beer', u'Burrito Famous', u'Which Wich', u'Gator City Sports Grill', u'Miya Sushi', u'La Familia', u'Ruby Tuesdays', u'Mr Han\'s Restaurant & Night', u'Formaggio\'s Bistro & Wine Bar', u'Lolli Cup', u'Sushi-2-Go', u'Yamato Japanese Steakhouse', u'Red Robin Gourmet Burgers', u'Chipotle Mexican Grill', u'Five Star Pizza', u'Waffle House', u'The Spot', u'Sugarcreek Restaurant', u'Ocean Buffet', u'Ichiban Sushi', u'The Fat Tuscan', u'Liquid Ginger', u'Blue Agave Mexican Restaurant', u'Panera Bread', u'Krishna Lunch', u'Winghouse of Gainesville', u'Relish Downtown', u'Tempo Bistro To Go', u'Opus Cafe', u'Lakeside Bar & Grill', u'Swamp Restaurant', u'Public and General', u'Chick-fil-A', u'Italian Gator', u'The Vine', u'Olive Garden', u'101 Cantina', u'Chili\'s Grill & Bar', u'Pollo Tropical', u'PDQ Gainesville', u'Patticakes', u'Zaxby\'s', u'Zoe\'s Kitchen', u'Bento', u'Chopstix Cafe', u'Firehouse Subs', u'Steak \'n Shake', u'Mahzu Sushi & Grill', u'Rice Thai Sushi & Asian Fusion', u'Miller\'s Gainesville Ale House', u'Pepper\'s Mexican Grill and Cantina', u'Steak \'n Shake', u'Cafe C', u'Loosey\'s', u'Harvest Thyme Cafe', u'Mi Apa Latin Cafe', u'Leonardo\'s Pizza by the Slice', u'Chuy\'s', u'Crane Ramen', u'Wah Ha Ha', u'The Jones B-Side', u'D\'Lites Emporium', u'Tijuana Flats', u'43rd Street Deli and Breakfast House', u'Wine & Cheese Gallery', u'Piesano\'s Stone Fired Pizza', u'Texas Roadhouse', u'Sonny\'s BBQ', u'Volcanic Sushi & Sake', u'Tijuana Flats', u'Sweetberries', u'Garlic & Ginger', u'Sushi Matsuri Japanese Restaurant', u'Mojo Hogtown Bar-B-Que', u'4Rivers Smokehouse', u'Square 1 Burgers & Bar', u'Civilization', u'Leonardo\'s 706', u'Bonefish Grill Gainsville', u'Jimmy John\'s', u'Mexico Lindo Restaurant', u'Indian Cuisine', u'La Aurora Latin Market', u'Sonny\'s Real Pit Bar B Q', u'Metro Diner', u'Piesano\'s Stone Fired Pizza', u'Cedar River Seafood', u'Red Lobster', u'Cafe C', u'Las Margaritas', u'Panera Bread', u'Loosey\'s', u'Flacos', u'China Wok', u'Brass Tap', u'BJ\'s Restaurant and Brewhouse', u'Wahoo Seafood Grill', u'Ameraucana Wood Fire', u'The Flying Biscuit Cafe', u'Jersey Mike\'s Subs', u'Carrabba\'s Italian Grill', u'The Gelato Company and Artisan Deli', u'Vegan2go', u'Peach Valley Cafe', u'Kabab House', u'Adam\'s Rib Company', u'Gators Den Sports Grill', u'Bono\'s Pit Bar-B-Q', u'Humble Pie', u'Waffle House', u'Po\' Boys Seafood & Grill', u'Opus Cafe', u'Rockeys Dueling Piano Bar', u'Baker Baker', u'Lillian\'s Music Store', u'Crafty Bastards', u'Wok N Roll', u'Gumby\'s Pizza', u'One Love Cafe', u'Bagels Unlimited', u'China Star', u'Panda Express', u'Boston Market', u'The Midnight', u'Sugar Creek Restaurant', u'Relish', u'Subway', u'Beef O\'Brady\'s', u'Camellia Court Cafe', u'Sandy\'s Place', u'Lime Rock Road Neighborhood Grill']

for q in Qs:
    Request={'q':q,'result_type':'recent','count':100,'include_entities':'true'}
    searchTwitter(Request,FileOut,'ru')