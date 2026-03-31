import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as ticker
from pathlib import Path

# Load data
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'

df_day = pd.read_csv(DATA_DIR / 'day.csv')
df_hour = pd.read_csv(DATA_DIR / 'hour.csv')

# Data Cleaning
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])
df_day['dteday'] = pd.to_datetime(df_day['dteday'])

# Mapping season
season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
df_hour['season'] = df_hour['season'].map(season_mapping)
df_day['season'] = df_day['season'].map(season_mapping)

# Mapping weather
weather_mapping = {1: 'Clear', 2: 'Mist', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Snow'}
df_hour['weathersit'] = df_hour['weathersit'].map(weather_mapping)
df_day['weathersit'] = df_day['weathersit'].map(weather_mapping)

# Mapping month
month_mapping = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 
                 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
df_hour['mnth'] = df_hour['mnth'].map(month_mapping)
df_day['mnth'] = df_day['mnth'].map(month_mapping)

# Mapping weekday
weekday_mapping = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
df_hour['weekday'] = df_hour['weekday'].map(weekday_mapping)
df_day['weekday'] = df_day['weekday'].map(weekday_mapping)

# Streamlit Dashboard
st.set_page_config(page_title="Dashboard Analisis Data Sepeda", layout="wide")
st.title('Dashboard Analisis Data Sepeda')

# Sidebar filters
st.sidebar.header('Filter Data')

min_date = df_hour['dteday'].min().date()
max_date = df_hour['dteday'].max().date()
selected_date_range = st.sidebar.date_input(
    'Rentang Tanggal',
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(selected_date_range) != 2:
    st.warning('Pilih rentang tanggal awal dan akhir untuk menampilkan data.')
    st.stop()

start_date, end_date = selected_date_range

season_order = ['Spring', 'Summer', 'Fall', 'Winter']
weather_order = ['Clear', 'Mist', 'Light Snow/Rain', 'Heavy Rain/Snow']
weekday_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

available_seasons = [s for s in season_order if s in df_hour['season'].dropna().unique()]
available_weather = [w for w in weather_order if w in df_hour['weathersit'].dropna().unique()]
available_weekdays = [d for d in weekday_order if d in df_hour['weekday'].dropna().unique()]

selected_seasons = st.sidebar.multiselect('Season', available_seasons, default=available_seasons)
selected_weather = st.sidebar.multiselect('Cuaca', available_weather, default=available_weather)
selected_weekdays = st.sidebar.multiselect('Hari', available_weekdays, default=available_weekdays)

workingday_choice = st.sidebar.selectbox('Tipe Hari', ['Semua', 'Hari Kerja', 'Hari Libur'])

filtered_df_hour = df_hour[
    (df_hour['dteday'].dt.date >= start_date) &
    (df_hour['dteday'].dt.date <= end_date) &
    (df_hour['season'].isin(selected_seasons)) &
    (df_hour['weathersit'].isin(selected_weather)) &
    (df_hour['weekday'].isin(selected_weekdays))
].copy()

if workingday_choice == 'Hari Kerja':
    filtered_df_hour = filtered_df_hour[filtered_df_hour['workingday'] == 1]
elif workingday_choice == 'Hari Libur':
    filtered_df_hour = filtered_df_hour[filtered_df_hour['workingday'] == 0]

if filtered_df_hour.empty:
    st.warning('Tidak ada data yang sesuai dengan filter. Ubah filter untuk melihat visualisasi.')
    st.stop()

filtered_df_hour['workingday_label'] = filtered_df_hour['workingday'].map({0: 'Hari Libur', 1: 'Hari Kerja'})

sns.set_style("whitegrid")
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

# Question 1: Pola Penyewaan Hari Kerja vs Hari Libur
st.subheader("Pola Penyewaan Sepeda per Jam Berdasarkan Hari Kerja vs Hari Libur")

fig1, ax1 = plt.subplots(figsize=(12, 6))

sns.lineplot(
    x='hr', y='cnt',
    data=filtered_df_hour,
    hue='workingday_label',
    hue_order=['Hari Libur', 'Hari Kerja'],
    marker='o',
    ci=None,
    palette=['#999999', '#1f77b4'],  # libur vs kerja
    ax=ax1
)

ax1.set_title('Pola Penyewaan Sepeda per Jam', fontsize=16, weight='bold')
ax1.set_xlabel('Jam (0-23)')
ax1.set_ylabel('Rata-Rata Penyewaan')
ax1.set_xticks(range(0, 24))

ax1.legend(title='Tipe Hari')
ax1.grid(alpha=0.3)

st.pyplot(fig1)

# Question 2: Pengguna Casual vs Registered
st.subheader("Perbandingan Aktivitas Penyewaan Sepeda per Jam: Registered vs Casual")

hourly_user_type = filtered_df_hour.groupby('hr').agg({'casual': 'mean', 'registered': 'mean'}).reset_index()

fig2, ax2 = plt.subplots(figsize=(12, 6))

sns.lineplot(
    x='hr', y='registered',
    data=hourly_user_type,
    marker='o',
    label='Registered',
    color='#1f77b4',
    ax=ax2
)

sns.lineplot(
    x='hr', y='casual',
    data=hourly_user_type,
    marker='o',
    label='Casual',
    color='#ff7f0e',
    ax=ax2
)

ax2.set_title('Registered vs Casual per Jam', fontsize=16, weight='bold')
ax2.set_xlabel('Jam (0-23)')
ax2.set_ylabel('Rata-Rata Penyewaan')
ax2.set_xticks(range(0, 24))
ax2.grid(alpha=0.3)

st.pyplot(fig2)

# Analisis Lanjutan: Blok Waktu
st.subheader("Analisis Lanjutan: Penyewaan Berdasarkan Blok Waktu")

def get_time_category(hour):
    if 0 <= hour < 6:
        return 'Dini Hari'
    elif 6 <= hour < 12:
        return 'Pagi'
    elif 12 <= hour < 18:
        return 'Sore'
    else:
        return 'Malam'

filtered_df_hour['time_category'] = filtered_df_hour['hr'].apply(get_time_category)

time_group_analysis = filtered_df_hour.groupby('time_category').agg(
    {'casual': 'sum', 'registered': 'sum', 'cnt': 'sum'}
).reindex(['Dini Hari', 'Pagi', 'Sore', 'Malam'])

time_group_analysis['cnt'] = time_group_analysis['cnt'].fillna(0)

fig3, ax3 = plt.subplots(figsize=(10, 5))

colors = ['#bbbbbb', '#bbbbbb', '#ff7f0e', '#bbbbbb']  # highlight SORE

sns.barplot(
    x=time_group_analysis.index,
    y='cnt',
    data=time_group_analysis,
    palette=colors,
    ax=ax3
)

ax3.set_title('Total Penyewaan per Blok Waktu', fontsize=16, weight='bold')
ax3.set_xlabel('Blok Waktu')
ax3.set_ylabel('Total Penyewaan')

# format angka
ax3.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

# label angka
label_offset = max(time_group_analysis['cnt'].max() * 0.02, 1)
for i, v in enumerate(time_group_analysis['cnt']):
    ax3.text(i, v + label_offset, f"{v:,.0f}", ha='center', fontsize=10)

# highlight insight langsung di chart
if (time_group_analysis['cnt'] > 0).any():
    top_idx = time_group_analysis['cnt'].idxmax()
    top_pos = ['Dini Hari', 'Pagi', 'Sore', 'Malam'].index(top_idx)
    ax3.text(top_pos, time_group_analysis.loc[top_idx, 'cnt'] + (label_offset * 6),
             'Tertinggi', ha='center', color='red', fontsize=11, weight='bold')

st.pyplot(fig3)