import scrapy


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['blog.csdn.net']   # 允许爬取的范围
    start_urls = ['https://blog.csdn.net/weixin_45650737']  # 初始请求的网址

    def parse(self, response):
        res = response.xpath("//div[@class='navList-box']//h4/text()").extract()
        # print('======>',response.body)
        print('------>',res)
