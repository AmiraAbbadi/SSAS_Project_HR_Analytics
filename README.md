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
lien colab pour partie exploration des données : https://colab.research.google.com/drive/1j9EVVXux60SXXrCDBGxF2Sb7vShWRbno?usp=sharing


![diagram](https://github.com/AmiraAbbadi/SSAS_Project_HR_Analytics/assets/167568387/32ad544d-73f7-4b4b-97f4-19bc8a6951b4)

