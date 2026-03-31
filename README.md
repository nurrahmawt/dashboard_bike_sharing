# Proyek Analisis Data: Bike Sharing Dashboard

Dashboard ini dibuat menggunakan Streamlit untuk menampilkan hasil analisis dataset Bike Sharing dari file `day.csv` dan `hour.csv`.

## Struktur Proyek
- `dashboard.py` : aplikasi dashboard Streamlit
- `Proyek_Analisis_Data.ipynb` : notebook analisis data
- `day.csv` : data agregasi harian
- `hour.csv` : data agregasi per jam

## 1) Prasyarat
Pastikan sudah terpasang:
- Python 3.9+ (disarankan Python 3.10 atau 3.11)
- `pip`

## 2) Setup Environment (Windows PowerShell)
Jalankan perintah berikut dari folder proyek:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install pandas matplotlib seaborn streamlit
```

Jika PowerShell memblokir aktivasi venv, jalankan sekali:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## 3) Menjalankan Dashboard
Masih dari folder proyek, jalankan:

```powershell
streamlit run dashboard.py
```

Setelah itu buka URL lokal yang muncul di terminal (umumnya `http://localhost:8501`).

## 4) Menjalankan Notebook (Opsional)
Jika ingin membuka analisis versi notebook:

```powershell
jupyter notebook
```

Lalu buka `Proyek_Analisis_Data.ipynb`.

## 5) Troubleshooting
- Error `FileNotFoundError`:
	Pastikan command dijalankan dari folder yang sama dengan `dashboard.py`, `day.csv`, dan `hour.csv`.
- Error `AttributeError: 'tuple' object has no attribute 'savefig'`:
	Pastikan `st.pyplot(...)` menerima objek figure matplotlib, bukan tuple.
- Port Streamlit sudah dipakai:

```powershell
streamlit run dashboard.py --server.port 8502
```

## Author
Nur Rahmawati