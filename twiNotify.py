#twiNotify v0.1
import urllib,time
import simplejson as json
q = '@w43l'
nap = 5
url = "http://search.twitter.com/search.json?%s" % urllib.urlencode({'q':q})
print "\a"
max_id = 0
while(1):
	searchRs = urllib.urlopen(url).read()
	mentionsJson = json.loads(searchRs)
	mentions = mentionsJson['results']
	time.sleep(nap)
	if (max_id != mentionsJson['max_id']):
		max_id = mentionsJson['max_id']
		print max_id
