import scrapy
from scrapy import Request
import requests
import json


class DevR01Spider(scrapy.Spider):
    name = "dev_r0.1"
    # allowed_domains = ["x"]
    # start_urls = ["http://x/"]

    # Find hidden API
    # Found out at page 2
    # Generate payload, headers using Postman
    url = "https://www.aliexpress.com/fn/search-pc/index"

    search_item = "iphone repair kit"

    payload = "{\"pageVersion\":\"984c9a58b6d16e5d8c31de9b899f058a\",\"target\":\"root\",\"data\":{\"d\":\"y\",\"page\":2,\"sorttype\":\"total_tranpro_desc\",\"SearchText\":\"iphone repair kit\",\"trafficChannel\":\"main\",\"g\":\"y\",\"sortType\":\"total_tranpro_desc\",\"origin\":\"y\"},\"eventName\":\"onChange\",\"dependency\":[]}"
    headers = {
    'authority': 'www.aliexpress.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ms;q=0.8,id;q=0.7',
    'bx-v': '2.2.3',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'ali_apache_id=33.1.233.206.168165714556.220188.8; XSRF-TOKEN=dac9b48a-8d41-44d6-9481-899122bf78be; intl_locale=en_US; xman_f=2b+2kj2uR0eXgou5CgWhGpgphxdU5wAXdY+PVxuvcQmT848+4eMIqOAY7k5W2eq049i6QZn0XvfYUScJHK6x8ZDQlzxE6mdvwBx2SpH42Dg0VtjIJ/KtWw==; acs_usuc_t=x_csrf=t9qft2mgtajx&acs_rt=69f1d345386a41a38eca9650f129b7cf; xman_t=1OHyCkveGr/Y3fNBNWP8rktUOCSfElO1Aaj/15OsX31W23J2PTLonF7R1pI/ULgS; aep_usuc_f=site=glo&c_tp=MYR&region=MY&b_locale=en_US; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005004559525694; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=0&acs_rt=69f1d345386a41a38eca9650f129b7cf; cna=Y/vCHBKJCQYCAXOkMwh5kRIh; _gcl_au=1.1.1374349958.1681657189; _ga=GA1.1.1945978505.1681657193; _m_h5_tk=f50ebfb538e6f439ddbeebcc11a8447b_1681665669021; _m_h5_tk_enc=449cfe8f525123048eb6187840f01cb6; AKA_A2=A; JSESSIONID=06B94F0DB668FA955FDC5CC4AB00231B; intl_common_forever=83SivZfHKM6YEGgFOKwPYc4eztw8UAsnADqNr2zNphADUCBHXiP+Ig==; _ga_VED1YSGNC7=GS1.1.1681663809.2.1.1681663832.0.0.0; isg=BBcXOYcLP1KSB7veVB1zlRtbpoJhXOu-ejLJLmlFTObxmDbacS3gD1D--jCGcMM2; tfstk=ccJCBw_nEibwzaMuKwiwCIGKlZWlaQqfVX_HA2JEqr5tR4KCWsA73Z_NaQ4RUgI1.; l=fBxfgCNHNIEcSVpaBO5Courza779iIdb8sPzaNbMiIEGC63ATyvOJRtQ2RINLd-RRJXPihTB4IRv12vT2er08zkfnSI97Xq9PQkMQe8C582bY; aep_usuc_f=site=glo&c_tp=MYR&region=MY&b_locale=en_US; intl_common_forever=Fh28PbEW4U/ISSL+zg4PQrqb8jkOQvJRN47Vte+nU26+D1PSVMkyiA==; intl_locale=en_US; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=0&acs_rt=69f1d345386a41a38eca9650f129b7cf',
    'dnt': '1',
    'origin': 'https://www.aliexpress.com',
    'referer': 'https://www.aliexpress.com/w/wholesale-iphone-repair-kit.html?d=y&page=2&sorttype=total_tranpro_desc&SearchText=iphone+repair+kit&trafficChannel=main&g=y&sortType=total_tranpro_desc',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
    }

    # response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

    def start_requests(self):
        return Request(url= self.url, method='POST', headers=self.headers, body=json.dumps(self.payload), callback=self.paginate)

    def paginate(self, response):
        pass
