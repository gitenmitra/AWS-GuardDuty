# Automation AWS-GuardDuty findings 
Get an SNS alert for High Severity GuardDuty findings<br><br>
Problem: Getting notified when there is Red finding in guardduty.
<BR><br>
Functionality: Solution is to trigger the CloudWatch event and send SNS to user when there is any findings with severity of greater than 7 in Guardduty.
<br><br>

<b>Architecture diagram</B><br><br>
<img src="https://github.com/gitenmitra/AWS/blob/main/GuardDutty.jpg?raw=true" alt="Architecture diagram" border="1">
