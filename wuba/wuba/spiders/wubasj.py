# -*- coding: utf-8 -*-

# 八个城市url：(https: // www.58.com / changecity.html?catepath=zhuangxiujc.shtml & catename= % E8 % A3 % 85 % E4 % BF % AE % E5 % BB % BA % E6 % 9D % 90 & fullpath=26509 & PGTID=0d20678d-0000-38aa-12e6-c410f82e0e6b & ClickID=1)
#     济南，https: // jn.58.com / zhuangxiujc.shtml
#     泰安，https: // ta.58.com / zhuangxiujc.shtml
#     青岛，https: // qd.58.com / zhuangxiujc.shtml
#     深圳，https: // sz.58.com / zhuangxiujc.shtml
#     广州，https: // gz.58.com / zhuangxiujc.shtml
#     珠海，https: // zh.58.com / zhuangxiujc.shtml
#     佛山，https: // fs.58.com / zhuangxiujc.shtml
#     合肥，https: // hf.58.com / zhuangxiujc.shtml
# 本地服务的url
#     https: // fs.58.com / zhuangxiujc.shtml?PGTID = 0d300261 - 000d - e7ff - 41a5 - 94b92c564bb2 & ClickID = 1
# 然后获取网页内的六个网页url, 分别要：(如果是要全部的url 每个网页是没有100页的，这样要爬取的网页翻倍增加，)
#     装修建房
#         家装服务 / jiazhuang /
#         店铺楼宇装修 / gongzhuang /
#         建房翻新改造 / fanjiangaizao /
#     建材 / 工具
#         建材工具购买 / jiancai /
#     家具 / 家饰
#         家具定制 / 购买 / jiajusp /
#         家纺家饰 / jiajuzs /
#             https: // fs.58.com / jiajuzs /?PGTID = 0d20678d - 000d - e495 - 0620 - 6d23e2a9a7c5 & ClickID = 2
#
# 进入这六个网页爬取网页内每个企业数据，要100页数据(指不定没有100页)
#     公司名称
#     电话(电话要自动化点击后获取 电话('/html/body/div[14]/div/div[1]/div[1]') 关闭('/html/body/div[14]/div/div[2]'))
#     名称 新房, 二手房翻新, 免费设计, 居家装饰, 先装修后付款
#     描述
#     url

import scrapy
from items import WubaItem
import requests
import time


class WubasjSpider(scrapy.Spider):
    name = 'wubasj'
    # allowed_domains = ['fs.58.com']
    start_urls = ['https://jn.58.com/zhuangxiujc.shtml']
    # start_urlss = ['https://jn.58.com/zhuangxiujc.shtml',
    #                 'https://ta.58.com/zhuangxiujc.shtml',
    #                 'https://qd.58.com/zhuangxiujc.shtml',
    #                 'https://sz.58.com/zhuangxiujc.shtml',
    #                 'https://gz.58.com/zhuangxiujc.shtml',
    #                 'https://zh.58.com/zhuangxiujc.shtml',
    #                 'https://fs.58.com/zhuangxiujc.shtml',
    #                 'https://hf.58.com/zhuangxiujc.shtml']

    def parse(self, response):
        classifys = response.xpath("//dl[@class='nav-content__catebox__sidebar--cateitem _catecss-item']")
        for classify in classifys[:-3]:
            url = classify.xpath("./dt/a/@href").extract()[0]
            url = 'https://jn.58.com'+str(url)
            yield scrapy.Request(url=url,callback=self.issuer,meta={'pa_url':url})
        # chengshi = response.xpath('//*[@id="content-box"]')
        # chengshi2 = response.xpath('//*[@id="content-box"]/div[1]/div/div[2]/a[1]/text()').extract()
        # xiangxi = chengshi.xpath('./div/div/div/a/@href').extract()
        # print(chengshi2,xiangxi)

        # k = response.xpath('/html/body/div[4]/div/div/div')
        # xx1 = k.xpath('./div[1]/dl/dd/a/text()').extract()
        # xx2 = k.xpath('./div[2]/dl/dd/a/text()').extract()
        # xx3 = k.xpath('./div[3]/dl/dd/a/text()').extract()
        # print(xx1,xx2,xx3)
        # items = WubaItem()
        # items_1 = []
        # a = response.xpath('/html/body/div[4]/div/div/div')
        # lj1 = ['https://jn.58.com' + x for x in a.xpath('./div[1]/dl/dd/a/@href').extract()]
        # lj2 = ['https://jn.58.com' + x for x in a.xpath('./div[2]/dl/dd/a/@href').extract()]
        # lj3 = ['https://jn.58.com' + x for x in a.xpath('./div[3]/dl/dd/a/@href').extract()]
        # for lj in lj1,lj2,lj3:
        #     items_1.append(lj)
        #     items['bendi'] = lj[0]
        #     yield scrapy.Request(url=items['bendi'], meta={'lj_lj': items},callback=self.parse_sj)
        # print(items_1)
        # for items in items_1:
        #     yield Request(url=items,callback=self.parse)
    # def parse_sj(self, response):
    #     item = response.meta['lj_lj'] # 忘记接收上一级的数据
    #     print('+++++++++++555555555555555555++++++++++')
    #     res = requests.get(response.url)
    #     res.encoding = 'utf-8'
    #     html = res.text
    #     print(html)
    #     print('+++++++++++555555555555555555++++++++++')
    #     gongsi = response.xpath('//tbody/tr/td[2]/p[1]/text()').extract()
    #     mingcheng = response.xpath('//tbody/tr/td[2]/a/text()').extract()
    #     print(mingcheng,gongsi)
    def issuer(self,response):
        issuers = response.xpath("//table[@id='jingzhun']")
        for issuer in issuers:
            trs = issuer.xpath("./tr[@class='ac_item']")
            for tr in trs:
                url = tr.xpath("./td[@class='t']/div/a/@href").extract_first("")
                if url == '':
                    url = tr.xpath("./td[@class='img']/div/a/@href").extract_first("")
                if url != '//fangxin.58.com/demand/form/quickpost?cateid=4063?from=pc_fangxin_zhuangxiu_listno1' and url != '':
                    yield scrapy.Request(url=url,callback=self.deal,meta={'deal_url':url,'pa_url':response.meta.get('pa_url','')})

    def deal(self, response):

        company_name = response.xpath("//div[@class='shopinfo__title']/h2/text()").extract_first("").strip()
        title = response.xpath("//div[@class='detail-title']/h1[@class='detail-title__name']/text()").extract_first("").strip()
        # category = response.xpath("//div[@class='infocard__container noswitch']/div[@class='infocard__container__item__main']/text()").extract()
        site = response.xpath("//div[@class='infocard__container__item infocard__container__item--shopaddress']/div[@class='infocard__container__item__main']/a/text()").extract()
        site = ''.join(site).strip()
        introduce = response.xpath("//div[@class='foldingbox']/article/text()").extract()
        url = response.meta.get('deal_url','')
        pa_url = response.meta.get('pa_url','')
        if introduce != []:
            introduce = ''.join(introduce)
        print(company_name)
        print(title)
        # print(category)
        print(site)
        print(introduce)
        item = WubaItem()
        item['bendi'] = pa_url
        item['gongsi'] = company_name
        item['mingcheng'] = title
        item['miaoshu'] = introduce
        item['lianjie'] = url
        yield item


