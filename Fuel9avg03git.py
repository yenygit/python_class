

import requests
import feedparser
import pprint

line = '_________________________________________________________'
arrowst = '>>>start>>>'
arrowend = '>>>end>>>'

def get_FwRss(url):
	response = requests.get(url)
	feed = feedparser.parse(response.content)
	priceinfo = feed['entries']
	return priceinfo

url_Nor_Tdy = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=25'
url_Sor_Tdy = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=26'
# url_Nor_Tmw = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=25&Day=tomorrow'
# url_Sor_Tmw = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=26&Day=tomorrow'

url_Nor_Tmw = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=25'
url_Sor_Tmw = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region=26'

priceinfo_Nor_Tdy = get_FwRss(url_Nor_Tdy)
priceinfo_Sor_Tdy = get_FwRss(url_Sor_Tdy)
priceinfo_Nor_Tmw = get_FwRss(url_Nor_Tmw)
priceinfo_Sor_Tmw = get_FwRss(url_Sor_Tmw)

# pprint.pprint(priceinfoavg, indent=4)


print(line) ###################################
print(arrowst)
print() ###################################


Fuel_Nor_Tdy = []
for Data in priceinfo_Nor_Tdy:	
	sublist = [Data['price'],Data['location']]
	Fuel_Nor_Tdy.append(sublist)

# for k in Fuel_Nor_Tdy:
# 	print(k)
# print(Fuel_Nor_Tdy)

Fuel_Sor_Tdy = []
for Data in priceinfo_Sor_Tdy:	
	sublist = [Data['price'],Data['location']]
	Fuel_Sor_Tdy.append(sublist)

# for k in Fuel_Sor_Tdy:
# 	print(k)
# print(Fuel_Sor_Tdy)

Fuel_Nor_Tmw = []
for Data in priceinfo_Nor_Tmw:	
	sublist = [Data['price'],Data['location']]
	Fuel_Nor_Tmw.append(sublist)

# for k in Fuel_Nor_Tmw:
# 	print(k)
# print(Fuel_Nor_Tmw)

Fuel_Sor_Tmw = []
for Data in priceinfo_Sor_Tmw:	
	sublist = [Data['price'],Data['location']]
	Fuel_Sor_Tmw.append(sublist)

# for k in Fuel_Sor_Tmw:
# 	print(k)
# print(Fuel_Sor_Tmw)

Fuel_Com_Tdy = Fuel_Nor_Tdy + Fuel_Sor_Tdy
# print(len(Fuel_Com_Tdy))

Fuel_Com_Tmw = Fuel_Nor_Tmw + Fuel_Sor_Tmw
# print(len(Fuel_Com_Tmw))

Suburd_list01 = []
for k in Fuel_Com_Tdy:
	Suburd_list01.append(k[1])
# print(Suburd_list01)

# for k in Fuel_Com:			### MISTAKE
# 	Suburd_list01 = []			### list inside for loop will create many list
# 	Suburd_list01.append(k[1])	### append only one item to one list
# 	print(Suburd_list01)		### print inside loop will print many list

# Suburd_list01.sort()
# print(Suburd_list02)

Count_list = []
for k in Suburd_list01:
	x = Suburd_list01.count(k)
	# print('{} count is {}'.format (k,x))
	Count_list.append(x)

Count_list02 = []
for k in Suburd_list01:
	x = Suburd_list01.count(k)
	Count_list02.append([k,x])
	# print('{} count is {}'.format (k,x))

# print(Count_list)
# print(len(Count_list))
# print(len(Fuel_Com))


###### error #######
# def by_loc(k):
# 	for k in Count_list02:
# 		return k[0]
# Count_list02.sort(key=by_loc)


Suburd_list02 = list(dict.fromkeys(Suburd_list01))
print(Suburd_list02)
# print(len(Suburd_list02))

Suburd_list02.sort()
# print(Suburd_list02)

# for k in Fuel_Com:
# 	print(k)
# 	print(k[0])
# 	print(k[1])

################# creating list of dictionary from list #################

Fuel_Com_Dic_Tdy = []
for k in Fuel_Com_Tdy:
	dic = {'price': k[0] ,'location': k[1]}
	Fuel_Com_Dic_Tdy.append(dic)
# print(Fuel_Com_Dic_Tdy)
# print(len(Fuel_Com_Dic_Tdy))

Fuel_Com_Dic_Tmw = []
for k in Fuel_Com_Tmw:
	dic = {'price': k[0] ,'location': k[1]}
	Fuel_Com_Dic_Tmw.append(dic)
# print(Fuel_Com_Dic_Tmw)
# print(len(Fuel_Com_Dic_Tmw))

################# insert new column of dictionary #################

for k in range(0,len(Count_list)):
	Fuel_Com_Dic_Tdy[k]['count'] = Count_list[k]

for k in range(0,len(Count_list)):
	Fuel_Com_Dic_Tmw[k]['count'] = Count_list[k]


def by_location(k):
	return k['location']
Fuel_Com_Dic_Tdy.sort(key=by_location)
Fuel_Com_Dic_Tmw.sort(key=by_location)

# sorted(Fuel_Com_Dic_Tdy, key = lambda k: k['location'])
# sorted(Fuel_Com_Dic_Tmw, key = lambda k: k['location'])

# for k in Fuel_Com_Dic_Tdy:
# 	print(k)
# for k in Fuel_Com_Dic_Tmw:
# 	print(k)
# for k in Suburd_list02:
# 	print(k)

avg_price_Tdy = []
Index_Tdy = 0
while Index_Tdy <= int(len(Suburd_list02))-1:
	sb = Suburd_list02[Index_Tdy]
	Index_Tdy += 1
	# print(sb)
	
	x = 0
	p = 0
	n = 0
	while x <= int(len(Fuel_Com_Dic_Tdy))-1:
		if sb == Fuel_Com_Dic_Tdy[x]['location']:
			p=float(p)+float(Fuel_Com_Dic_Tdy[x]['price'])/int(Fuel_Com_Dic_Tdy[x]['count'])
		x += 1
	avg_price_Tdy.append(p)
	# print('Today average for {} : {}'.format(sb,p)) ### Averaging result ###
# print(avg_price_Tdy)

avg_price_Tmw = []
Index_Tmw = 0
while Index_Tmw <= int(len(Suburd_list02))-1:
	sb = Suburd_list02[Index_Tmw]
	Index_Tmw += 1
	# print(sb)
	
	x = 0
	p = 0
	n = 0
	while x <= int(len(Fuel_Com_Dic_Tmw))-1:
		if sb == Fuel_Com_Dic_Tmw[x]['location']:
			p=float(p)+float(Fuel_Com_Dic_Tmw[x]['price'])/int(Fuel_Com_Dic_Tmw[x]['count'])
		x += 1
	avg_price_Tmw.append(p)
	# print('Tomorrow average for {} : {}'.format(sb,p)) ### Averaging result ###
# print(avg_price_Tmw)
	

############################################################

### final list ###
avg_list_TdyTmw = []
for k in Suburd_list02:
	avg_list_TdyTmw.append([k])

### list numbering ###
for k in range(0,len(avg_list_TdyTmw)):
	avg_list_TdyTmw[k].insert(0,str(k+1))

### adding today avg price ###
for k in range(0,len(avg_list_TdyTmw)):
	avg_list_TdyTmw[k].append(avg_price_Tdy[k])

### adding tomorrow avg price and number of store###
for k in range(0,len(avg_list_TdyTmw)):
	avg_list_TdyTmw[k].append(avg_price_Tmw[k])

avg_list_TdyTmw.insert(0,['No:','Suburb','Today Avg','Tomorrow Avg'])

# for k in avg_list_TdyTmw:
# 	print(k)


###########################################################

fileout = open("tableavg.html", "w")

table = '''
<style type>
	table {border-collapse: collapse; border:ridge 2px black; width: 60%;
	text-align: left; font-family: }
	td, th {border: 1px solid grey; padding: 5px;}
	th {height: 30px;}
	tr.Tdy {background-color:orange; color:white;}
	tr.Header {background-color:grey; color:white;}
</style>'''

table += '<p>Average petrol price of suburb</p>\n'

table += "<table>\n"

# Create the table's headers
header = avg_list_TdyTmw[0]
table += '''  <tr class="Header">\n'''
for k in header:
    table += "    <th>{}</th>\n".format(k.strip())
table += "  </tr>\n"

# Create the table's in following row
for k in avg_list_TdyTmw[1:]:
	if k[2] == 'Tdy':
		table += '''  <tr class="Tdy">\n'''
	else:
		table += "  <tr>\n"
	for x in k:
		table += "    <td>{}</td>\n".format(str(x).strip())
	table += "  </tr>\n"
table += "</table>"

fileout.writelines(table)
fileout.close()


print(table)##########################################

# return table

print(line) ###################################
print(arrowend)


