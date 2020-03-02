#Imports 

import urllib3
from bs4 import BeautifulSoup 

#http request 
http = urllib3.PoolManager() 

#Requesting 
url = "https://www.bol.com/nl/ra/algemeen/nieuwe-collectie-mode-voor-heren/64450/N/47024/?bltg=itm_event%3Dclick%26itm_id%3D2100000160%26itm_lp%3D1%26itm_type%3Dinstrument%26sc_type%3DCURRENT%26itm_ttd%3DFLEX_BANNER%26mmt_id%3DXlzv8eVJVWjnPsfRmL4kVQAAAzM%26rpgActionId%3D64450%26rpgInstrumentId%3D2100000160%26pg_nm%3Dmain%26slt_id%3D819%26slt_pos%3DA2%26slt_owner%3DRPG%26sc_algo%3DRPGR%26slt_nm%3DFLEX_BANNER%26slt_ttd%3DFLEX_BANNER%26sc_id%3D0&promo=main_819_CRPGR64450_A2_MHP_1_210000"
response = http.request('GET', url) 
soup = BeautifulSoup(response.data)
print(soup)