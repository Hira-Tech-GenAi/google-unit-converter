# unit_converter.py
from typing import Dict, List, Union

class UnitConverter:
    def __init__(self) -> None:
        self.conversions: Dict[str, Dict[str, Union[float, str]]] = {
            "length": {
                "meter": 1.0,
                "kilometer": 1000.0,
                "centimeter": 0.01,
                "millimeter": 0.001,
                "inch": 0.0254,
                "foot": 0.3048,
                "yard": 0.9144,
                "mile": 1609.34,
            },
            "mass": {
                "kilogram": 1.0,
                "gram": 0.001,
                "milligram": 0.000001,
                "pound": 0.453592,
                "ounce": 0.0283495,
            },
            "temperature": {
                "celsius": "C",
                "fahrenheit": "F",
                "kelvin": "K",
            },
            "area": {
                "square meter": 1.0,
                "square kilometer": 1000000.0,
                "square centimeter": 0.0001,
                "square foot": 0.092903,
                "square inch": 0.00064516,
            },
            "volume": {
                "cubic meter": 1.0,
                "liter": 0.001,
                "milliliter": 0.000001,
                "gallon (US)": 0.00378541,
                "quart (US)": 0.000946353,
                "pint (US)": 0.000473176,
                "fluid ounce (US)": 2.95735e-5,
            },
        }

    def get_available_units(self) -> List[str]:
        units: List[str] = []
        for category in self.conversions:
            units.extend(self.conversions[category].keys())
        return sorted(list(set(units)))

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        from_category: Union[str, None] = None
        to_category: Union[str, None] = None

        for cat, unit_map in self.conversions.items():
            if from_unit in unit_map:
                from_category = cat
            if to_unit in unit_map:
                to_category = cat

        if from_category is None or to_category is None:
            raise KeyError("Invalid unit provided.")

        if from_category != to_category:
            if from_category == "temperature" and to_category == "temperature":
                if from_unit == "celsius" and to_unit == "fahrenheit":
                    return (value * 9/5) + 32
                elif from_unit == "celsius" and to_unit == "kelvin":
                    return value + 273.15
                elif from_unit == "fahrenheit" and to_unit == "celsius":
                    return (value - 32) * 5/9
                elif from_unit == "fahrenheit" and to_unit == "kelvin":
                    return (value - 32) * 5/9 + 273.15
                elif from_unit == "kelvin" and to_unit == "celsius":
                    return value - 273.15
                elif from_unit == "kelvin" and to_unit == "fahrenheit":
                    return (value - 273.15) * 9/5 + 32
                elif from_unit == to_unit:
                    return value
            else:
                raise ValueError(f"Cannot convert between {from_category} and {to_category}.")

        if from_category in ["length", "mass", "area", "volume"]:
            from_value_base: float = float(self.conversions[from_category][from_unit])
            to_value_base: float = float(self.conversions[to_category][to_unit])
            return value * (from_value_base / to_value_base)
        else:
            raise ValueError(f"Conversion for {from_category} not fully implemented.")

if __name__ == "__main__":
    converter = UnitConverter()
    print("Available units:", converter.get_available_units())
    print(f"10 meters in feet: {converter.convert(10.0, 'meter', 'foot')}")
    print(f"100 grams in kilograms: {converter.convert(100.0, 'gram', 'kilogram')}")
    print(f"25 Celsius in Fahrenheit: {converter.convert(25.0, 'celsius', 'fahrenheit')}")