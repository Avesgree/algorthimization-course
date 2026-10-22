def generate_report(orders: list[dict[str, float]]) -> dict[str, float]:
    """Считает общую выручку кафе по списку заказов.

    Args:
        orders: Список словарей с данными метрик.

    Returns:
        Словарь с итоговой выручкой.
    """
    total_revenue = sum(order.get("total", 0.0) for order in orders)
    return {"total_revenue": total_revenue}


def format_title(text: str, width: int = 40) -> str:
    """Центрирует заголовок отчета и оформляет его рамкой.

    Args:
        text: Текст заголовка для форматирования.
        width: Полная ширина строки. По умолчанию 40.

    Returns:
        Готовая строка, дополненная знаками равно по краям.
    """
    return text.center(width, "=")
