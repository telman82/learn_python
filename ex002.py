
incident_number = "INC-20482"
system = "Процессинг платежей"
error_count = 37
lost_trx_amount = 12500.00
escalation = True

print(f"Инцидент {incident_number} | Система: {system}")
lost_trx_amount = 12500.00

# Два знака после запятой
print(f"Средняя сумма: {lost_trx_amount:.2f} руб.")
# → Средняя сумма: 12500.00 руб.

# С разделителем тысяч
big_amount = 1250000.50
print(f"Сумма: {big_amount:,.2f} руб.")
# → Сумма: 1,250,000.50 руб.