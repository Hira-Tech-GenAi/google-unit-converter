# app.py
import streamlit as st
from unit_converter import UnitConverter
from typing import Dict, List, Tuple

#? Initialize the UnitConverter
converter = UnitConverter()

#? --- Attractive UI ---
st.set_page_config(
    page_title="Google Unit Converter",
    page_icon=":ruler:",
    layout="wide",
)

st.title(":blue[Google] :orange[Unit] :green[Converter]")
st.markdown("A simple and elegant unit converter powered by Python.")
st.markdown("---")

with st.container():
    col_input, col_output = st.columns(2)

    with col_input:
        st.subheader("Enter Value and Units:")
        value: float = st.number_input("Value", value=1.0)
        from_unit: str = st.selectbox("From Unit", converter.get_available_units())

    with col_output:
        st.subheader("Select Target Unit:")
        to_unit: str = st.selectbox("To Unit", converter.get_available_units())

st.markdown("---")

#? Conversion button
if st.button("Convert", use_container_width=True):
    try:
        result: float = converter.convert(value, from_unit, to_unit)
        st.subheader("Conversion Result:")
        st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
    except ValueError as e:
        st.error(f"Error: {e}")
    except KeyError as e:
        st.error(f"Error: Invalid unit: {e}")

#? Information and Disclaimer
st.markdown("---")
st.info("This is a basic unit converter and may not support all possible units or complex conversions.")
st.info("For more advanced conversions, please refer to dedicated online tools.")
st.markdown("---")
st.markdown("Developed with :heart: and Streamlit")