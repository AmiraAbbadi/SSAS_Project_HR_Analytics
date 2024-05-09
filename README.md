[Version finale du projet.pdf](https://github.com/AmiraAbbadi/SSAS_Project_HR_Analytics/files/15267986/Version.finale.du.projet.pdf)
Idée de Projet : Analyse de la Rétention des Employés

Objectif : L'objectif de ce projet est d'analyser les facteurs qui influent sur la rétention des employés au sein d'une entreprise afin d'identifier les mesures à prendre pour améliorer la rétention du personnel.
Table de dimension
 Employee :
•	EmployeeID (Clé primaire)
•	Age (Âge de l'employé)
•	AgeGroup (Groupe d'âge de l'employé)
•	Attrition (Si l'employé a quitté l'entreprise ou non)
•	Department (Département dans lequel l'employé travaille)
•	Education (Niveau d'éducation de l'employé)
•	EducationField (Domaine d'éducation de l'employé)
•	Gender (Genre de l'employé)
•	MaritalStatus (Statut matrimonial de l'employé)
•	Over18 (Si l'employé est majeur)
•	OverTime (Si l'employé fait des heures supplémentaires ou non)
 Date :
•	DateID (Clé primaire)
•	Date (Date)
•	Year (Année)
•	Month (Mois)
•	DayOfMonth (Jour du mois)
Table de faits 
ExperienceFact :
•	RemunerationID : Identifiant de la rémunération (clé primaire)
•	EmployeeID : Identifiant de l'employé (clé étrangère faisant référence à la table de dimension Employee)
•	DateID (Clé étrangère vers la table Date)
•	SalarySlab : Tranche de salaire
•	MonthlyIncome : Revenu mensuel
•	PercentSalaryHike : Pourcentage d'augmentation de salaire
•	MonthlyRate : Taux mensuel
SatisfactionFact :
•	SatisfactionID (Clé primaire)
•	EmployeeID (Clé étrangère vers la table Employee)
•	DateID (Clé étrangère vers la table Date)
•	JobSatisfaction (Satisfaction du travail de l'employé)
•	EnvironmentSatisfaction (Satisfaction de l'environnement de travail de l'employé)
•	RelationshipSatisfaction (Satisfaction des relations au travail de l'employé)
•	WorkLifeBalance (Équilibre entre vie professionnelle et vie personnelle de l'employé)
•	DistanceFromHome (Distance entre le domicile de l'employé et son lieu de travail)
•	BusinessTravel (Fréquence des voyages professionnels de l'employé)
1.	Les attributs :

•	EmpID (clé primaire) : Identifiant de l’employé. Valeur unique pour chaque employé.
•	Age : Âge de l’employé. Valeurs possibles sont des nombres entiers.
•	AgeGroup : Groupe d’âge de l’employé. Valeurs possibles sont des plages d’âge comme “26-35”, “36-45”, etc.
•	Attrition : Attrition de l’employé. Valeurs possibles sont “Yes” (oui) ou “No” (non).
•	BusinessTravel : Fréquence des voyages d’affaires de l’employé. Valeurs possibles sont “Travel_Rarely”, “Travel_Frequently”, “Non-Travel”.
•	DailyRate : Taux journalier de l’employé. Valeurs possibles sont des nombres entiers.
•	Department : Département de l’employé. Valeurs possibles sont “Sales”, “Research & Development”, “Human Resources”.
•	DistanceFromHome : Distance entre le domicile et le lieu de travail de l’employé. Valeurs possibles sont des nombres entiers.
•	Education : Niveau d’éducation de l’employé. Valeurs possibles sont des nombres entiers.
•	EducationField : Domaine d’éducation de l’employé. Valeurs possibles sont “Life Sciences”, “Medical”, “Marketing”, “Technical Degree”, etc.
•	EmployeeCount : Nombre d’employés. Valeurs possibles sont des nombres entiers.
•	EmployeeNumber : Numéro de l’employé. Valeur unique pour chaque employé.
•	EnvironmentSatisfaction : Satisfaction de l’environnement de l’employé. Valeurs possibles sont des nombres entiers.
•	Gender : Sexe de l’employé. Valeurs possibles sont “Male”, “Female”.
•	HourlyRate : Taux horaire de l’employé. Valeurs possibles sont des nombres entiers.
•	JobInvolvement : Implication dans le travail de l’employé. Valeurs possibles sont des nombres entiers.
•	JobLevel : Niveau de poste de l’employé. Valeurs possibles sont des nombres entiers.
•	JobRole : Rôle de l’employé. Valeurs possibles sont “Sales Executive”, “Research Scientist”, “Laboratory Technician”, “Manufacturing Director”, “Healthcare Representative”, etc.
•	JobSatisfaction : Satisfaction professionnelle de l’employé. Valeurs possibles sont des nombres entiers.
•	MaritalStatus : Statut marital de l’employé. Valeurs possibles sont “Single”, “Married”, “Divorced”.
•	MonthlyIncome : Revenu mensuel de l’employé. Valeurs possibles sont des nombres entiers.
•	SalarySlab : Tranche de salaire de l’employé. Valeurs possibles sont “Upto 5k”, “5k-10k”, “10k-15k”, etc.
•	MonthlyRate : Taux mensuel de l’employé. Valeurs possibles sont des nombres entiers.
•	NumCompaniesWorked : Nombre d’entreprises dans lesquelles l’employé a travaillé. Valeurs possibles sont des nombres entiers.
•	Over18 : Si l’employé a plus de 18 ans. Valeurs possibles sont “Y” (oui) ou “N” (non).
•	OverTime : Si l’employé fait des heures supplémentaires. Valeurs possibles sont “Yes” (oui) ou “No” (non).
•	PercentSalaryHike : Pourcentage d’augmentation de salaire de l’employé. Valeurs possibles sont des nombres entiers.
•	PerformanceRating : Évaluation de la performance de l’employé. Valeurs possibles sont des nombres entiers.
•	RelationshipSatisfaction : Satisfaction relationnelle de l’employé. Valeurs possibles sont des nombres entiers.
•	StandardHours : Heures standard de l’employé. Valeurs possibles sont des nombres entiers.
•	StockOptionLevel : Niveau d’option d’achat d’actions de l’employé. Valeurs possibles sont des nombres entiers.
•	TotalWorkingYears : Nombre total d’années de travail de l’employé. Valeurs possibles sont des nombres entiers.
•	TrainingTimesLastYear : Nombre de fois que l’employé a été formé l’année dernière. Valeurs possibles sont des nombres entiers.
•	WorkLifeBalance : Équilibre entre vie professionnelle et vie privée de l’employé. Valeurs possibles sont des nombres entiers.
•	YearsAtCompany : Nombre d’années passées par l’employé dans l’entreprise. Valeurs possibles sont des nombres entiers.
•	YearsInCurrentRole : Nombre d’années passées par l’employé dans son rôle actuel. Valeurs possibles sont des nombres entiers.
•	YearsSinceLastPromotion : Nombre d’années depuis la dernière promotion de l’employé. Valeurs possibles sont des nombres entiers.
•	YearsWithCurrManager : Nombre d’années passées par l’employé avec son manager actuel. Valeurs possibles sont des nombres entiers.




![diagram](https://github.com/AmiraAbbadi/SSAS_Project_HR_Analytics/assets/167568387/32ad544d-73f7-4b4b-97f4-19bc8a6951b4)

