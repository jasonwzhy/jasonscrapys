import scrapy
class My089Spider(scrapy.Spider):
	"""docstring for My089Spider"""
	name = "my089"
	allowed_domains = ["my089.com"]
	start_urls = [
		"https://www.my089.com/Loan/default.aspx"
	]
	def parse(self,response):
		print response.xpath('/html/body')
		item = DemoscrapyItem()
		item['content'] = response.xpath('/html/body')
		"""for sel in response.xpath('//*[@id="aspnetForm"]/div[3]'):
			item = DemoscrapyItem()
			item['content'] = sel
			yield item"""
		filename = response.url.split("/")[-2]
		with open(filename,'wb') as f:
			f.write(response.body)