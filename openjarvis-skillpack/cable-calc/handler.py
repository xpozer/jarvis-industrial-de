"""Cable cross-section calculator. Shows all formulas and assumptions. Result must be verified."""
import math


RESISTIVITY = {"cu": 0.0178, "al": 0.0282}  # Ohm·mm²/m at 20°C
MATERIAL_NAME = {"cu": "Kupfer", "al": "Aluminium"}


def run(inputs: dict) -> dict:
    current_a = float(inputs.get("current_a", 0))
    length_m = float(inputs.get("length_m", 0))
    voltage_v = float(inputs.get("voltage_v", 230))
    material = str(inputs.get("material", "cu")).lower().strip()
    voltage_drop_pct = float(inputs.get("voltage_drop_pct", 3))

    if current_a <= 0 or length_m <= 0:
        return {"result": "FEHLER: Strom und Leitungslänge müssen größer 0 sein."}

    if material not in RESISTIVITY:
        return {"result": f"FEHLER: Unbekanntes Material '{material}'. Gültig: cu, al"}

    rho = RESISTIVITY[material]
    delta_u = (voltage_drop_pct / 100) * voltage_v
    cross_section = (2 * rho * length_m * current_a) / delta_u
    cross_section_rounded = next((s for s in [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120] if s >= cross_section), cross_section)

    result = f"""Kabelquerschnittsberechnung
Material: {MATERIAL_NAME.get(material, material)}
Strom: {current_a} A
Länge: {length_m} m (Einfachleitung, Hinleitung × 2 im Faktor)
Spannung: {voltage_v} V
Max. Spannungsfall: {voltage_drop_pct}% = {delta_u:.1f} V

Formel: A = (2 × ρ × L × I) / ΔU
       A = (2 × {rho} × {length_m} × {current_a}) / {delta_u:.1f}
       A = {cross_section:.3f} mm²

Nächster Normquerschnitt: {cross_section_rounded} mm²

Annahmen:
- Einphasige Wechselstromleitung (Hin- und Rückleiter)
- Rho bei 20°C Leitertemperatur
- Kein Häufungsfaktor berücksichtigt
- Kein thermischer Kurzschlussstrom berücksichtigt

⚠ Richtwert — durch Elektrofachkraft prüfen lassen.
   Offizielle Berechnung nach VDE 0100 und IEC 60364."""

    return {"result": result}


if __name__ == "__main__":
    result = run({"current_a": 16, "length_m": 25, "voltage_v": 230, "material": "cu"})
    print(result["result"])
