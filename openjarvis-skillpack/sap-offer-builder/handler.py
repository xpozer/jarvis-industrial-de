"""SAP Offer/Order Text Draft Builder. Generates drafts only — no direct SAP writes."""
from datetime import date


def run(inputs: dict) -> dict:
    work_type = inputs.get("work_type", "Arbeit").strip()
    equipment = inputs.get("equipment", "Anlage").strip()
    location = inputs.get("location", "")
    hours = inputs.get("hours")
    norm_ref = inputs.get("norm_ref", "")

    location_str = f", {location}" if location else ""
    hours_str = f"\nGeschätzter Aufwand: {hours} Std." if hours else ""
    norm_str = f"\nNormgrundlage: {norm_ref} (Metadaten — kein Normtext)" if norm_ref else ""
    today = date.today().strftime("%d.%m.%Y")

    draft = f"""ENTWURF — Auftragstext SAP PM
Datum: {today}

Maßnahme: {work_type}
Anlage/Betriebsmittel: {equipment}{location_str}{hours_str}{norm_str}

Kurzbeschreibung:
{work_type} an {equipment}{location_str} gemäß Wartungsplan und geltenden Vorschriften.
Durchführung durch Elektrofachkraft. Sicherheitsregeln nach DGUV V3 beachten.

Status: ENTWURF — Vor Verwendung in SAP prüfen und anpassen.
Kein geschützter Normtext enthalten."""

    return {"draft": draft}


if __name__ == "__main__":
    result = run({"work_type": "Inspektion", "equipment": "UVA-12", "location": "Halle 3", "hours": 2, "norm_ref": "VDE 0105"})
    print(result["draft"])
