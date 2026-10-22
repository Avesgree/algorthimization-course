from typing import List, Dict

def generate_report(orders: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Генерирует отчет по заказам в кафе.
    
    :param orders: Список словарей с данными заказов.
    :return: Словарь с итоговыми метриками.
    """
    total_revenue = sum(order.get("total", 0.0) for order in orders)
    return {"total_revenue": total_revenue}
