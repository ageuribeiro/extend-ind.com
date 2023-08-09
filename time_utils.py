import pytz
from datetime import datetime

def convert_to_timezone(dt, timezone):
    source_timezone = pytz.timezone('UTC')  # Fuso horário de origem (pode variar)
    target_timezone = pytz.timezone(timezone)  # Fuso horário de destino
    localized_dt = source_timezone.localize(dt)
    target_dt = localized_dt.astimezone(target_timezone)
    return target_dt