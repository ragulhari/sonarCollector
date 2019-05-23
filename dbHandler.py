import pymysql
import json
from pymongo import MongoClient
from datetime import datetime
from MetricExtraction import MetricExtraction
import os

class Configs:

    def loadBDConfigs(self):

        fileReader = open(os.path.dirname(os.path.abspath(__file__)) + "/configs.json","r")
        return fileReader.read()        

class DatabaseHandler:

    def getConnection(self):

        loadConfigs = Configs()
        jsonConfigs = json.loads(loadConfigs.loadBDConfigs())

        cnx = pymysql.connect(user=jsonConfigs["configs"]["db"]["user"], 
                            password=jsonConfigs["configs"]["db"]["password"],
                            host=jsonConfigs["configs"]["db"]["host"],
                            port=jsonConfigs["configs"]["db"]["port"],
                            database=jsonConfigs["configs"]["db"]["database"])
        return cnx

    def executeOperation(self, query, dataTuple, needsCommit=False):
        obj = self.getConnection()
        cursor = obj.cursor()
        if (needsCommit == False):
            cursor.execute(query, dataTuple)
            return cursor
        else:
            obj.cursor().execute(query, dataTuple)
            obj.commit()

    def insertMetric(self,repo,repo_name,project_last_analysis,metric):
        add_sonar_data = ("INSERT INTO sonar_data (date,project_last_analysis,repo,repo_name,code_smells,new_technical_debt,blocker_violations,bugs,coverage,new_coverage,critical_violations,violations,line_coverage,sqale_rating,major_violations,minor_violations,new_code_smells,new_blocker_violations,new_bugs,new_critical_violations,new_violations,new_line_coverage,new_major_violations,new_minor_violations,vulnerabilities,new_vulnerabilities,sqale_index,false_positive_issues,sqale_debt_ratio,reliability_remediation_effort,tests) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        return self.executeOperation(add_sonar_data, (datetime.now().strftime("%Y-%m-%d"),project_last_analysis,repo,repo_name,metric.code_smells,metric.new_technical_debt,metric.blocker_violations,metric.bugs,metric.coverage,metric.new_coverage,metric.critical_violations,metric.violations,metric.line_coverage,metric.sqale_rating,metric.major_violations,metric.minor_violations,metric.new_code_smells,metric.new_blocker_violations,metric.new_bugs,metric.new_critical_violations,metric.new_violations,metric.new_line_coverage,metric.new_major_violations,metric.new_minor_violations,metric.vulnerabilities,metric.new_vulnerabilities,metric.sqale_index,metric.false_positive_issues,metric.sqale_debt_ratio,metric.reliability_remediation_effort,metric.tests),True)


    def getProjectLastUpdate(self, project_code):
        select_last_task = "SELECT project_last_analysis FROM sonar_data WHERE repo = %s ORDER BY date desc limit 1"

        project_data = self.executeOperation(select_last_task, (project_code)).fetchone()

        if project_data is not None:
            return project_data[0]
        else:
            return None
