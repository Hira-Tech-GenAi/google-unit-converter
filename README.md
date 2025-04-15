
# 🌐 Google Unit Converter

A sleek, user-friendly **unit conversion tool** built with Python and Streamlit. This app allows you to convert values between a wide range of **units** across categories like length, mass, temperature, area, and volume — all in an interface inspired by Google's minimalism.

![Unit Converter](https://img.shields.io/badge/Built%20With-Streamlit-blue?style=flat&logo=streamlit)  
![Python Version](https://img.shields.io/badge/Python-3.9+-brightgreen?style=flat&logo=python)

---

## 🚀 Features

- 🔢 Convert between a wide variety of **units** (e.g., meters to feet, Celsius to Fahrenheit, gallons to liters)
- 🌡️ **Temperature conversions** are handled with custom logic
- 💡 Clear, interactive **Streamlit interface**
- 🎯 Fast and accurate conversion logic using a centralized `UnitConverter` class
- 🎨 Modern and responsive UI

---

## 📁 Project Structure

```
unit-converter/
├── app.py                  # Streamlit frontend
├── unit_converter.py       # Core conversion logic
└── README.md               # Project documentation
```

---

## 🛠️ How It Works

The logic is handled by the `UnitConverter` class in `unit_converter.py`. It supports conversions in the following categories:

- **Length**: meter, kilometer, inch, foot, yard, mile, etc.
- **Mass**: kilogram, gram, pound, ounce, etc.
- **Temperature**: Celsius, Fahrenheit, Kelvin
- **Area**: square meter, square foot, square inch, etc.
- **Volume**: liter, milliliter, gallon, pint, etc.

The frontend (`app.py`) provides an intuitive interface built with Streamlit, allowing users to input values, choose source and target units, and view results instantly.

---

## 📦 Installation

Make sure you have Python 3.9+ installed.

1. **Clone the repository**

```bash
https://github.com/Hira-Tech-GenAi/google-unit-converter.git
cd google-unit-converter
```

2. **Install dependencies**

```bash
pip install streamlit
```

3. **Run the app**

```bash
streamlit run app.py
```

---

## 🧪 Example Conversions

- `10 meters` → `feet` → ✅ `32.8084 ft`
- `100 grams` → `kilograms` → ✅ `0.1 kg`
- `25 Celsius` → `Fahrenheit` → ✅ `77.0 °F`

---

## ⚠️ Disclaimer

This is a basic unit converter for general purposes. It may not include all units or advanced conversions. For more precision-critical or scientific applications, consider using specialized tools.

---

## ❤️ Credits

Built with 💖 by **Hira Khalid** using Python & Streamlit.  
Feel free to fork, improve, and share!

---

## 📃 License

This project is licensed under the [MIT License](LICENSE).

