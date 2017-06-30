import requests
import base64
import datetime
#import json
#import simplejson
#import urllib
#import urllib2
#import hashlib
from fnexchange.core.plugins import AbstractPlugin


class JiraPlugin(AbstractPlugin):
	def Get_Issue_Type(self, payload):
		elements = payload["elements"]
		base_url = getattr(self.config, 'base_url', None)
		issuetypes_url = getattr(self.config,'issue_types', None)
		username = getattr(self.config, 'username', None)
		password = getattr(self.config, 'password', None)

		auth = 'Basic '+ base64.b64encode(username+':'+password)
		headers = {'Content-Type':'application/json','Authorization': auth }
		send_url = base_url + issuetypes_url
		"""
		{
			"alias":"jira",
			"token" : "SECURE-TOKEN-2-HERE" ,
			"action" : "Get_Issue_Type" ,
			"payload": {"elements":[{}]}
		}
		"""
		success = False
		info = ""
		try:
			#print "y"
			response = requests.get(send_url,headers=headers)
			#print response.json()
			success = response.status_code == 200
			info = "list of all issue types"
			#print "hureee"
		except:
			pass



		return {
		'metadata': {
			'success': success,
			'info': info,
			'report_json':response.json()
		},
		'elements': elements  # return the same thing back
		}
	def Create_Issue1(self, payload):
		elements = payload["elements"]
		print "New Face"
		Issue_types = getattr(self.config, 'all_issue_types_you_want', None)
		print len(Issue_types)
		issuetypes_url = getattr(self.config,'issue_types', None)
		base_url = getattr(self.config, 'base_url', None)
		createissue_url = getattr(self.config,'create_issue', None)
		username = getattr(self.config, 'username', None)
		password = getattr(self.config, 'password', None)

		types_we_need = getattr(self.config,'all_issue_types_you_want', None)
		types_we_need_list = types_we_need.split(',')
		print len(types_we_need_list)
		#print len(types_we_need_list[5])
		auth = 'Basic '+ base64.b64encode(username+':'+password)
		headers = {'Content-Type':'application/json','Authorization': auth }
		
		issue_send_url = base_url + createissue_url
		issuetypes_send_url = base_url + issuetypes_url
		
		initial_types_dic={}
		print "Get Jinxed"
		try:
			response = requests.get(issuetypes_send_url,headers=headers)
			initial_types_dic = response.json()
			print initial_types_dic
		except:
			pass

		initial_types_list = initial_types_dic["projects"][0]["issuetypes"]
		print initial_types_list
		name_to_id_map = {}
		types =[]
		print "Blow the Sun"
		for dic in initial_types_list :
			print dic["name"]
			print dic["id"]
			#name_to_id_map[dic["name"]] = dic["id"]
			types.append(dic["name"])
		print "still get jinxed"
		print types
		print Issue_types
		for item in types_we_need_list :
			print item
			if item in types:
				print item
				types.remove(item)
			else :
				print "shit happens"
				try:
					param = {"name": item, "description":"provide"+item,"type": "standard"}
					response = requests.post(issuetypes_send_url,headers=headers,json=param)
					print response.json()
				except:
					print "hi"
					pass
		for item in types:
			try:
				response = requests.delete(issuetypes_send_url+"/"+name_to_id_map[item],headers=headers)
				print response.json()
			except:
				pass
		param={
				"fields":{
							"project"		:{
												"id":"10000"
											},
							"summary"		:	"summary",
							"issuetype"		:{
												"name": "IT Help"
											},
							"labels"		:[
												"labels"
											],
							"description"	:	"description",
							"duedate"		:	datetime.datetime.today().strftime('%Y-%m-%d')
						}
			}
		"""	
		param={
				"fields":{
							"project"		:{
												"id":"10000"
											},
							"summary"		:	elements[0]["summary"],
							"issuetype"		:{
												"name":elements[0]["name"]
											},
							"labels"		:[
												elements[0]["labels"]
											],
							"description"	:	elements[0]["description"],
							"duedate"		:	datetime.datetime.today().strftime('%Y-%m-%d')
						}
			}
		{
			"alias":"jira",
			"token" : "SECURE-TOKEN-2-HERE" ,
			"action" : "Get_Issue_Type" ,
			"payload": {"elements":[{}]}
		}
		"""
		success = False
		info = ""
		try:
			print "y"
			response = requests.post(issue_send_url,headers=headers,json=param)
			print response.json()
			success = response.status_code == 201
			info = "list of all issue types"
			print "hureee"
		except:
			pass



		return {
		'metadata': {
			'success': success,
			'info': info,
			'report_json':response.json()
		},
		'elements': elements  # return the same thing back
		}
	def Create_Issue(self, payload):
		elements = payload["elements"]
		base_url = getattr(self.config, 'base_url', None)
		createissue_url = getattr(self.config,'create_issue', None)
		username = getattr(self.config, 'username', None)
		password = getattr(self.config, 'password', None)

		auth = 'Basic '+ base64.b64encode(username+':'+password)
		headers = {'Content-Type':'application/json','Authorization': auth }
		
		issue_send_url = base_url + createissue_url
		
		param={
				"fields":{
							"project"		:{
												"id":elements[0]["pro_id"]
											},
							"summary"		:	elements[0]["summary"],
							"issuetype"		:{
												"name": elements[0]["issuetype"]
											},
							"labels"		:[
												elements[0]["labels"]
											],
							"description"	:	elements[0]["description"],
						#	"duedate"		:	datetime.datetime.today().strftime('%Y-%m-%d')
						}
			}
		"""	
		{
			"alias":"jira",
			"token" : "SECURE-TOKEN-2-HERE" ,
			"action" : "Create_Issue" ,
			"payload": {"elements":[{"pro_id":"existing_project10103","summary":"CIAO ADDIOS","issuetype":"existing_issuetypeChange","labels":"Making_Out_nospace","description":"Cioa Addios, I'm done!!"}]}
		}
		"""
		success = False
		info = ""
		try:
			response = requests.post(issue_send_url,headers=headers,json=param)
			success = response.status_code == 201
			info = "created issue with id = "+ response.json()["id"]
		except:
			pass



		return {
		'metadata': {
			'success': success,
			'info': info,
			'report_json':response.json()
		},
		'elements': elements  # return the same thing back
		}
	def Delete_Issue(self, payload):
		elements = payload["elements"]
		base_url = getattr(self.config, 'base_url', None)
		deleteissue_url = getattr(self.config,'delete_issue', None)
		username = getattr(self.config, 'username', None)
		password = getattr(self.config, 'password', None)

		auth = 'Basic '+ base64.b64encode(username+':'+password)
		headers = {'Content-Type':'application/json','Authorization': auth }
		
		delete_send_url = base_url + deleteissue_url + '/' + elements[0]["id"]
		
		param={
				"deletesubtasks": "true"
			}
		"""	
		{
			"alias":"jira",
			"token" : "SECURE-TOKEN-2-HERE" ,
			"action" : "Delete_Issue" ,
			"payload": {"elements":[{"id":"existingID"}]}
		}
		"""
		success = False
		info = ""
		try:
			response = requests.delete(delete_send_url,headers=headers,json=param)
			success = response.status_code == 204
			info = "deleted issue with id = "+ elements[0]["id"]
		except:
			pass



		return {
		'metadata': {
			'success': success,
			'info': info,
			'report_json': ""
		},
		'elements': elements  # return the same thing back
		}
