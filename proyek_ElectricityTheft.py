# -*- coding: utf-8 -*-
"""Proyek Dicooding

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q0E5PFR0mhm_LvZMUSBzreoeNWaRXnlx

#Predictive Analysis: Pencurian Listrik

---
(oleh: [Emil Reginald Bowo](https://www.linkedin.com/in/emilrbowo/))
###Deskripsi Proyek
Tujuan dari proyek ini adalah untuk mengembangkan model machine learning yang bisa memprediksi apakah pelanggan melakukan pencurian listrik dengan input penggunaan listrik mereka selama 1 bulan.

##1. Import Library yang digunakan
"""

!pip install pyloras
import pyloras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import f1_score, roc_auc_score, classification_report
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier
import seaborn as sns

"""## 2. Data Understanding
### 2.1 Data Loading
Untuk data sendiri didapat dari kaggle dengan judul "SGCC Electricity Theft Detection" yaitu dataset imbalance mengenai pencurian listrik. Dataset berasal dari [Kaggle](https://www.kaggle.com/datasets/bensalem14/sgcc-dataset/data)
#### Informasi Dataset

| **Jenis**     | **Keterangan**                                                                                     |
|---------------|----------------------------------------------------------------------------------------------------|
| **Title**     | SGCC Dataset                                                                                       |
| **Source**    | Kaggle                                                                                             |
| **Maintainer**| Bensalem14                                                                                         |
| **License**   | Database Contents License (DbCL) v1.0                                                              |
| **Visibility**| Publik                                                                                             |
| **Tags**      | Tabular, Energy, Government, Electricity, Binary Classification, China                              |
| **Usability** | 10.00           
Kita download dulu datanya.

"""

import kagglehub

# Download latest version
path = kagglehub.dataset_download("bensalem14/sgcc-dataset")

print("Path to dataset files:", path)

# Path to the CSV file
file_path = "/root/.cache/kagglehub/datasets/bensalem14/sgcc-dataset/versions/1/datasetsmall.csv"

# Load the CSV into a DataFrame
df = pd.read_csv(file_path)

"""### 2.2 Exploratory Data Analysis (EDA)
#### 2.2.1 EDA - Deskripsi Variabel
"""

df

"""Dapat kita lihat bahwa pada dataset terdapat kolom berisi penggunaan listrik pelanggan selama sebulan, kemudian ada nomor konsumen. Di kolom terakhir ada Flag, dimana apabila Flag bernilai 1 maka pelanggan itu melakukan pencurian listrik, sementara apabila 0 maka tidak ada pencurian. Karena nomer konsumen tidak penting, kita drop kolom tersebut"""

df = df.drop(columns=['CONS_NO'])

df.info()

"""Dapat kita lihat pada data penggunaan merupakan bentuk float sementara flag bentuk integer"""

df.describe()

"""Fungsi `describe()` memberikan ringkasan statistik untuk setiap kolom dalam dataset. Berikut adalah informasi yang disediakan:

- **Count**: Jumlah sampel atau data dalam kolom tersebut.
- **Mean**: Nilai rata-rata dari data.
- **Std**: Standar deviasi, yang menunjukkan seberapa besar data menyebar dari rata-rata.
- **Min**: Nilai terkecil dalam kolom.
- **25%**: Kuartil pertama, yaitu batas yang memisahkan 25% data terendah dari sisanya.
- **50%**: Kuartil kedua atau median, yaitu nilai tengah dari data yang telah diurutkan.
- **75%**: Kuartil ketiga, batas yang memisahkan 75% data terendah dari 25% data tertinggi.
- **Max**: Nilai terbesar dalam kolom.
"""

df.shape

"""Untuk baris ada 25863 dan 27 kolom

### 2.2.2 Menangani outlier, duplicated data, dan missing value
"""

df.duplicated().sum()

"""Dapat kita lihat, ada 3820 data yang merupakan duplikasi.

Kita lihat apakah ada data yang kosong pada dataset
"""

df.isnull().sum()

"""Dapat kita lihat masih banyak nilai yang kosong pada dataset.

Kita lihat apakah ada outlier yang janggal pada dataset
"""

df_outlier=df.select_dtypes(exclude=['object'])
for column in df_outlier:
        plt.figure()
        sns.boxplot(data=df_outlier, x=column)

print(df['1/13/2014'].max())
print(df['1/25/2014'].max())

"""Dapat dilihat dari grafik, pada kolom 1/13/2014, Nilai paling besar sangat jauh dari dataset lainnya dan tidak memungkinkan, yaitu lebih dari 80000. Pada 1/25/2014, Nilai paling besar adalah lebih dari 500000, sangat jauh dari data lain.

### 2.2.3 EDA Univariate Analysis
"""

df.hist(bins=10, figsize=(20,15))
plt.show()

plt.figure(figsize=(15, 15))
correlation_matrix = df.corr().round(2)

sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title(f"Matriks Korelasi ", size=20)

"""Pada data terdapat imbalance data yang dapat membuat model machine learning tidak dapat memprediksi data yang sedikit dengan baik."""

class_counts = df['FLAG'].value_counts()
class_counts

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

X, y = df.iloc[:, :-1], df['FLAG']

sns.countplot(x=df['FLAG'])
plt.title('Data Imbalance pada terdeteksi atau tidak', fontsize=14)

"""### 3. Data Preparation
#### 3.1 Data Cleaning

Melakukan drop terhadap duplicates.
"""

df.drop_duplicates(inplace=True)

df.duplicated().sum()

"""Melakukan interpolasi untuk mengisi data yang kosong"""

df.interpolate(method='linear', inplace=True)

""" Kita gunakan interpolasi dengan metode linear, karena dataset merupakan penggunaan listrik setiap hari selama sebulan kita dapat menggunakan interpolasi linear untuk mengisi kosongnya data."""

df.isnull().sum()

"""Melakukan drop terhadap outlier yang terlalu besar."""

max_value_index=df['1/13/2014'].idxmax()
df = df.drop(index=max_value_index)
max_value_index=df['1/25/2014'].idxmax()
df = df.drop(index=max_value_index)

"""Kita cek apakah outlier sudah dihapus"""

df_outlier=df.select_dtypes(exclude=['object'])
for column in df_outlier:
        plt.figure()
        sns.boxplot(data=df_outlier, x=column)

"""#### 3.2 Data Balancing
Untuk mengatasi data imbalance, kita dapat menggunakan [LORAS](https://github.com/zoj613/pyloras) untuk mengatasinya. Metode LORAS membantu mengatasi masalah ketidakseimbangan kelas yang dapat terjadi dalam dataset. Hal ini sangat penting terutama saat menangani peristiwa langka, seperti anomali grid ekstrem atau pola konsumsi yang tidak biasa. LORAS berfungsi menyeimbangkan dataset dengan membuat titik data sintetis di dekat batas antara berbagai kelas. Metode ini dapat meningkatkan kinerja model machine learning untuk analisis prediktif dan mendeteksi outlier dalam konteks aktivitas jaringan listrik pada dataset SGCC.
"""

loras = pyloras.LORAS()
X, y = df.iloc[:, :-1], df['FLAG']
X_balanced, y_balanced = loras.fit_resample(X, y)

sns.countplot(x=y_balanced)
plt.title('Data Balanced pada terdeteksi atau tidak', fontsize=14)

"""#### 3.3 Train-Test-Split"""

X_train, X_test, y_train, y_test = train_test_split(X_balanced, y_balanced, test_size=0.2, random_state=42)

print(f'Total datasets: {len(X_balanced)}')
print(f'Total data Latih: {len(X_train)}')
print(f'Total data Uji: {len(X_test)}')

"""## 4. Model Development
### 4.1 KNN (K-Nearest Neighbour)
"""

# Siapkan dataframe untuk analisis model
trainmodels = pd.DataFrame(index=['accuracy','recall','precision', 'F1'],
                      columns=['KNN', 'RandomForest', 'Boosting'])

testmodels = pd.DataFrame(index=['accuracy','recall','precision', 'F1'],
                      columns=['KNN', 'RandomForest', 'Boosting'])

from sklearn.neighbors import KNeighborsClassifier

# Initialize KNeighborsClassifier with desired parameters
knn = KNeighborsClassifier(n_neighbors=10, n_jobs=-1)  # You can adjust 'n_neighbors' based on your dataset
knn.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, classification_report, confusion_matrix
y_pred = knn.predict(X_train)
trainmodels.loc['accuracy','KNN'] = accuracy_score(y_train, y_pred)
trainmodels.loc['recall','KNN'] = recall_score(y_train, y_pred)
trainmodels.loc['precision','KNN'] = precision_score(y_train, y_pred)
trainmodels.loc['F1','KNN'] = f1_score(y_train, y_pred)

"""#### 4.2 Random Forest"""

from sklearn.ensemble import RandomForestClassifier
# buat model prediksi
RF = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=55, n_jobs=-1)
RF.fit(X_train, y_train)

trainmodels.loc['accuracy','RandomForest'] = accuracy_score(y_train, RF.predict(X_train))
trainmodels.loc['recall','RandomForest'] = recall_score(y_train, RF.predict(X_train))
trainmodels.loc['precision','RandomForest'] = precision_score(y_train, RF.predict(X_train))
trainmodels.loc['F1','RandomForest'] = f1_score(y_train, RF.predict(X_train))

"""### 4.3 Boosting Algorithm"""

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
# Define the Bagging Classifier
boosting_model = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=10),  # Base estimator
    n_estimators=200,  # Number of boosting stages
    learning_rate=0.1,  # Step size
    random_state=42     # Random seed
)

# Train the model
boosting_model.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, classification_report, confusion_matrix
y_pred = boosting_model.predict(X_train)
trainmodels.loc['accuracy','Boosting'] = accuracy_score(y_train, y_pred)
trainmodels.loc['recall','Boosting'] = recall_score(y_train, y_pred)
trainmodels.loc['precision','Boosting'] = precision_score(y_train, y_pred)
trainmodels.loc['F1','Boosting'] = f1_score(y_train, y_pred)

"""### 5. Evaluasi Model

#### 5.1 Skor model
"""

trainmodels

"""Dapat dilihat dari hasil evaluasi terhadap test dataset, KNN memiliki hasil recall paling baik"""

model_dict = {'KNN': knn, 'RandomForest': RF, 'Boosting': boosting_model}
for name, model in model_dict.items():
    y_pred = model.predict(X_test)
    testmodels.loc['accuracy',name] = accuracy_score(y_test, y_pred)
    testmodels.loc['recall',name] = recall_score(y_test, y_pred)
    testmodels.loc['precision',name] = precision_score(y_test, y_pred)
    testmodels.loc['F1',name] = f1_score(y_test, y_pred)
testmodels

"""#### 5.2 Grafik evaluasi"""

train_recall = trainmodels.loc['recall']
test_recall = testmodels.loc['recall']
combined_accuracy = pd.DataFrame({
    'Test Recall': test_recall,
    'Train Recall': train_recall
})

combined_accuracy = combined_accuracy.sort_values(by='Train Recall', ascending=True)
fig, ax = plt.subplots(figsize=(10, 6))
combined_accuracy.plot(kind='barh', ax=ax, zorder=3, color=['darkblue', 'orange'])
ax.grid(zorder=0)
plt.title('Model Recall Comparison (Train vs Test)', fontsize=16)
plt.xlabel('Recall', fontsize=14)
plt.ylabel('Models', fontsize=14)
plt.show()

"""Dapat dilihat bahwa metode KNN merupakan metode paling bagus untuk memprediksi apakah ada pencurian listrik."""
