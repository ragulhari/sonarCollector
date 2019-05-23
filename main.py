import MetricExtraction
import SonarExtractor
import schedule
import time


#TODO: Detect projects from Sonarqube
projects = ['mktzap-web-cetelem', 'kairos', 'kairos:publisher']


class SonarJobs:

    def run(self):
        print("Iniciando atualização...")
        extractor = SonarExtractor.SonarExtractor()
        extractor.getProjects()


sonar = SonarJobs()
sonar.run()

####Habilitar scheduler - descomente as linhas abaixo e comente as duas linhas acima

#schedule.every(1).minutes.do(SonarJobs().run)
#schedule.every(1).days.do(SonarJobs().run)


#while 1:
#    schedule.run_pending()
#    time.sleep(1)
