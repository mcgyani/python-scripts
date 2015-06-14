#!/usr/bin/env python

from zabbix_api import ZabbixAPI, ZabbixAPIException
import json

zapi = ZabbixAPI(server="http://localhost/zabbix")
zapi.login("Admin", "zabbix")


hosts = zapi.host.get({"output": "extend", "monitored_hosts": 1
	}
)

for host in hosts:
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
	},
	"monitored": True,
	"active": True
})
for trigeron in trigger_on:
	print trigeron["description"]
	
trigger_on_ex = zapi.trigger.get({
	"output": "extend",
	"filter": {
		"value": 1
	},
	"active": True
})

print hosts
print json.dumps(trigger_on, indent = 4) 
print trigger_on_ex
