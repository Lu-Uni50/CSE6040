import re

# s = 'JKRowling@Huge-Books.org'

# Testing valid email: 'richie@cc.gatech.edu'
# Testing valid email: 'bertha_hugely@sampson.edu'

# def parse_email (s):
#     pattern = re.compile(r'''^            # Beginning of string
#                             ([a-zA-Z]+[A-Za-z._\-+]+)    # user name
#                             \@            # @
#                             ([A-Za-z.\-_]+[a-zA-Z]+)    # domain
#                             $              # End of string
#                             ''',
#                             re.VERBOSE)

#     if pattern.match(s):
#         return pattern.match(s).groups()
    
#     raise ValueError

# print(parse_email(s))

# def parse_phone1 (s):
    # pattern = re.compile(r'''^                              # Beginning of string
    #                         \s*       # spaces
    #                         (\([0-9]{3,3}\))    # area number
    #                         \s*            # spaces
    #                         ([0-9]{3,3})      # local number - 3 digits
    #                         \-
    #                         ([0-9]{4,4})       # local number - 4 digits
    #                         $                               # End of string
    #                         ''',
    #                         re.VERBOSE)

#     if pattern.match(s):
#         return pattern.match(s).groups()
#     raise ValueError

# s = '(404) 121-2121'
# print(parse_phone1(s))
s = '''
 </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="eG-UO83g_5zDk70FIJbm2w" data-key="2" data-component-bound="true">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/south-city-kitchen-midtown-atlanta-2?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="South City Kitchen - Midtown" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(3).jpg" srcset="https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/180s.jpg 2.00x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/ms.jpg 1.11x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/120s.jpg 1.33x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/168s.jpg 1.87x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/ls.jpg 2.78x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">2.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/south-city-kitchen-midtown-atlanta-2?osq=fried+chicken" data-hovercard-id="tvYceAR7TJ7zS6N6kF5y8g"><span>South City Kitchen - Midtown</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4-half rating-large" title="4.5 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.5 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            1777 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=southern&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Southern</a>,
                    <a href="https://www.yelp.com/search?cflt=breakfast_brunch&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Breakfast &amp; Brunch</a>,
                    <a href="https://www.yelp.com/search?cflt=gluten_free&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Gluten-Free</a>
    </span>


    </div>


                        <ul class="search-result_tags">
            <li class="tag-18x18_menu-black">
                <small>
                    <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-menu icon--size-18 icon--black">
    <svg class="icon_svg">
        <use xlink:href="#18x18_menu"></use>
    </svg>
</span>

                    On the menu: Springer Mountain Farms <span class="highlighted">Fried</span> <span class="highlighted">Chicken</span>
                </small>
                
            </li>
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                            <span class="neighborhood-str-list">
            Midtown        </span>

                <address>
        1144 Crescent Ave NE<br>Atlanta, GA 30309
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 873-7358
    </span>

        </div>
    </div>
    
 </div>


                </li>
                <li class="regular-search-result">
                                <div class="search-result natural-search-result" data-biz-id="eG-UO83g_5zDk70FIJbm2w" data-key="2" data-component-bound="true">
            <div class="biz-listing-large">
        <div class="main-attributes">
            <div class="media-block media-block--12">
                <div class="media-avatar">
                                    <div class="photo-box pb-90s">
                <a href="https://www.yelp.com/biz/south-city-kitchen-midtown-atlanta-2?osq=fried+chicken" class="js-analytics-click" data-analytics-label="biz-photo">
                <img alt="South City Kitchen - Midtown" class="photo-box-img" height="90" src="./Best Fried chicken in Atlanta, GA - Yelp_files/90s(3).jpg" srcset="https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/180s.jpg 2.00x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/ms.jpg 1.11x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/120s.jpg 1.33x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/168s.jpg 1.87x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/ls.jpg 2.78x,https://s3-media1.fl.yelpcdn.com/bphoto/cqDbJPa7Q2OqOce6Snn3qQ/258s.jpg 2.87x" width="90">

        </a>

    </div>




                </div>
                <div class="media-story">
                    <h3 class="search-result-title">
                                    <span class="indexed-biz-name">2.         <a class="biz-name js-analytics-click" data-analytics-label="biz-name" href="https://www.yelp.com/biz/south-city-kitchen-midtown-atlanta-2?osq=fried+chicken" data-hovercard-id="tvYceAR7TJ7zS6N6kF5y8g"><span>South Cieiejkd - Midtown</span></a>
</span>


                    </h3>
                    
                                <div class="biz-rating biz-rating-large clearfix">
                



    <div class="i-stars i-stars--regular-4-half rating-large" title="4.5 star rating">
        <img class="offscreen" height="303" src="./Best Fried chicken in Atlanta, GA - Yelp_files/stars.png" width="84" alt="4.5 star rating">
    </div>


                    <span class="review-count rating-qualifier">
            1999 reviews
    </span>

        </div>


                            <div class="price-category">
                <span class="bullet-after">
            
        <span class="business-attribute price-range">$$</span>
        </span>
            <span class="category-str-list">
                    <a href="https://www.yelp.com/search?cflt=southern&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Southern</a>,
                    <a href="https://www.yelp.com/search?cflt=breakfast_brunch&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Breakfast &amp; Brunch</a>,
                    <a href="https://www.yelp.com/search?cflt=gluten_free&amp;find_desc=fried+chicken&amp;find_loc=Atlanta%2C+GA">Gluten-Free</a>
    </span>


    </div>


                        <ul class="search-result_tags">
            <li class="tag-18x18_menu-black">
                <small>
                    <span aria-hidden="true" style="width: 18px; height: 18px;" class="icon icon--18-menu icon--size-18 icon--black">
    <svg class="icon_svg">
        <use xlink:href="#18x18_menu"></use>
    </svg>
</span>

                    On the menu: Springer Mountain Farms <span class="highlighted">Fried</span> <span class="highlighted">Chicken</span>
                </small>
                
            </li>
    </ul>

                </div>
            </div>
        </div>

        <div class="secondary-attributes">
                            <span class="neighborhood-str-list">
            Midtown        </span>

                <address>
        1144 Crescent Ave NE<br>Atlanta, GA 30309
    </address>


            
    <span class="offscreen">Phone number</span>
    <span class="biz-phone">
        (404) 873-7358
    </span>

        </div>
    </div>

    
'''

# pattern = re.compile(r'''
#                      <span class=\"indexed-biz-name\">(?P<rank>\d*)
#                      [\s\S]*
#                      <span>(?P<name>.*)</span>
#                      [\s\S]*
#                      title=\"(?P<stars>.*)star rating\">
#                      [\s\S]*
#                      <span class=\"review-count rating-qualifier\">[\s\n]*(?P<numrevs>\d+)\sreviews
#                      [\s\S]*
#                      <span class=\"business-attribute price-range\">(?P<price>.*)</span>
#                      ''',
#                     re.VERBOSE)

regex = r"<span class=\"indexed-biz-name\">(?P<rank>\d*)[\s\S]*<span>(?P<name>.*)</span>[\s\S]*title=\"(?P<stars>.*)\sstar rating\">[\s\S]*<span class=\"review-count rating-qualifier\">[\s\n]*(?P<numrevs>\d+)\sreviews[\s\S]*<span class=\"business-attribute price-range\">(?P<price>.*)</span>"

matches = re.finditer(regex, s)

rankings = []
for match in matches:
    ranking = {}  
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    for groupNum in range(0, len(match.groups())):
        ranking['name'] = match.group('name')
        ranking['stars'] = match.group('stars')
        ranking['numrevs'] = int(match.group('numrevs'))
        ranking['price'] = match.group('price')
        
    rankings.append(ranking)
    
print(rankings)

# if pattern.match(s):
#         print(pattern.match(s))
# else:
#     print("nah")

# rankings = {}
# for i in range(10):
#     rankings[i] = {}
#     rankings[i]['name'] = 

# '''
# '<span\\sclass=\"indexed-biz-name\">(?P<rank>\\d*)
#     [\\s\\S]*?
#         <span>(?P<name>[\\s\\S]*?)</span>
#         </a>[\\s\\S]*?
#         (?P<stars>\\d\\.\\d)
#         [\\s\\S]*?
#         (?P<numrevs>\\d*)\\sreviews
#         [\\s\\S]*?
#         ge\">
#         (?P<price>[\\s\\S]*?)
# </span>'
# '''