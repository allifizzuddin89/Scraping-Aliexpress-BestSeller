import scrapy
from scrapy import Request
from scrapy.shell import inspect_response
from pprint import pprint


class MainSpider(scrapy.Spider):
    name = "main"
    # allowed_domains = ["x"]
    # start_urls = ["http://x/"]

    # specify which response codes the spider is able to handle
    handle_httpstatus_list = [404]

    # begin with page 1
    page_no = 1
    find_item = 'iphone repair kit'
    find_item = find_item.replace(' ','-')

    # General url for searching specific item, url below
    # sorttype=total_tranpro_desc, sort by orders
    # sorttype=price_asc, sort by price ascending
    # sorttype=price_desc, sort by price descending
    # Btw, you might replace the url as you wish acording to your preferred category

    url = "https://www.aliexpress.com/w/wholesale-{0}.html?sorttype=total_tranpro_desc&d=y&page={1}"
    
    #nav-global > div.ng-item-wrap.ng-item.ng-switcher > div > div > div > div.switcher-language.item.util-clearfix > div > ul > li:nth-child(1) > a
    headers = {
        'authority': 'acs.aliexpress.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ms;q=0.8,id;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ali_apache_id=33.1.244.149.1680800431938.231149.8; intl_locale=en_US; xman_f=22ODYBEvJ0wtmXNt74qYsbgfR4vK1oTZIuqxTFiFCfe3ToJ9ZG9qt80HrH3RJ1whWuQIqtaXgk3s7IXOZ1blLUULviDDQl50L0DWVx9n+FSp/mvHl6rBpA==; acs_usuc_t=x_csrf=naf3thmd9fi9&acs_rt=e3b68f14f01d4b038b8e99f5b4538f7c; xman_t=uEpONyu0YMTjN2NVgK3ayykToyPgehgYakDrrMGMlnXAn5vPtkkVAatbMONOvqt5; aep_usuc_f=site=glo&c_tp=MYR&region=MY&b_locale=en_US; cna=wei1HJCBvFECAXOkUYyLc+bc; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=0&acs_rt=e3b68f14f01d4b038b8e99f5b4538f7c; _gcl_au=1.1.827289287.1680800453; _ga=GA1.1.1760922766.1680800453; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005001613063919%091005003245182094; intl_common_forever=9i5BD4w656t86zYcI7asSSuYuVZeq2UfTKCpbnG9HfaNRh7Di53Niw==; AKA_A2=A; _ga_VED1YSGNC7=GS1.1.1680809652.3.0.1680809652.0.0.0; _m_h5_tk=ed9884aa15d49be7bef4f53d861f664d_1680811633672; _m_h5_tk_enc=ddf8584c0b0b486e42549c5add817be0; isg=BExMGN6aRLC8r1BNrD7nJ7iWHaN-hfAvrYkJq6YNWPefMew7zpXAv0KH0TEJeSiH; tfstk=cYtNB0tH-zEB2o9xwMj2TSINNB1OZepMnkW5SjCcGTATb9QGiJFAKX_1LtwUiNf..; l=fBxEd2s7NS4YpqiwKOfwPurza77OSIRAguPzaNbMi9fP9w1HJ5MFW1inlVYMCnGNF6PBR3oVgDzMBeYBYIxSxioyyJvwWFHmn_vWSGf..',
        'dnt': '1',
        'origin': 'https://www.aliexpress.com',
        'referer': 'https://www.aliexpress.com/',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
    }

    def start_requests(self):
        # self.url.format(search-item,page number)
        yield Request(self.url.format(self.find_item, self.page_no),headers=self.headers, callback=self.parse_main_page)

    def parse_main_page(self, response):
        # inspect_response(response, self)
        url_lists = []
        url_lists_new = []
        url_lists = response.css('div.list--gallery--34TropR>a.manhattan--container--1lP57Ag::attr(href)').getall()
        i=0
        for j in url_lists:
            url_lists_new.append("https:"+j)
            print('\n',url_lists_new[i])
            i+=1
        
        yield Request(url=url_lists_new[0],headers=self.headers, callback=self.parse_sub_page)
        # url_list_new = "https:"+url_lists
        # url_lists_new = 'https:'.join(url_lists)
        # url_lists[0] = "https:"+url_lists[0]
        # print('\n',url_lists_new)
        # yield Request(url=url_list_new[0],headers=self.headers, callback=self.parse_sub_page)

    #     for url_list in url_lists:
    #         # item ={'url' : url_list.strip('//')}
    #         # yield item
    #         # print('\n', url_list.strip('//'))
            
    #         # url_list = url_list.strip('//')
    #         # missing https in the parsed link
    #         url_list_new = "https:"+url_list
    #         print('\n',url_list_new)
    #         yield Request(url=url_list_new,headers=self.headers, callback=self.parse_sub_page)
    # #         response.follow(url=url_list,headers=self.headers, callback=self.parse_sub_page)
    
    def parse_sub_page(self, response):
        # the data could be parsed in this page if we load java
        # so 2 options
        # 1. use scrapy-playwright to load java
        # 2. there is hidden json, in window.runParams, contains data
        # options no 2  dont require to load java
        inspect_response(response, self)
        # print('\nSUCCESS\n')
        # print('\n',response.css('div.product-title > h1.product-title-text::text')) 
        # item = {'name':response.css('div.product-title > h1.product-title-text::text').get()}
        # yield item