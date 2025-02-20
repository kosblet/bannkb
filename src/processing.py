from datetime import datetime
from typing import Dict, List


def filter_operations(operation_list: List[Dict], status: str = 'EXECUTED') -> List[Dict]:
    """
    Filters the list of operation dictionaries by the given status.

    Args:
        operation_list (List[Dict]): List of operation dictionaries.
        status (str): The status to filter by. Default is 'EXECUTED'.

    Returns:
        List[Dict]: Filtered list of operation dictionaries.
    """
    return [entry for entry in operation_list if entry.get('state') == status]

def sort_operations_by_date(
    operation_list: List[Dict], descending: bool = True
) -> List[Dict]:
    """
    Sorts the list of operation dictionaries by the date.

    Args:
        operation_list (List[Dict]): List of operation dictionaries.
        descending (bool): Sort order. Default is True (descending). If False, the list will be
                          sorted in ascending order by date.

    Returns:
        List[Dict]: Sorted list of operation dictionaries.
    """
    return sorted(
        operation_list,
        key=lambda x: datetime.fromisoformat(x['date']),
        reverse=descending
    )
