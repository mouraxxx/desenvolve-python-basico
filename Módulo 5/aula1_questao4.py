import datetime

agora = datetime.datetime.now()

dia = agora.day
mes = agora.month
ano = agora.year
hora = agora.hour
minuto = agora.minute

print(f"Data: {dia:02d}/{mes:02d}/{ano}")
print(f"Hora: {hora:02d}:{minuto:02d}")