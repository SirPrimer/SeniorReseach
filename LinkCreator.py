link = 'https://www.jobbkk.com/%E0%B8%AB%E0%B8%B2%E0%B8%87%E0%B8%B2%E0%B8%99/%E0%B8%AD%E0%B8%B7%E0%B9%88%E0%B8%99%E0%B9%86/'
maxLink = 33 #maximum job menu page
with open('realOgLinks.csv', 'w') as f:
    for i in range(1,maxLink+1):
        fullLink = link + str(i)
        print(fullLink, file=f)
