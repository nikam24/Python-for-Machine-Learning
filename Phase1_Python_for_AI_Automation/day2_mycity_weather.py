import requests 
import openpyxl 
from datetime import datetime 
import os 

CITY = "Parbhani" 
API_KEY = os.getenv("WEATHER_API_KEY")
EXCEL_FILE = "weather_data.xlsx"

def get_weather():
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={CITY}" 
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        if "current" in data: 
            temp = data["current"]["temperature"] 
            description = data["current"]["weather_descriptions"][0] 
            humidity = data["current"]["humidity"] 
            return temp, description, humidity 
        else:
            raise Exception(f"Error in API response: {data.get('error', {}).get('info', 'Unknown error')}") 
    else: 
        raise Exception(f"Failed to fetch weather data: {response.status_code}h")

def save_to_excel(temperature, description, humidity):
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(EXCEL_FILE): 
        wb = openpyxl.Workbook() 
        sheet = wb.active 
        sheet.title = "Weather Data" 
        sheet.append(["Date", "Temperature (°C)", "Description", "Humidity (%)"]) 
        wb.save(EXCEL_FILE) 
    
    wb = openpyxl.load_workbook(EXCEL_FILE) 
    sheet = wb.active 
    sheet.append([today, temperature, description, humidity]) 
    wb.save(EXCEL_FILE)

if __name__ == "__main__": 
    try:
        temperature, desc, humidity = get_weather() 
        save_to_excel(temperature, desc, humidity) 
        print(f"Weather data for {CITY} saved successfully!")
    except Exception as e:
        print(f"Error: {e}")