#@author: Giten Mitra
#Date: 21 May 2022
#Description: 

# Import the SDK
import boto3
from pprint import pprint

# Clients
clientGD = boto3.client('guardduty')
clientSNS = boto3.client('sns')

# Obtain Detector ID - GD is regional Service
def gd_detector():
	try:
		paginator = clientGD.get_paginator('list_detectors')
		response_iterator_GD_detector = paginator.paginate()
		for response in response_iterator_GD_detector:
			for k,v in response.items():
				if k == "DetectorIds":
					if v == []:
						continue
					else:
						detectorID = (v[0])
				else:
					continue
		list_findings(detectorID=detectorID)
	except Exception as error:
		print (str(error))

# Obtain the Findings ID that matched the filter criteria
def list_findings(detectorID):
	try:
		finding_lst = []
		paginator = clientGD.get_paginator('list_findings')
		response_iterator_list_findings = paginator.paginate(DetectorId=detectorID,
			FindingCriteria={
	        'Criterion': {
	            'severity': {
	                'Gt': 7,
	                'Lt': 9,
	            },
	            'service.archived': {
	            'Eq': [
	            'false',
	            ],
	            }
	        }
	    })
		for response in response_iterator_list_findings:
			for k,v in response.items():
				if k == "FindingIds":
					if v == []:
						continue
					else:
						for list_v in v:
							findingID = (list_v)
							finding_lst.append(findingID)
				else:
					continue
		get_finding(findingID=finding_lst,detectorID=detectorID)
	except Exception as error:
		print (str(error))

# Describe Findings IDs
def get_finding(findingID,detectorID):
	try:
		response = clientGD.get_findings(DetectorId=detectorID,FindingIds=findingID)
		for k,v in response.items():
			if k == "Findings":
				if v == []:
					continue
				else:
					for value in v:
						sns_notification(ID=(value["Id"]))
			else:
				continue
	except Exception as error:
		print (str(error))

# Send SNS notification
def sns_notification(ID):
	try:
		response = clientSNS.publish(
		TopicArn='arn:aws:sns:ap-southeast-1:111111111111:GuardDuty-Findings',
        Message=' !!Warning!! - You have GuardDuty finding ID: '+ str(ID) + 'in MEDIUM and HIGH Category,Please review and close it asap',
        Subject='GuardDuty Severity Warning!!'
        )
	except Exception as error:
		print (str(error))

gd_detector()
