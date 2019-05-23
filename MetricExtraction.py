class MetricExtraction:
    code_smells = ""                    #Número total de code smells da ferramenta
    new_technical_debt = ""             #Débito técnico acrescentado a partir da última versão
    blocker_violations = ""     
    bugs = ""                           #Número de bugs
    coverage = ""                       #Responde à questão: Quanto de código fonte foi coberto por testes unitários?
    new_coverage = ""                   #Incremento de código coberto (ver item "coverage")
    critical_violations = ""            
    violations = ""                     #Contagem total de violações do código
    line_coverage = ""
    sqale_rating = ""
    major_violations = ""
    minor_violations = ""
    new_code_smells = ""                #Número de novos code smells levantados
    new_blocker_violations = ""
    new_bugs = ""                       #Número de novos bugs
    new_critical_violations = ""
    new_violations = ""                 #Número de novas violações de código
    new_line_coverage = ""              #Densidade de linhas cobertas por unit tests. Medido por (Linhas cobertas / Linhas executáveis)
    new_major_violations = ""
    new_minor_violations = ""           
    vulnerabilities = ""                #Número de vulnerabilidades
    new_vulnerabilities = ""            #Número de novas vulnerabilidades
    sqale_index = ""                    #Esforço em MINUTOS para corrigir todos os code smells da solução. Assume o dia como tendo 8 horas
    false_positive_issues = ""          #Número de issues marcados como "falso positivo"
    sqale_debt_ratio = ""               #Indicador que demonstra a taxa entre construir um novo código ou corrigir o legado, sendo < 1 a correção o mais indicado.
    reliability_remediation_effort = "" #Esforço em MINUTOS para corrigir todos os bugs
    tests = ""                          #Número de testes unitários

    def composeMetric(self, metric_name, metric_value):

        if metric_name == "code_smells":
            self.code_smells = metric_value
        if metric_name == "new_technical_debt":
            self.new_technical_debt = metric_value
        if metric_name == "blocker_violations":
            self.blocker_violations = metric_value
        if metric_name == "bugs":
            self.bugs = metric_value
        if metric_name == "coverage":
            self.coverage = metric_value
        if metric_name == "new_coverage":
            self.new_coverage = metric_value
        if metric_name == "critical_violations":
            self.critical_violations = metric_value
        if metric_name == "violations":
            self.violations = metric_value
        if metric_name == "line_coverage":
            self.line_coverage = metric_value
        if metric_name == "sqale_rating":
            self.sqale_rating = metric_value
        if metric_name == "major_violations":
            self.major_violations = metric_value
        if metric_name == "minor_violations":
            self.minor_violations = metric_value
        if metric_name == "new_code_smells":
            self.new_code_smells = metric_value
        if metric_name == "new_blocker_violations":
            self.new_blocker_violations = metric_value
        if metric_name == "new_bugs":
            self.new_bugs = metric_value
        if metric_name == "new_critical_violations":
            self.new_critical_violations = metric_value
        if metric_name == "new_violations":
            self.new_violations = metric_value
        if metric_name == "new_line_coverage":
            self.new_line_coverage = metric_value
        if metric_name == "new_major_violations":
            self.new_major_violations = metric_value
        if metric_name == "new_minor_violations":
            self.new_minor_violations = metric_value
        if metric_name == "vulnerabilities":
            self.vulnerabilities = metric_value
        if metric_name == "new_vulnerabilities":
            self.new_vulnerabilities = metric_value
        if metric_name == "sqale_index":
            self.sqale_index = metric_value
        if metric_name == "false_positive_issues":
            self.false_positive_issues = metric_value
        if metric_name == "sqale_debt_ratio":
            self.sqale_debt_ratio = metric_value
        if metric_name == "reliability_remediation_effort":
            self.reliability_remediation_effort = metric_value
        if metric_name == "tests":
            self.tests = metric_value