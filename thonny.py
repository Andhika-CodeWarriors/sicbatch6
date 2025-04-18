import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

# Info Ubidots
ACCESS_TOKEN = 'BBUS-vybSbBCszADtYwPCypmmuDEsKfgZ6'
DEVICE_LABEL = 'code-warriors'
VARIABLE_LABEL = 'jarak'

# URL yang sudah diperbarui
url = f"https://industrial.api.ubidots.com/api/v2.0/devices/code-warriors/jarak/values/"

headers = {
    "X-Auth-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

# Fungsi ambil data
def get_data():
    response = requests.get(url, headers=headers)
    print(response.status_code)  # Cek status code dari API
    if response.status_code == 200:
        data = response.json()
        print(data)  # Cek format data JSON yang diterima
        if 'results' in data and len(data['results']) > 0:
            return data['results']
        else:
            st.error("Data tidak ditemukan di Ubidots.")
            return None
    else:
        st.error(f"Gagal mengambil data: {response.status_code}")
        return None

# Tampilan Streamlit
st.set_page_config(page_title="Dashboard Banjir", layout="centered")
st.title("🌊 Real-time Monitoring Ketinggian Air")

# Refresh otomatis tiap 5 detik
st_autorefresh(interval=5000, key="data_refresh")

# Ambil data
data = get_data()
if data:
    latest = data[0]['value']
    st.metric(label="Tinggi Air Saat Ini (cm)", value=f"{latest:.2f}")
else:
    st.error("Gagal mengambil data dari Ubidots.")