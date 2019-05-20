import pandas as pd
import matplotlib.pyplot as plt

# pulled from https://yearbook.enerdata.net/
elec = pd.read_excel('Enerdata_Energy_Statistical_Yearbook_2018.xlsx', sheet_name='Electricity domestic consumpti'
                     , usecols='A:AC', header=2, skipfooter=2)

elec.rename(columns=lambda x: str(x), inplace=True)
elec.rename(columns={'Unnamed: 0': 'country'}, inplace=True)
elec['growth'] = elec['2017'] - elec['1990']

# Remove regions
elec = elec[~elec.country.isin(['World', 'OECD', 'G7', 'BRICS', 'Europe', 'European Union', 'CIS', 'America',
                                   'North America', 'Latin America', 'Asia', 'Pacific', 'Africa', 'Middle-East'])]

# makes the plot and assign it to a variable
elec_open = elec.sort_values(['growth'], ascending=False).plot(kind='bar',
                                                               x='country', y='growth', title="Usage by Country")
elec_open.set(xlabel='Country', ylabel='Growth in TWh')

# changes the size of the graph
fig = elec_open.get_figure()
fig.set_size_inches(13.5, 9)
plt.show()

# Create a new dataframe with sum by year
elec = elec.set_index('country')
yr_usage = pd.DataFrame(data=elec.sum(), columns=['usage'])
yr_usage = yr_usage[:-1]

# makes the plot and assign it to a variable
yr_open = yr_usage.plot(kind='bar', title="Usage by Year")
yr_open.set(xlabel='Year', ylabel='Usage in TWh')

# changes the size of the graph
fig = yr_open.get_figure()
fig.set_size_inches(13.5, 9)
plt.show()
