import scrapy 



class test_scraper(scrapy.Spider) :
	name = "test_spider"

	def start_requests(self) :
		yield scrapy.Request(url = "https://publicholidays.fr/fr/2019-dates/", callback = self.parse)

	def parse(self, response) : 
		# define table 
		table =  response.xpath('//table[@class = "publicholidays phgtable "]')[0]
		header =  [title for title in table.xpath('//thead//tr/th/text()').extract()]
		yield {
			header[0] : table.xpath('//td[1]/text()').extract(),
			header[1] : table.xpath('//td[2]/text()').extract(),
			header[2] : table.xpath('//td[3]/a[@class = "summary url"]/text()').extract()
			}
