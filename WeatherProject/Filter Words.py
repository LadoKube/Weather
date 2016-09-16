import csv

# List of some place names in london
London_Places = ['London', 'soho', 'greenwich','twickenham', 'wembley ', 'waterloo', 'whitechapel', 'buckingham palace','hyde park']

# I grabbed a list of boroughs from the internet and added it to the above list. Will add this file to git
with open('\\users\\student05\\documents\\London Boroughs.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        London_Places.append(str(row[0]))

# Hand wrote a list of weather key words for three types of weather
GoodWeather = ['Sunny', 'weather hot', 'weather lovely', 'weather beautiful', 'beautiful day', 'weather delightful', 'gorgeous weather',
                 'amazing weather','glorious weather']
BadWeather = ['shit weather', 'stormy weather', 'weather rain', 'rainy weather', 'pissing down','pouring rain','snow weather', 'hail weather',
              'freezing day', 'awful weather', 'terrible weather', 'thunder weather']
MixWeather = ['crap weather', 'cold day','cold weather','freezing weather','fantastic weather', 'stunning weather', 'scorching weather']

# Initialise three lists for combining the place names and different phrases
GoodWeatherPhrases = []
BadWeatherPhrases = []
MixWeatherPhrases = []

# for loops to combine the places and weathers together
for i in range(len(London_Places)):
    for j in range(len(GoodWeather)):
        GoodWeatherPhrases.append(str(London_Places[i]) + ' ' + str(GoodWeather[j]))
    for k in range(len(BadWeather)):
        BadWeatherPhrases.append(str(London_Places[i] + ' ' + str(BadWeather[k])))
    for l in range(len(MixWeather)):
        MixWeatherPhrases.append(str(London_Places[i] + ' ' + str(MixWeather[l])))

# Writes each list out to a csv so we can easily copy and paste from notepad
with open('\\users\\student05\\documents\\GoodWeatherPhrases.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|')
    writer.writerow(GoodWeatherPhrases)

with open('\\users\\student05\\documents\\BadWeatherPhrases.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|')
    writer.writerow(BadWeatherPhrases)

with open('\\users\\student05\\documents\\MixWeatherPhrases.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',', quotechar='|')
    writer.writerow(MixWeatherPhrases)