import scrapy
from ..items import SeniorresearchItem

class QuoteSpider(scrapy.Spider):

    name = 'jobbkkNonUrgentJobSpider'

    with open ('NonUrgentLink.csv') as file:
        start_urls = [line.strip() for line in file]

    custom_settings = {
        'FEEDS': {'NonUrgentDone.csv': {'format': 'csv', 'overwrite': True }}
        }

    def parse(self, response):

        items = SeniorresearchItem()

        jobTitle = response.css('.col-xs-6 .text-red::text').extract()
        jobWorkPattern = response.css('.margin-bottom:nth-child(4) .margin-bottom-1+ h6::text').extract()
        jobReceptions = response.css('.col-md-12:nth-child(4) h6:nth-child(3)::text').extract()
        jobLocation = response.css('.col-md-12:nth-child(4) h6:nth-child(4)::text').extract()
        jobSalary = response.css('.margin-bottom:nth-child(4) h6:nth-child(5)::text').extract()
        jobHoliday = response.css('.col-md-8.col-sm-12 span::text').extract()
        jobWorkHours = response.css('.margin-bottom:nth-child(4) h6:nth-child(7)::text').extract()
        jobOtherWork = response.css('.margin-bottom:nth-child(4) h6:nth-child(8)::text').extract()


        responsibilities = response.css('.margin-bottom:nth-child(6) .margin-bottom-1+ h6::text').extract()

        qualiGender = response.css('.margin-bottom:nth-child(8) h6:nth-child(2)::text').extract()
        qualiAge = response.css('.margin-bottom:nth-child(8) h6:nth-child(3)::text').extract()
        qualiEduLevel = response.css('.margin-bottom:nth-child(8) h6:nth-child(4)::text').extract()
        qualiExperience = response.css('.margin-bottom:nth-child(8) h6:nth-child(5)::text').extract()
        qualiOther = response.css('.margin-bottom:nth-child(8) h6:nth-child(6)::text').extract()

        qualifications2 = response.css('.margin-bottom-1+ h6:nth-child(8)::text').extract()

        benefit = response.css('.margin-bottom:nth-child(10) li::text').extract()
        benefit2 = response.css('.margin-bottom-1+ h6:nth-child(4)::text').extract()

        companyName = response.css('h4 a::text').extract()

        link = response.css('::attr(href)').extract()[0]

        items['jobTitle'] = jobTitle
        items['jobWorkPattern'] = jobWorkPattern
        items['jobReceptions'] = jobReceptions
        items['jobLocation'] = jobLocation
        items['jobSalary'] = jobSalary
        items['jobHoliday'] = jobHoliday
        items['jobWorkHours'] = jobWorkHours
        items['jobOtherWork'] = jobOtherWork

        items['responsibilities'] = responsibilities


        items['qualiGender'] = qualiGender
        items['qualiAge'] = qualiAge
        items['qualiEduLevel'] = qualiEduLevel
        items['qualiExperience'] = qualiExperience
        items['qualiOther'] = qualiOther


        items['qualifications2'] = qualifications2
        items['benefit'] = benefit
        items['benefit2'] = benefit2
        items['companyName'] = companyName
        items['link'] = link

        yield items
