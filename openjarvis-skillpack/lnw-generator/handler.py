"""Leistungsnachweis (Performance Record) Draft Generator."""
from datetime import date as dt_date


def run(inputs: dict) -> dict:
    technician = inputs.get("technician", "").strip()
    order_number = inputs.get("order_number", "").strip()
    work_description = inputs.get("work_description", "").strip()
    hours = inputs.get("hours", 0)
    record_date = inputs.get("date") or dt_date.today().strftime("%d.%m.%Y")

    if not technician or not order_number or not work_description:
        return {"draft": "FEHLER: Techniker, Auftragsnummer und Arbeitsbeschreibung sind Pflichtfelder."}

    draft = f"""ENTWURF — Leistungsnachweis
Datum: {record_date}

Auftragsnummer: {order_number}
Techniker: {technician}
Geleistete Stunden: {hours} Std.

Durchgeführte Arbeiten:
{work_description}

Bestätigung:
Arbeiten wurden fachgerecht und gemäß Sicherheitsvorschriften durchgeführt.

Status: ENTWURF — Vor Einreichung prüfen und unterzeichnen lassen.
Automatisch erstellt — kein Normtext enthalten."""

    return {"draft": draft}


if __name__ == "__main__":
    result = run({"technician": "J. Schmidt", "order_number": "10098765", "work_description": "Prüfung ortsfester elektrischer Anlagen nach DGUV V3", "hours": 4})
    print(result["draft"])
