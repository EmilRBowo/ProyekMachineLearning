# Laporan Proyek Machine Learning - Emil Reginald Bowo

## Domain Proyek
Domain yang dipilih untuk proyek machine learning ini adalah Energi, dengan judul Predictive Analytics: Pencurian Listrik
### Latar Belakang
![Transmisi Listrik](https://en.wikipedia.org/wiki/File:500kV_3-Phase_Transmission_Lines.png)
Pencurian listrik di Indonesia merupakan masalah yang cukup serius yang dapat berdampak pada sektor ekonomi, lingkungan, dan keselamatan. Pencurian ini sering terjadi di sektor rumah tangga, industri, hingga sektor komersial.Diperkirakan bahwa pencurian listrik menyebabkan kerugian sekitar 96 miliar dollar setiap tahun di industri listrik, dengan negara-negara berkembang menanggung sebagian besar beban ini, yang mencapai sekitar 60 miliar dollar per tahun.[[1]](https://doi.org/10.1109/tpwrs.2022.3162391) Konsumsi listrik ilegal sering kali menyebabkan ketidakseimbangan antara pasokan dan permintaan, yang menyulitkan perusahaan utilitas untuk mengelola sumber daya mereka dengan efektif.[[2]](https://doi.org/10.2478/amns-2024-0850)Penerapan predictive analysis atau analisis prediktif dalam industri distribusi listrik dapat menjadi solusi yang efektif untuk menghentikan pencurian listrik. Dengan menggunakan teknik analisis data yang canggih, industri distribusi listrik dapat memprediksi dan mendeteksi pola konsumsi listrik yang mencurigakan sebelum menjadi masalah besar. Dengan mengurangi insiden pencurian, perusahaan distribusi listrik dapat menstabilkan harga listrik bagi konsumen yang sah, sehingga memastikan bahwa biaya tidak dibebankan secara tidak proporsional kepada pengguna yang jujur.[[3]](https://doi.org/10.1155/2019/4136874)
## Business Understanding
Pengembangan model prediksi pencurian listrik memiliki potensi untuk memberikan manfaat bagi berbagai pihak, termasuk perusahaan utilitas dan konsumen. Model ini dapat membantu mengidentifikasi potensi pencurian listrik, mengurangi kerugian yang ditimbulkan, dan meningkatkan efisiensi distribusi energi. Contoh potensi manfaat dari hasil prediksi pencurian listrik yang akurat dapat membantu perusahaan utilitas dalam melakukan pemantauan dan intervensi lebih awal, serta mengoptimalkan pengelolaan sumber daya energi. 

### Problem Statements
Berdasarkan latar belakang, berikut rincian masalah:
- Bagaimana membuat model machine learning yang dapat memprediksi pencurian listrik berdasarkan data penggunaan listrik pelanggan?
- Model jenis apa yang memiliki akurasi paling baik?

### Goals

Tujuan dari project ini:
- Membuat model machine learning yang dapat memprediksi pencurian listrik dari penggunaan listrik selama sebulan
- Membandingkan algoritma dan memilih algoritma dengan akurasi paling baik

### Solution statements
- Membuat model KNN untuk memprediksi adanya pencurian listrik
- Membuat model Random Forest untuk memprediksi pencurian
- Membuat model Boosting algorithm untuk memprediksi pencurian

## Data Understanding
### Informasi Dataset
| **Jenis**     | **Keterangan**                                                                                     |
|---------------|----------------------------------------------------------------------------------------------------|
| **Title**     | SGCC Dataset                                                                                       |
| **Source**    | [Kaggle](https://www.kaggle.com/datasets/bensalem14/sgcc-dataset/data)                                                                                            |
| **Maintainer**| Bensalem14                                                                                         |
| **License**   | Database Contents License (DbCL) v1.0                                                              |
| **Visibility**| Publik                                                                                             |
| **Tags**      | Tabular, Energy, Government, Electricity, Binary Classification, China                              |
| **Usability** | 10.00                                                                                               |

Berikut ini contoh data pada dataset 
| 01/01/2014 | 01/02/2014 | ... | 1/24/2014 | 1/25/2014 | 1/26/2014 | CONS_NO                                    | FLAG |
|-------------|-------------|-----|-----------|-----------|-----------|-------------------------------------------|------|
| 2401.00     | 2500.00     | ... | 1774.00   | 2089.00   | 2272.00   | A0E791400CF1C48C43DC26A68227854A          | 1    |
| 3318.00     | 282.00      | ... | 3876.00   | 3228.00   | 96.00     | B415F931D3BFB17ACEF48BC648B04FC2          | 1    |
| 1020.80     | 1097.40     | ... | 1214.60   | 1285.40   | 1444.00   | DE8E1EAE4E578C0CEF92D1E23499888F          | 1    |

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- 01/01/2014 sampai 1/26/2014 : merupakan penggunaan listrik pelanggan per hari dalam kilowatt mulai dari tanggal 01/01/2014 sampai tanggal 1/26/2014.
- CONS_NO: merupakan nomor identifikasi pelanggan.
- FLAG: merupakan data apakah pelanggan teridentifikasi mencuri atau tidak. 0 berarti tidak terjadi pencurian dan 1 berarti terjadi pencurian

### Exploratory Data Analysis - Deskripsi Variabel
- Dataset berupa CSV (Comma-Seperated Values).
- Dataset memiliki 25863 sample dengan 26 fitur.
- Dataset memiliki 26 fitur bertipe float64 dan 1 fitur bertipe int64.
- Terdapat 122 missing value dalam dataset. 

### Exploratory Data Analysis - Univariate Analysis
![Gambar Analisis Univariate Kategori](https://drive.google.com/file/d/126HdOJhwIkC7KjNmDbZXdTnnEN8dX6xK/view?usp=drive_link)
Dapat dilihat pada gambar, terdapat 20152 untuk data 0 atau tidak terdeteksi pencurian dan 1889
untuk terdeteksi pencurian. Hal ini menunjukkan adanya ketidakseimbangan data yang cukup besar.
### Exploratory Data Analysis - Multivariate Analysis
![Gambar Analisis Multivariate Kategori](https://drive.google.com/file/d/1HRwlvs-jIe_Fmitj4iLdkjpN-KEqEQSs/view?usp=drive_link)
Dapat dilihat dari matriks korelasi, FLAG atau deteksi adanya pencurian atau tidak memiliki korelasi dengan data lainnya. Beberapa tanggal memiliki korelasi positif yang cukup besar dengan tanggal lainnya, contohnya tanggal 1/20 dengan 1/22.

## Data Preparation
Pada tahap **Persiapan Data**, dilakukan kegiatan seperti **Pengumpulan Data**, **Penilaian Data**, dan **Pembersihan Data**. Pada proses **Pengumpulan Data**, data diimpor dengan cara yang memungkinkan agar dapat dibaca dengan baik menggunakan dataframe Pandas. Untuk **Penilaian Data**, berikut beberapa pemeriksaan yang dilakukan:

- **Duplicate data** (data yang memiliki kesamaan dengan data lainnya).
- **Missing Value** (data atau informasi yang tidak ada atau tidak tersedia).
- **Outlier** (data yang jauh berbeda dari rata-rata kelompok data yang ada).

Pada proses Data Cleaning yang dilakukan adalah seperti membagi data menjadi data testing dan data uji.

Pada proyek ini terdapat data duplikat sebanyak 3820 sehingga dilakukan dropping. Dropping dilakukan untuk menjaga kualitas dan akurasi data. Nilai duplikat dapat menyebabkan distorsi dalam analisis dan model prediksi karena memberikan bobot yang berlebihan terhadap data yang sebenarnya identik. Dalam konteks statistik, duplikasi data dapat mempengaruhi perhitungan rata-rata, variansi, atau model prediktif yang mengandalkan distribusi data yang tepat.

Terdapat Missing Value sebanyak 122, kita gunakan interpolasi dengan mode linear untuk mengisi missing value tersebut. Interpolasi mode linier digunakan untuk data penggunaan listrik sebulan karena metode ini sederhana dan efektif dalam mengisi nilai yang hilang atau mengisi kekosongan data berdasarkan pola yang ada. Dengan interpolasi linier, nilai yang hilang diperkirakan dengan menggambar garis lurus antara dua titik data yang diketahui, yang mana sering kali sesuai dengan tren penggunaan listrik yang relatif stabil dalam jangka waktu tertentu.

Terdapat juga outlier yang cukup janggal pada kolom 1/13/2014, Nilai paling besar sangat jauh dari dataset lainnya dan tidak memungkinkan, yaitu lebih dari 80000. Pada 1/25/2014, Nilai paling besar adalah lebih dari 500000, sangat jauh dari data lain. Kita lakukan dropping terhadap kedua data tersebut untuk menjaga kualitas data.

Terdapat ketidakseimbangan data yang cukup besar pada dataset. Kita akan melakukan resampling dengan [LORAS](https://github.com/zoj613/pyloras). Metode LORAS membantu mengatasi masalah ketidaksesuaian kelas yang bisa terjadi dalam dataset. Ini sangat penting ketika menangani peristiwa langka seperti anomali ekstrem pada jaringan atau pola konsumsi yang tidak biasa. LORAS bertujuan untuk menyeimbangkan dataset dengan membuat titik data palsu di dekat batas antara kelas yang berbeda. 

Dalam proyek ini, digunakan Train Test Split dari library sklearn.model_selection untuk memisahkan dataset menjadi data latih dan data uji dengan proporsi 20:80 dan random state sebesar 42.

## Modeling
##### **KNN (K-Nearest Neighbors)**

**Keunggulan:**
1. **Sederhana dan Mudah Dipahami:** KNN mudah dipahami dan diimplementasikan karena hanya membutuhkan jarak antara titik data untuk membuat prediksi.
2. **Non-parametrik:** KNN tidak mengasumsikan bentuk distribusi data tertentu, sehingga cocok untuk berbagai jenis data.
3. **Tidak Memerlukan Pelatihan:** KNN adalah algoritma berbasis data sehingga tidak membutuhkan fase pelatihan, membuatnya cepat dalam beberapa kasus.

**Kelemahan:**
1. **Lambat pada Data Besar:** KNN bisa sangat lambat ketika digunakan pada dataset besar, karena harus menghitung jarak ke semua titik data setiap kali prediksi dilakukan.
2. **Sensitif terhadap Skala Data:** KNN sangat sensitif terhadap skala fitur, sehingga diperlukan normalisasi atau standarisasi data.
3. **Tidak Efektif pada Dimensi Tinggi:** KNN mungkin tidak efektif untuk dataset dengan dimensi tinggi (high-dimensional data) karena fenomena yang disebut "curse of dimensionality."

**Parameter yang Digunakan:**
- `n_neighbors`: Jumlah tetangga terdekat yang digunakan untuk prediksi.
- `n_jobs`: Jumlah prosesor yang digunakan untuk menjalankan perhitungan secara paralel. Set `-1` untuk menggunakan semua prosesor yang tersedia.

---

##### **Random Forest**

**Keunggulan:**
1. **Akurasi Tinggi:** Random Forest dapat menghasilkan model yang sangat akurat dengan menggabungkan banyak pohon keputusan.
2. **Mengurangi Overfitting:** Dengan membuat banyak pohon keputusan pada subset data dan fitur yang berbeda, Random Forest membantu mengurangi overfitting dibandingkan dengan pohon keputusan tunggal.
3. **Feature Importance:** Random Forest dapat memberikan informasi penting tentang fitur yang paling berpengaruh dalam model.

**Kelemahan:**
1. **Kompleksitas Model:** Random Forest menghasilkan model yang lebih kompleks dan sulit diinterpretasikan dibandingkan dengan model yang lebih sederhana.
2. **Lambat untuk Prediksi:** Karena melibatkan banyak pohon keputusan, proses prediksi bisa lebih lambat, terutama pada data yang sangat besar.
3. **Kebutuhan Memori:** Random Forest memerlukan lebih banyak memori untuk menyimpan banyak pohon keputusan.

**Parameter yang Digunakan:**
- `n_estimators`: Jumlah pohon keputusan dalam model random forest.
- `max_depth`: Kedalaman maksimal setiap pohon keputusan dalam random forest.

---

##### **Boosting Algorithm (Misalnya, AdaBoost, Gradient Boosting)**

**Keunggulan:**
1. **Akurasi Tinggi:** Boosting dapat meningkatkan akurasi model secara signifikan, terutama pada masalah klasifikasi dengan data yang tidak seimbang atau kompleks.
2. **Mengurangi Bias:** Dengan menambahkan pohon atau model yang lebih lemah secara bertahap, boosting efektif dalam mengurangi bias model.
3. **Penanganan Data Tidak Seimbang:** Beberapa algoritma boosting, seperti Gradient Boosting, dapat menangani data yang tidak seimbang dengan baik.

**Kelemahan:**
1. **Rentan terhadap Overfitting:** Jika tidak diatur dengan benar (misalnya, jumlah iterasi terlalu banyak), boosting bisa rentan terhadap overfitting.
2. **Proses Pelatihan Lambat:** Karena sifat iteratif dari boosting, pelatihan bisa memakan waktu, terutama pada dataset besar dan kompleks.
3. **Sensitif terhadap Noise:** Boosting dapat sangat sensitif terhadap data yang berisik (noise), dan dapat menghasilkan model yang kurang robust jika data yang digunakan mengandung banyak noise.

**Parameter yang Digunakan:**
- `estimator`: Model dasar yang digunakan sebagai estimasi awal, misalnya `DecisionTreeClassifier(max_depth=10)` untuk pohon keputusan dengan kedalaman maksimal 10.
- `n_estimators`: Jumlah tahap boosting yang digunakan, dalam hal ini 200 iterasi.
- `learning_rate`: Kecepatan langkah untuk setiap iterasi, yang mengontrol seberapa besar kontribusi setiap model baru terhadap prediksi akhir, diset ke 0.1.
- `random_state`: Nilai acak untuk memastikan hasil yang dapat direproduksi, diset ke 42.

## Evaluation
Karena kita ingin mendeteksi adanya pencurian listrik, dan kemudian mengirim petugas untuk mengecek apakah benar ada pencurian listrik, kita mnggunakan metrik recall. Sama seperti deteksi tumor, model diharapkan lebih banyak mendeteksi adanya pencurian yang kemudian akan diperiksa oleh ahli.
**Recall** adalah metrik yang digunakan untuk mengukur kemampuan model dalam mengidentifikasi semua data positif yang benar. Recall sering disebut sebagai **True Positive Rate** atau **Sensitivity**. Recall dihitung dengan rumus berikut:

`Recall = (TP) / (TP + FN) × 100`

#### Penjelasan:

- **TP (True Positive):** Jumlah data positif yang diprediksi dengan benar sebagai positif.
- **FN (False Negative):** Jumlah data positif yang diprediksi secara tidak benar sebagai negatif (Kesalahan Tipe II).

Recall menunjukkan seberapa banyak data positif yang berhasil diidentifikasi oleh model dibandingkan dengan jumlah data positif yang sebenarnya ada. Metrik ini sangat berguna saat kita ingin memastikan bahwa model tidak melewatkan data positif, terutama dalam kasus-kasus seperti deteksi penyakit atau deteksi pencurian, di mana kehilangan data positif dapat memiliki dampak yang serius.

Rumus ini membagi jumlah data yang diklasifikasikan dengan benar sebagai positif (TP) dengan jumlah seluruh data positif yang ada (TP + FN). Mengalikan dengan 100% mengubah rasio ini menjadi persentase.

| Model          | Recall   |
|----------------|----------|
| **KNN**        | 0.978593 |
| **RandomForest**| 0.965551 |
| **Boosting**   | 0.945128 |

Dari hasil dapat dilihat bahwa model KNN memiliki Recall terbaik sehingga paling cocok untuk deteksi pencurian listrik
## Referensi
[1] Khan, I. U., Javaid, N., Taylor, J. A., & Ma, X. (2023). Robust data driven analysis for electricity theft attack-resilient power grid. IEEE Transactions on Power Systems, 38(1), 537-548. https://doi.org/10.1109/tpwrs.2022.3162391
[2] Jia, S. (2024). Electric theft detection based on multilayer backpropagation neural network optimized by sine chaotic genetic algorithm. Applied Mathematics and Nonlinear Sciences, 9(1). https://doi.org/10.2478/amns-2024-0850
[3] Xu, D., Cui, M., Wei, F., Li, L., & Wei, W. (2024). A review of electricity theft detection technology. Tenth International Conference on Energy Materials and Electrical Engineering (ICEMEE 2024), 152. https://doi.org/10.1117/12.3050710


**---Ini adalah bagian akhir laporan---**


