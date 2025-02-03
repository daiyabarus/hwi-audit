from dataclasses import asdict


def gs_cell(cell: str, nename: str, baseline_data: dict) -> list:
    """
    Compares the Cell attributes to the baseline data and generates the result.
    
    Args:
        cell (Cell): The Cell object to compare.
        nename (NENAME): The NENAME object containing NENAME and LMTVERSION.
        baseline_data (list): The baseline data to compare against.
    
    Returns:
        list: A list of dictionaries containing the comparison results.
    """
    results = []
    cell_attributes = asdict(cell.attributes)
    nename_attributes = asdict(nename.attributes)

    for baseline in baseline_data:
        if int(cell_attributes["DlEarfcn"]) == baseline["DlEarfcn"]:
            parameter = baseline["Parameter"]
            xml_value = cell_attributes.get(parameter, "N/A")
            npt_value = baseline["npt_value"]
            result = "Match" if str(xml_value) == str(npt_value) else "Mismatch"

            results.append({
                "NENAME": nename_attributes["NENAME"],
                "CellName": cell_attributes["CellName"],
                "DlEarfcn": cell_attributes["DlEarfcn"],
                "LocalCellId": cell_attributes["LocalCellId"],
                "MO": baseline["MO"],
                "Parameter": parameter,
                "xml_value": xml_value,
                "npt_value": npt_value,
                "result": result
            })
    
    return results    return results