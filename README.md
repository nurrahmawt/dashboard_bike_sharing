# 🚲 Bike Sharing Data Analysis

## 📌 Project Overview

Proyek ini bertujuan untuk menganalisis pola penyewaan sepeda menggunakan dataset **Bike Sharing**. Analisis difokuskan pada perilaku pengguna berdasarkan waktu (jam), tipe pengguna, serta kondisi hari (hari kerja vs hari libur).

---

## ❓ Business Questions

1. Bagaimana perbedaan pola penyewaan sepeda antara hari kerja dan hari libur pada setiap jamnya?
2. Pada jam berapa pengguna *casual* paling aktif dibandingkan pengguna *registered*?

---

## 🛠️ Tools & Libraries

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit

---

## 📊 Data Wrangling

### Data Source

Dataset yang digunakan:

* `hour.csv` (data per jam)
* `day.csv` (data per hari)

### Data Assessment

* Tidak terdapat missing values
* Tidak ditemukan data duplikat
* Tipe data `dteday` dikonversi menjadi datetime
* Terdapat outlier pada data per jam (normal karena pola rush hour)

### Data Cleaning

* Konversi tipe data tanggal
* Mapping kategori:

  * Season (Spring, Summer, Fall, Winter)
  * Weather (Clear, Mist, Rain, dll)
  * Month & Weekday menjadi label

---

## 🔍 Exploratory Data Analysis (EDA)

### 1. Pola Penyewaan Berdasarkan Jam

* Puncak penyewaan terjadi pada:

  * **08:00 (pagi)**
  * **17:00–18:00 (sore)**
* Menunjukkan penggunaan untuk aktivitas commuting

### 2. Hari Kerja vs Hari Libur

* Hari kerja memiliki rata-rata penyewaan lebih tinggi
* Hari libur menunjukkan pola lebih stabil dan rekreatif

### 3. Pengaruh Cuaca

* Cuaca cerah → penyewaan tinggi
* Hujan/salju → penyewaan turun drastis (>60%)

---

## 📈 Visualization & Insights

### Perbandingan Hari Kerja vs Libur

* Hari kerja → pola **bimodal (rush hour)**
* Hari libur → puncak di siang hari (12:00–15:00)

### Perbandingan Casual vs Registered

* **Registered** dominan di jam sibuk
* **Casual** lebih aktif di siang hari (11:00–16:00)

---

## 🧠 Key Insights

* Sepeda banyak digunakan sebagai alat transportasi kerja
* Pengguna casual lebih condong ke aktivitas rekreasi
* Faktor cuaca sangat memengaruhi permintaan
* Waktu sore menjadi periode dengan aktivitas tertinggi

---

## 📊 Interactive Dashboard

Aplikasi dashboard interaktif dibuat menggunakan Streamlit untuk eksplorasi data secara real-time.

👉 **Akses Dashboard:**
[Bike-Sharing] https://dashboardbikesharing-mepyvosjvht8v5yttgut8p.streamlit.app/

---

## 🚀 How to Run

1. Clone repository

```bash
git clone https://github.com/username/bike-sharing-analysis.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run Streamlit

```bash
streamlit run dashboard.py
```

---

## 📌 Conclusion

* Pola penggunaan sepeda sangat dipengaruhi oleh waktu dan jenis hari
* Hari kerja menunjukkan pola commuting yang jelas
* Pengguna casual lebih aktif di jam santai
* Insight ini dapat digunakan untuk strategi operasional dan pemasaran

---

## 📎 Notes

Project ini merupakan bagian dari submission analisis data menggunakan Python dan visualisasi interaktif.