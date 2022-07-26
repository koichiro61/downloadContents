'''
Read a list of urls and download the contents in the urls
'''

import urllib.request
import urllib.parse
import re
import ssl
import time

filepath = 'fileurl.txt'

wait = 3

ssl._create_default_https_context = ssl._create_unverified_context

f = open(filepath, 'r', encoding='UTF-8')

seq = 0
urldict = {}

url = f.readline()

while url != '':	#============================ start of the main loop
	url = url.rstrip('\n')
	url_count = urldict.get(url, 0)
	
	if url_count == 0:	# the first time for this url
				# ok, let's start the preparation --------------
		
		urldict[url] = 1	
		seq += 1
		
		# get extension of the target
		m = re.match(r'^.+[\.\?](\S+)$', url)	
		if m is not None:
			ext = '.' + m.group(1)
		else:
			ext = ''
		save_name = 'f{:04d}{}'.format(seq, ext)
		
		# url encoding
		url = urllib.parse.quote(url, safe=':/?')
				
		print (url, save_name)
			
		try:
			urllib.request.urlretrieve(url, save_name)
		except urllib.error.HTTPError as err:
			print(url, err.code, err.reason)
		except urllib.error.URLError as err:
			print(url, err.reason)
		time.sleep(wait)
		
		# end of the main processing --------------------------------------
	else:	# urldict[url] > 0, i.e. this url has appeared in the past 
		urldict[url] += 1	# just count up. no need to download the same contents again
		
	url = f.readline()
	# =========================================== end of the main loop
'''
for kk in urldict.keys():	# to list up the urls and the count of appearance
	print(kk, urldict[kk])
'''
