# Automation AWS-GuardDuty findings 
Get an SNS alert for High Severity GuardDuty findings<br><br>
<b>Problem:</B> Getting notified when there is Red finding in AWS GuardDuty.
<BR><br>
<b>Functionality:</B> Solution is to trigger the CloudWatch event and send SNS to user when there is any findings with severity of greater than 7 in Guardduty.
<br><br>

<b>Architecture diagram</B><br><br>
<img src="https://github.com/gitenmitra/AWS/blob/main/GuardDutty.jpg?raw=true" alt="Architecture diagram" border="1">
<br><br>
<b>How to Run the Script :</B> Create a Lambda function called "GuardDutyAlert" the run-time version Python 3.6 or above by using the attach code. 
Creation of the Lambda function will in turn create CloudWatch Logs groups for its logging.
Lamda can be call every 5 mins or as per your business requirement. <br><br>
<b>Prerequisite</b>: GuardDuty must be enabled on your account 
