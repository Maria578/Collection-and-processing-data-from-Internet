# -*- coding: utf-8 -*-
import scrapy


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='bloko-button HH-Pager-Controls-Next HH-Pager-Control']/@href")

        vacancy_links = response.xpath("//a[@class='bloko-link HH-LinkModifier']/@href").extract()
        for link in vacancy_links:
            yield response.follow(link, callback=self.vacancy_parse)

        yield response.follow(next_page, callback=self.parse)

    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath("//h1[@class='bloko-header-1']//text()").extract_first()
        salary = response.xpath("//p[@class='vacancy-salary']/span/text()").extract()
        yield JobparserItem(name=name, salary=salary, link=response.url)
