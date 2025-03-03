import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color:#778899; /* Light blue*/
    }
    </style>
    """,
    unsafe_allow_html=True
)

def length_converter(value, from_unit, to_unit):
    conversions = {
        "meter": 1,
        "kilometer": 0.001,
        "centimeter": 100,
        "millimeter": 1000,
        "mile": 0.000621371,
        "yard": 1.09361,
        "foot": 3.28084,
        "inch": 39.3701,
    }
    return value * (conversions[to_unit] / conversions[from_unit])

def weight_converter(value, from_unit, to_unit):
    conversions = {
        "kilogram": 1,
        "gram": 1000,
        "milligram": 1e6,
        "pound": 2.20462,
        "ounce": 35.274,
    }
    return value * (conversions[to_unit] / conversions[from_unit])

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return value

st.markdown("<h1 style='text-decoration: underline; text-align: center; font-weight: bold;'>UNIT CONVERTER APP</h1>", unsafe_allow_html=True)

st.title("🚀Welcome to Unit Converter!")
st.write("With the help of this you can easily convert different units.📖")
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

if category == "Length":
    from_unit = st.selectbox("From Unit", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    to_unit = st.selectbox("To Unit", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From Unit", ["kilogram", "gram", "milligram", "pound", "ounce"])
    to_unit = st.selectbox("To Unit", ["kilogram", "gram", "milligram", "pound", "ounce"])
    value = st.number_input("Enter Value", min_value=0.0, format="%.2f")
    if st.button("Convert"):
        result = weight_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter Value", format="%.2f")
    if st.button("Convert"):
        result = temperature_converter(value, from_unit, to_unit)
        st.markdown(f"<p class='result-text'>{value} {from_unit} is equal to {result:.4f} {to_unit}</p>", unsafe_allow_html=True)

        st.success(f"{value}° {from_unit} is equal to {result:.2f}° {to_unit}")
   
