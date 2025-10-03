# Currency Converter Desktop Application

A responsive Python desktop application developed as part of university coursework to provide real-time currency conversion using an external REST API.

## 🌟 Key Features
* **Real-time Conversion**: Fetching live exchange rates for USD, EUR, GBP, JPY, and RON via the **Open Exchange Rates API**.
* **Quick Toggle**: A dedicated function to instantly swap source and target currencies.
* **User-Friendly GUI**: A modern and intuitive interface built with **Tkinter** and **ttk**.
* **Error Handling**: Comprehensive input validation and connectivity feedback using **messagebox** alerts.

## 🛠️ Technical Implementation
* **Language**: Python 3.x.
* **Libraries**:
    * `tkinter` & `ttk`: Used for structuring and styling the graphical user interface.
    * `requests`: Utilized for executing HTTP requests to the financial API.
* **Core Logic**:
    * Implemented a `convert_currency` function that calculates values based on dynamic API data.
    * Used the formula: `converted_value = (amount / source_rate) * target_rate`.
    * Applied a `dictionary=True` approach to process JSON responses from the API.

## 📂 Project Structure
* `Convertor_Valutar_Goran_Dimitrie.py`: Single-file integration of logic and GUI.
* `README.md`: Project documentation and setup guide.

## 🚀 How to Run
1. Ensure you have Python installed.
2. Install the required `requests` library:
   pip install requests

---
**Author:** Goran Dimitrie  
**Student @ ETTI UPB**