import re

adres = '80.91.33.133 - - [04/Jun/2015:07:06:14 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.22)"'
adres2 ='192.235.75.62 - - [04/Jun/2015:07:06:41 +0000] "GET /downloads/product_1 HTTP/1.1" 404 334 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.12)"'

print(adres)
print(re.search(r'\d+ "', adres).group()[:-2])       #   data
print(re.search(r'\d+ "', adres2).group()[:-2])       #   data
