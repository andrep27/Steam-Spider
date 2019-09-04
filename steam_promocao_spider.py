import scrapy 
from urllib.parse import urlparse
from scrapy.selector import Selector

class Produto(scrapy.Item):
    Nome = scrapy.Field()
    PrecoInicial = scrapy.Field()
    PrecoFinal = scrapy.Field()
    DiaTermino = scrapy.Field()

class SteamPromocaoSpider (scrapy.Spider):
    name = "steam"
    start_urls = ["https://store.steampowered.com"]

    def parse(self, response):
        body_sel = Selector(response)
        urls_jogo = body_sel.xpath("//div[@class='home_page_content']//div[@id='tab_specials_content']//a//@href").extract()

    def parse_atracao (self, response):
        body_sel = Selector(response)

        Nome = self.to_str(body_sel.xpath("//div[@class='game_area_purchase_game']//h1//text()")).extract()

        PrecoInicial = self.to_str(body_sel.xpath("//div[@class='game_purchase_action']//div[@class='discount_original_price']//text()")).extract()

        PrecoFinal = self.to_str(body_sel.xpath("//div[@class='game_purchase_action']//div[@class='discount_final_price']//text()")).extract()

        DiaTermino = self.to_str(body_sel.xpath("//p[@class='game_purchase_discount_countdown']//text()")).extract()

    def to_str(self, selector):
        return selector.extract()[0].encode("utf-8")
        
 

    print("--------------------")