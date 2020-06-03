# Fm_Staging_automation

# README #
This is the Automation repository for the feature Live Stream (Live Commerce)
Done in Python 3.8

## How do I get set up? ##

Download and install Python version 3.6 or above  
[Python](https://www.python.org/downloads/)  


```mkdir testing```  
```cd testing ```  
Use Git or checkout with SVN using the web URL.  
```git clone https://github.com/akashgkrishnan/Fm_Staging_automation.git```


Change In to the Directory with requirements.txt  

Open CMD/Terminal  

```pip install -r requirements.txt```  

This will install all the required Dependencies

Change in to the Tests Directory and  
### Run the command : ###
```py.test -v -s```

### For generating HTML report ###
``` py.test -v -s --html=report.html```



## Jenkins Integration 


## CheckList 

Check VPN Connection  
Check Port Forwarding For DB  
Check DB connection code in Base class

## jenkins set up 
Install Java  
click and download [Download Jenkins](http://mirrors.jenkins.io/war-stable/latest/jenkins.war)

Open the folder where the jenkins.war is downloaded  
Open CMD/Terminal on the location  
Enter the command  

```java -jar jenkins.war```    

select project as github project

Add choice parameter  
Under Choice Parameter set the choices as  
QA1  
QA2  

Add Git parameter  for branch  

Add string paramter with name count default = 1

select windows batch command/ shell command and enter the following commands

```buildoutcfg
cd API_Automation
cd Tests
py.test -v -s --count=%count% --html=$WORKSPACE\API_Automation\reports\report.html --junitxml="result.xml"
```

Post Build completion  
Open Workspace and move into the reports folder and open report.html  
