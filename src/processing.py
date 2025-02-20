from datetime import datetime
from typing import Dict, List


def filter_by_state(
    operations: List[Dict], state: str = 'EXECUTED'
) -> List[Dict]:
    """
    Фильтрует список словарей операций по заданному состоянию.
    Args:
        operations (List[Dict]): Список словарей операций.
        state (str): Состояние для фильтрации. По умолчанию 'EXECUTED'.
    Returns:
        List[Dict]: Отфильтрованный список словарей операций.
    """

    return [op for op in operations if op.get('state') == state]


def sort_by_date(
    operations: List[Dict], descending: bool = True
) -> List[Dict]:
    """
    Сортирует список словарей операций по дате.
    Args:
        operations (List[Dict]): Список словарей операций.
        descending (bool): Порядок сортировки. По умолчанию True (по убыванию).
    Returns:
        List[Dict]: Отсортированный список словарей операций.
    """

    return sorted(
        operations,
        key=lambda x: datetime.fromisoformat(x['date']),
        reverse=descending
    )
