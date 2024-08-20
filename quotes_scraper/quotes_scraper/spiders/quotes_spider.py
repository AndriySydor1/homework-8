import scrapy
from quotes_scraper.items import QuoteItem, AuthorItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            quote_item = QuoteItem(
                text=quote.css('span.text::text').get(),
                author=quote.css('small.author::text').get(),
                tags=quote.css('div.tags a.tag::text').getall()
            )
            yield quote_item

            author_url = quote.css('span a::attr(href)').get()
            if author_url is not None:
                yield response.follow(author_url, self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        author_item = AuthorItem(
            name=response.css('h3.author-title::text').get().strip(),
            birth_date=response.css('span.author-born-date::text').get(),
            birth_place=response.css('span.author-born-location::text').get().strip(),
            description=response.css('div.author-description::text').get().strip()
        )
        yield author_item
        
