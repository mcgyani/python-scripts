#!/usr/bin/env python

from zabbix_api import ZabbixAPI
import json

zapi = ZabbixAPI(server="http://localhost/zabbix")
zapi.login("Admin", "zabbix")

hostgroup = "Zabbix servers"

hostgroup = zapi.host.get({"output": "extend"
	}
)

for host in hostgroup:
	for key, value in host.iteritems():
		if key == "error":
			print value

trigger_on = zapi.trigger.get({
	"output": [
		"triggerid",
		"description",
		"priority"
	],
	"filter": {
		"value": 1
	}
})
for trigeron in trigger_on:
	print trigeron["description"]
	
print json.dumps(trigger_on, indent = 4) 
