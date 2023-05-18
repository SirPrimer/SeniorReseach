# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SeniorresearchItem(scrapy.Item):
    jobTitle = scrapy.Field()
    responsibilities = scrapy.Field()
    qualifications2 = scrapy.Field()
    benefit = scrapy.Field()
    benefit2 = scrapy.Field()
    companyName = scrapy.Field()
    companyType = scrapy.Field()
    companyContent = scrapy.Field()
    link = scrapy.Field()

    jobTitle = scrapy.Field()
    jobWorkPattern = scrapy.Field()
    jobReceptions = scrapy.Field()
    jobLocation = scrapy.Field()
    jobSalary = scrapy.Field()
    jobHoliday = scrapy.Field()
    jobWorkHours = scrapy.Field()
    jobOtherWork = scrapy.Field()

    jobWorkDay = scrapy.Field()
    jobLevel = scrapy.Field()

    qualiGender = scrapy.Field()
    qualiAge = scrapy.Field()
    qualiEduLevel = scrapy.Field()
    qualiExperience = scrapy.Field()
    qualiOther = scrapy.Field()


