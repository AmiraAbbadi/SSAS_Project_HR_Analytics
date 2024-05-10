# -*- coding: utf-8 -*-
"""ProjectHR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j9EVVXux60SXXrCDBGxF2Sb7vShWRbno

# Importation des bibliothèques
"""

import numpy as np # est une bibliothèque pour effectuer des calculs numériques
import pandas as pd # est une bibliothèque pour la manipulation et l'analyse des données.
import matplotlib.pyplot as plt # utilisée pour la visualisation des données.
import seaborn as sns # utilisée pour la visualisation des données.

"""# Chargement des données"""

HRData = pd.read_csv('/content/HR_Analytics.csv')
# charger un jeu de données de hr à partir d'un fichier CSV en utilisant
#la fonction read_csv de la bibliothèque Pandas.

"""# Exploration des données"""

HRData.head() # Afficher par défaut les cinq premières lignes du DataFrame

HRData.shape # Afficher tuple qui représente les dimensions du DataFrame

HRData.info() # Afficher des informations sur le DataFrame

HRData.isnull().sum() # Afficher le nombre de valeurs nulles pour chaque colonne de votre DataFrame

"""# visualisation des données"""

colunas = ['WorkLifeBalance','TrainingTimesLastYear','StockOptionLevel',
    'RelationshipSatisfaction','PerformanceRating','NumCompaniesWorked',
   'JobInvolvement', 'JobLevel', 'JobSatisfaction',
   'EnvironmentSatisfaction','Education']

plt.figure(figsize=(9,36))
for i,col in enumerate(colunas):
    axes = plt.subplot(13,2, i + 1)
    sns.countplot(x=HRData [col], hue=HRData ['Gender'], palette=['#ED72A3','#8565F0'])
plt.tight_layout()
plt.show()