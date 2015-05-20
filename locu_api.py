import urllib2
import json
 
#locu_api = 'bf25f41dc88a14c39cc5d63f18d5d1d18d465f01'
 
url = 'https://api.locu.com/v1_0/venue/search/?locality=Bucharest&api_key=bf25f41dc88a14c39cc5d63f18d5d1d18d465f01'
obj = urllib2.urlopen(url)
 
data = json.load(obj)
print json.dumps(data,indent=4)
for item in data['objects']:
        print item['phone']
 
        #if-folosea diacritice / else: returna NoneAttrbute Error pt ca era campul null 
        if item['street_address'] is not None:
                print item['street_address'].encode('utf-8')
        else:   
                print str(item['street_address'])
 
for key, value in data.iteritems():
        if key == 'objects':
                for i in value:
                        for key, value in i.iteritems():
                                if key == 'postal_code' and value == '040404':
                                        print i['name']
