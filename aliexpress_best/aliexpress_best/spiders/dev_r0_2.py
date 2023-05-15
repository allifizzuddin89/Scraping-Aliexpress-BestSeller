import scrapy
from scrapy import Request
import requests
import json
from  pprint import pprint
from scrapy.shell import inspect_response
from scrapy.exceptions import CloseSpider

class DevR02Spider(scrapy.Spider):
    name = "dev_r0_2"
    # allowed_domains = ["x"]
    # start_urls = ["http://x/"]

    url = 'https://www.aliexpress.com/fn/search-pc/index'
    
    # Key in search item in below
    search_text = "repair kit iphone"
    search_text_dash = search_text.replace(' ','-')
    search_text_plus = search_text.replace(' ','+')
    page_no = 1
    search_referer_value= f"https://www.aliexpress.com/w/wholesale-{search_text_dash}.html?d=y&page={page_no}&sorttype=total_tranpro_desc&SearchText={search_text_plus}&trafficChannel=main&g=y&sortType=total_tranpro_desc"
    

    headers = {
        "authority": "www.aliexpress.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,ms;q=0.8,id;q=0.7",
        "bx-v": "2.2.3",
        "content-type": "application/json;charset=UTF-8",
        "dnt": "1",
        "origin": "https://www.aliexpress.com",
        "referer": search_referer_value,
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Microsoft Edge\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Linux\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48"
    }

    cookies = {
        "ali_apache_id": "33.1.233.206.168165714556.220188.8",
        "XSRF-TOKEN": "dac9b48a-8d41-44d6-9481-899122bf78be",
        "intl_locale": "en_US",
        "xman_f": "2b+2kj2uR0eXgou5CgWhGpgphxdU5wAXdY+PVxuvcQmT848+4eMIqOAY7k5W2eq049i6QZn0XvfYUScJHK6x8ZDQlzxE6mdvwBx2SpH42Dg0VtjIJ/KtWw==",
        "acs_usuc_t": "x_csrf=t9qft2mgtajx&acs_rt=69f1d345386a41a38eca9650f129b7cf",
        "xman_t": "1OHyCkveGr/Y3fNBNWP8rktUOCSfElO1Aaj/15OsX31W23J2PTLonF7R1pI/ULgS",
        "aep_usuc_f": "site=glo&c_tp=MYR&region=MY&b_locale=en_US",
        "aep_history": "keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005004559525694",
        "xman_us_f": "x_locale=en_US&x_l=0&x_c_chg=0&acs_rt=69f1d345386a41a38eca9650f129b7cf",
        "cna": "Y/vCHBKJCQYCAXOkMwh5kRIh",
        "_gcl_au": "1.1.1374349958.1681657189",
        "_ga": "GA1.1.1945978505.1681657193",
        "_m_h5_tk": "f50ebfb538e6f439ddbeebcc11a8447b_1681665669021",
        "_m_h5_tk_enc": "449cfe8f525123048eb6187840f01cb6",
        "AKA_A2": "A",
        "JSESSIONID": "06B94F0DB668FA955FDC5CC4AB00231B",
        "intl_common_forever": "83SivZfHKM6YEGgFOKwPYc4eztw8UAsnADqNr2zNphADUCBHXiP+Ig==",
        "_ga_VED1YSGNC7": "GS1.1.1681663809.2.1.1681663832.0.0.0",
        "isg": "BBcXOYcLP1KSB7veVB1zlRtbpoJhXOu-ejLJLmlFTObxmDbacS3gD1D--jCGcMM2",
        "tfstk": "ccJCBw_nEibwzaMuKwiwCIGKlZWlaQqfVX_HA2JEqr5tR4KCWsA73Z_NaQ4RUgI1.",
        "l": "fBxfgCNHNIEcSVpaBO5Courza779iIdb8sPzaNbMiIEGC63ATyvOJRtQ2RINLd-RRJXPihTB4IRv12vT2er08zkfnSI97Xq9PQkMQe8C582bY"
    }

    body_pre = {"pageVersion":"984c9a58b6d16e5d8c31de9b899f058a","target":"root","data":{"d":"y","page":page_no,"sorttype":"total_tranpro_desc","SearchText":search_text,"trafficChannel":"main","g":"y","sortType":"total_tranpro_desc","origin":"y"},"eventName":"onChange","dependency":[]}
    body = f'{body_pre}'

    # body_pre['data']['page'] = 3
    # body = f'{body_pre}'
    # pprint('Body : \n{}'.format(body_pre))

    # search_referer_value = search_referer_value.format(page_no=1)
    # print('Search : {}\n'.format(search_referer_value))

    # pprint('HEADERS : {}'.format(headers['referer']))
    # print('\nAFTER change headers\n')
    # # page_no = 2
    # headers['referer'] = 'test'
    # pprint('HEADERS : {}'.format(headers['referer']))
    # print('\nAFTER change headers full\n')
    # pprint('HEADERS : {}'.format(headers))
   
    # pprint('COOKIES : {}'.format(cookies))
    # pprint('BODY : {}'.format(body))

    def start_requests(self):

        request = Request(
            url=self.url,
            method='POST',
            dont_filter=True,
            cookies=self.cookies,
            headers=self.headers,
            body=self.body,
            callback= self.parse
        )
        yield request

    def parse(self, response):
        # inspect_response(response, self)
        # Exit if the connection is declined
        if response.status == 404: 
            raise CloseSpider('Receive 404 response')
        
        raw_data= response.body
        data = json.loads(raw_data)
        # total_data_perpage = len(data['data']['result']['mods']['itemList']['content'])
        try:
            total_data_perpage = data['data']['result']['pageInfo']['pageSize']
        except KeyError:
            raise CloseSpider('Data per page is not exist, no more data')
        # print('\n\n Has {} DATA\n\n'.format(total_data_perpage))
        
        # Exit if there is no data available
        if total_data_perpage == 0:
            raise CloseSpider('No more data in response')
        
        # output csv file is in data folder in this project folder root
        for i in range(total_data_perpage):
            try:
                item ={
                    'Name' : data['data']['result']['mods']['itemList']['content'][i]['title']['displayTitle'],
                    'Price' : data['data']['result']['mods']['itemList']['content'][i]['prices']['salePrice']['minPrice']
                }
                yield item
            except KeyError:
                item={
                    'Name' : None,
                    'Price' : None
                }
                yield item
            except IndexError:
                item={
                    'Name' : None,
                    'Price' : None
                }
                yield item
        
        

        self.page_no += 1
        search_referer_value= f"https://www.aliexpress.com/w/wholesale-{self.search_text_dash}.html?d=y&page={self.page_no}&sorttype=total_tranpro_desc&SearchText={self.search_text_plus}&trafficChannel=main&g=y&sortType=total_tranpro_desc"

        self.body_pre['data']['page'] = self.page_no
        self.body = f'{self.body_pre}'

        self.headers['referer'] = search_referer_value
        
        print('\n\n Has {} DATA in page {}\n'.format(total_data_perpage,self.page_no-1))
        print('\nPAGE NO {}'.format(self.page_no))
        print('\n')
        pprint('HEADERS : {}'.format(self.headers))
        print('\n')
        pprint('BODY : {}'.format(self.body))
        print('\n')

        yield response.follow(
            url=self.url,
            method='POST',
            dont_filter=True,
            cookies=self.cookies,
            headers=self.headers,
            body=self.body,
            callback= self.parse
        )





        # start_requests(page_no = 1):
        # print("\nHas {} pages\n".format(data['data']['result']['pageInfo']['pageSize']))
        # self.page_no += 1
        # self.next_page = f'https://www.aliexpress.com/w/wholesale-{self.search_text_dash}.html?d=y&page={self.page_no}&sorttype=total_tranpro_desc&SearchText={self.search_text_plus}&trafficChannel=main&g=y&sortType=total_tranpro_desc'




        # print('\n New link : \n{}'.format(self.next_page))
        # print('\n\nNEW HEADERS\n\n')
        # pprint('\nHEADERS : {}'.format(self.headers))
        # pprint('\nCOOKIES : {}'.format(self.cookies))
        # pprint('\nBODY : {}'.format(self.body))
        # yield response.follow(
        #     url=next_page,
        #     method='POST',
        #     dont_filter=True,
        #     cookies=self.cookies,
        #     headers=self.headers,
        #     body=self.body,
        #     callback= self.parse
        #     )


