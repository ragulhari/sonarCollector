import requests
import json
import MetricExtraction
import datetime
import os
from dbHandler import DatabaseHandler

#Configuração do ambiente Sonarqube 
MEASURES_CALL_ENDPOINT = "/api/measures/component?"
PROJECTS_CALL_ENDPOINT = "/api/projects/search"

#Documentação dos indicadores (v. 7.7): https://docs.sonarqube.org/latest/user-guide/metric-definitions
class SonarExtractor: 

    def loadConfigs(self):

        fileReader = open(os.path.dirname(os.path.abspath(__file__)) + "/configs.json","r")
        return fileReader.read()        


    def getProjects(self):

        configData = self.loadConfigs()

        projects_url = configData["configs"]["sonarqube"]["domain"] + PROJECTS_CALL_ENDPOINT
        sonar_token = configData["configs"]["sonarqube"]["token"]

        headers = {"Content-Type": "application/json"}
        response = requests.get(projects_url, headers=headers, auth=(sonar_token, ''))

        if response.status_code == 200:
            
            jsonRetorno = json.loads(response.content.decode('utf-8'))

            if jsonRetorno.get("components") is not None:
                projectList = jsonRetorno["components"]

                for project in projectList:

                    project_key = ""
                    project_last_analysis = ""
                    last_update_recorded = ""

                    if project.get("key") is not None:
                        project_key = project["key"]
                    if project.get("lastAnalysisDate") is not None:
                        project_last_analysis = datetime.datetime.strptime(project["lastAnalysisDate"], "%Y-%m-%dT%H:%M:%S+%f")

                    db = DatabaseHandler()
                    
                    last_update_recorded = db.getProjectLastUpdate(project_key)
                    if last_update_recorded is not None:
                        last_update_recorded = datetime.datetime.strptime(last_update_recorded)
                    print(project_last_analysis)
                    if last_update_recorded is None or last_update_recorded != project_last_analysis:
                        print("OI")
                        self.getMeasures(project_key, project_last_analysis)


    def getMeasures(self, projectName, project_last_analysis):
        repo = ""                           #Key do Repositório
        repo_name = ""                      #Nome do repositório
        
        extraction = MetricExtraction.MetricExtraction()

        configData = self.loadConfigs()

        measures_url = configData["configs"]["sonarqube"]["domain"] + MEASURES_CALL_ENDPOINT

        api_url = measures_url + "component=" + projectName + "&metricKeys=code_smells,new_technical_debt,blocker_violations,bugs,coverage,new_coverage,critical_violations,violations,line_coverage,sqale_rating,major_violations,minor_violations,new_code_smells,new_blocker_violations,new_bugs,new_critical_violations,new_violations,new_line_coverage,new_major_violations,new_minor_violations,vulnerabilities,new_vulnerabilities,sqale_index,false_positive_issues,sqale_debt_ratio,reliability_remediation_effort,tests"
        headers = {"Content-Type": "application/json"}
    
        print (api_url)

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            
            jsonRetorno = json.loads(response.content.decode('utf-8'))

            if jsonRetorno.get("component") is not None:
                if jsonRetorno["component"].get("key") is not None:
                    repo = jsonRetorno["component"]["key"]
                if jsonRetorno["component"].get("name") is not None:
                    repo_name = jsonRetorno["component"]["name"]

                metrics = ""

                if jsonRetorno["component"].get("measures") is not None:
                    metrics = jsonRetorno["component"]["measures"]

                    for metric in metrics:

                        metric_name = ""
                        metric_value = ""

                        if metric.get("metric") is not None:
                            metric_name = metric["metric"]

                        if metric.get("value") is not None:
                            metric_value = metric["value"]

                        else:

                            if metric.get("periods") is not None:
                                periods = metric["periods"]
                                
                                index = 0

                                for period in periods:
                                    if index < int(period["index"]):
                                        index = int(period["index"])
                                        metric_value = period["value"]

                        extraction.composeMetric(metric_name, metric_value)
                                

            db = DatabaseHandler()
            db.insertMetric(repo, repo_name, project_last_analysis, extraction)


        else:
            print(response.status_code)
                
