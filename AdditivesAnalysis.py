import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

world_food_facts = pd.read_csv('../datafeeds/FoodFacts.csv')
world_food_facts.countries = world_food_facts.countries.str.lower()


def mean(l):
    return float(sum(l)) / len(l)


world_additives = world_food_facts[world_food_facts.additives_n.notnull()]


def return_additives(country):
    return world_additives[world_additives.countries == country].additives_n.tolist()


# Get list of additives amounts for some countries
fr_additives = return_additives('france') + return_additives('en:fr')
za_additives = return_additives('south africa')
uk_additives = return_additives('united kingdom') + return_additives('en:gb')
us_additives = return_additives('united states') + return_additives('en:us') + return_additives('us')
sp_additives = return_additives('spain') + return_additives('españa') + return_additives('en:es')
ch_additives = return_additives('china')
nd_additives = return_additives('netherlands') + return_additives('holland')
au_additives = return_additives('australia') + return_additives('en:au')
jp_additives = return_additives('japan') + return_additives('en:jp')
de_additives = return_additives('germany')

countries = ['FR', 'ZA', 'UK', 'US', 'ES', 'CH', 'ND', 'AU', 'JP', 'DE']
additives_l = [mean(fr_additives),
               mean(za_additives),
               mean(uk_additives),
               mean(us_additives),
               mean(sp_additives),
               mean(ch_additives),
               mean(nd_additives),
               mean(au_additives),
               mean(jp_additives),
               mean(de_additives)]

y_pos = np.arange(len(countries))

plt.bar(y_pos, additives_l, align='center', alpha=0.5)
plt.title('Average amount of additives')
plt.xticks(y_pos, countries)
plt.ylabel('Amount of additives')

plt.show()