from langchain.tools import tool
import json

@tool("json_validator", description=(
        "Validates JSON data against a schema or checks if a string is valid JSON. "
        "Input should be a JSON string to validate. Returns validation results "
        "indicating whether the JSON is well-formed and any errors found. "
        "Use this when you need to verify JSON syntax or structure before processing."))
def json_validation(json_string:str) -> str:
    """Validates if a string is valid JSON"""
    try:
        json.loads(json_string)
        return f"Valid JSON: The provided string is well formated JSON"

    except json.JSONDecodeError as e:
        return f"Invalid JSON: {str(e)}"