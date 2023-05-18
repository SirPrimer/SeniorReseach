import scrapy
from ..items import SeniorresearchItem

class QuoteSpider(scrapy.Spider):

    name = 'jobbkkUrgentJobSpider'

    with open ('UrgentLink.csv') as file:
        start_urls = [line.strip() for line in file]

    custom_settings = {
        'FEEDS': {'UrgentDone.csv': {'format': 'csv', 'overwrite': True }}
        }

    def parse(self, response):

        items = SeniorresearchItem()

        jobTitle = response.css('div.mb-2 h6.textRed.fontSubHead::text').extract()
        jobWorkPattern = response.css('.fontText+ p::text').extract()
        jobReceptions = response.css('p:nth-child(5)::text').extract()

        jobLocation = response.css('p.fontSubText::text').extract()
        jobSalary = response.css('p~ p+ .mb-2::text').extract()

        jobHoliday = response.css('.font-weight-bold~ span+ span::text , .mb-2~ p .font-weight-bold+ span::text, p:nth-child(8)::text').extract()
        jobWorkHours = response.css('p:nth-child(9)::text').extract()
        jobOtherWork = response.css('p:nth-child(10)::text').extract()

        jobWorkDay = response.css('p:nth-child(7)::text').extract()
        jobLevel = response.css('.mb-2~ p:nth-child(4)::text').extract()


        responsibilities = response.css('section:nth-child(8) li::text').extract()

        qualiGender = response.css('section:nth-child(10) p:nth-child(1)::text').extract()
        qualiAge = response.css('section:nth-child(10) p:nth-child(2)::text').extract()
        qualiEduLevel = response.css('section:nth-child(10) p:nth-child(3)::text').extract()
        qualiExperience = response.css('section:nth-child(10) p:nth-child(4)::text').extract()

        qualifications2 = response.css('section:nth-child(12) li::text').extract()

        benefit = response.css('h6 li::text').extract()
        benefit2 = response.css('section:nth-child(16) div h6::text').extract()

        companyName = response.css('.mb-4 .fontSubHead::text').extract()
        companyType = response.css('.fontText.mt-3::text').extract()
        companyContent = response.css('.content::text').extract()

        link = response.css('::attr(href)').extract()[0]


        items['jobTitle'] = jobTitle
        items['jobWorkPattern'] = jobWorkPattern
        items['jobReceptions'] = jobReceptions
        items['jobLocation'] = jobLocation
        items['jobSalary'] = jobSalary
        items['jobHoliday'] = jobHoliday
        items['jobWorkHours'] = jobWorkHours
        items['jobOtherWork'] = jobOtherWork
        items['jobWorkDay'] = jobWorkDay
        items['jobLevel'] = jobLevel

        items['responsibilities'] = responsibilities

        items['qualiGender'] = qualiGender
        items['qualiAge'] = qualiAge
        items['qualiEduLevel'] = qualiEduLevel
        items['qualiExperience'] = qualiExperience

        items['qualifications2'] = qualifications2
        items['benefit'] = benefit
        items['benefit2'] = benefit2
        items['companyName'] = companyName
        items['companyType'] = companyType
        items['companyContent'] = companyContent
        items['link'] = link

        yield items




