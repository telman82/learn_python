# Строка (str) — текст
incident_id = "INC-20481"
status = "в работе"

# Целое число (int) — счётчик, ID
priority = 2
affected_users = 150

# Дробное число (float) — суммы, проценты
transaction_amount = 45230.50
sla_compliance = 98.7

# Булево значение (bool) — да/нет, включено/выключено
is_critical = True
escalated = False

# Вывод на экран
print(f"Инцидент {incident_id}, приоритет {priority}")
print(f"Затронуто пользователей: {affected_users}")
print(f"Критический: {is_critical}")