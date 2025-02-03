import xml.etree.ElementTree as ET
from dataclasses import fields
from typing import Any, Type


class XMLParser:
    """
    A class to parse XML strings into objects of a specified dataclass.
    """

    def __init__(
        self,
        xml_string: str,
        attribute_class: Type[Any],
        root_tag: str,
        attributes_tag: str,
    ):
        """
        Initializes the XMLParser with the XML string, attribute class, and tags.

        Args:
            xml_string (str): The XML string to parse.
            attribute_class (Type[Any]): The dataclass type for the attributes.
            root_tag (str): The root tag of the XML (e.g., "Cell").
            attributes_tag (str): The tag containing the attributes (e.g., "attributes").
        """
        self.xml_string = xml_string
        self.attribute_class = attribute_class
        self.root_tag = root_tag
        self.attributes_tag = attributes_tag

    def extract_value(self, element: ET.Element) -> str:
        """
        Extracts the value from an XML element.
        Prioritizes the <!--string--> comment if present, otherwise uses the element's text.

        Args:
            element (ET.Element): The XML element to extract the value from.

        Returns:
            str: The extracted value or "NA" if no value is found.
        """
        if element is None:
            return "NA"

        if element.tail and "<!--" in element.tail:
            comment = element.tail.strip()
            if comment.startswith("<!--") and comment.endswith("-->"):
                return comment[4:-3].strip()

        return element.text.strip() if element.text else "NA"

    def parse(self) -> Any:
        """
        Parses the XML string and returns an object of the specified attribute_class.

        Returns:
            An instance of the attribute_class with parsed values.

        Raises:
            ValueError: If the root tag or attributes tag is not found.
        """
        root = ET.fromstring(self.xml_string)
        if root.tag != self.root_tag:
            raise ValueError(
                f"Expected root tag '{self.root_tag}', but found '{root.tag}'."
            )

        attributes_element = root.find(self.attributes_tag)
        if attributes_element is None:
            raise ValueError(f"No <{self.attributes_tag}> tag found in the XML.")

        # Extract all attributes
        attributes = {}
        for field in fields(self.attribute_class):
            element = attributes_element.find(field.name)
            attributes[field.name] = self.extract_value(element)

        return self.attribute_class(**attributes)
