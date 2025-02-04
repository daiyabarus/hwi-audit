import xml.etree.ElementTree as ET
from dataclasses import fields
from typing import Any, Type


def extract_value(element: ET.Element) -> str:
    """
    Extracts the value from an XML element.
    Prioritizes the <!--string--> comment if present, otherwise uses the element's text.
    """
    if element is None:
        return "NA"

    # Extract the comment if it exists
    if element.tail and "<!--" in element.tail:
        comment = element.tail.strip()
        if comment.startswith("<!--") and comment.endswith("-->"):
            return comment[4:-3].strip()

    # Use the element's text if no comment is found
    return element.text.strip() if element.text else "NA"


def parse_xml(
    xml_string: str, attribute_class: Type[Any], root_tag: str, attributes_tag: str
) -> Any:
    """
    Parses the XML string and returns an object of the specified attribute_class.

    Args:
        xml_string (str): The XML string to parse.
        attribute_class (Type[Any]): The dataclass type for the attributes.
        root_tag (str): The root tag of the XML (e.g., "Cell").
        attributes_tag (str): The tag containing the attributes (e.g., "attributes").

    Returns:
        An instance of the attribute_class with parsed values.
    """
    root = ET.fromstring(xml_string)
    if root.tag != root_tag:
        raise ValueError(f"Expected root tag '{root_tag}', but found '{root.tag}'.")

    attributes_element = root.find(attributes_tag)
    if attributes_element is None:
        raise ValueError(f"No <{attributes_tag}> tag found in the XML.")

    # Extract all attributes
    attributes = {}
    for field in fields(attribute_class):
        element = attributes_element.find(field.name)
        attributes[field.name] = extract_value(element)

    return attribute_class(**attributes)
