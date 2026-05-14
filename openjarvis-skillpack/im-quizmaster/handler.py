"""IHK Industriemeister Quiz — BwHa, MIKP, ZIB, NTG. Learning aid only."""
import random

QUESTIONS = {
    "bwha": [
        {"q": "Was versteht man unter dem Deckungsbeitrag?", "a": "Erlös minus variable Kosten. Er zeigt, wie viel zur Deckung der Fixkosten beiträgt."},
        {"q": "Erläutere den Unterschied zwischen Kostenart, Kostenstelle und Kostenträger.", "a": "Kostenart: Was kostet etwas (z.B. Löhne). Kostenstelle: Wo entstehen Kosten (z.B. Abteilung). Kostenträger: Wofür entstehen Kosten (z.B. Produkt, Auftrag)."},
        {"q": "Was ist der Break-even-Point?", "a": "Der Punkt, an dem Erlöse und Gesamtkosten gleich sind. Darunter: Verlust, darüber: Gewinn."},
        {"q": "Nenne drei Merkmale der Vollkostenrechnung.", "a": "1. Alle Kosten werden auf Kostenträger verteilt. 2. Fixkosten werden anteilig zugerechnet. 3. Geeignet für Preisuntergrenze bei Vollauslastung."},
        {"q": "Was bedeutet Amortisationsrechnung?", "a": "Sie ermittelt, wie lange es dauert bis eine Investition durch Rückflüsse gedeckt ist. Formel: Investition / jährlicher Rückfluss."},
    ],
    "mikp": [
        {"q": "Was sind die Kernaufgaben der Mitarbeiterführung?", "a": "Planen, Organisieren, Motivieren, Kontrollieren und Entwickeln von Mitarbeitern."},
        {"q": "Erläutere den Unterschied zwischen transaktionaler und transformationaler Führung.", "a": "Transaktional: Führung durch Belohnung/Bestrafung (Austauschprinzip). Transformational: Führung durch Vision, Inspiration und Vorbildwirkung."},
        {"q": "Was versteht man unter dem Führungsstil nach dem Reifegradmodell?", "a": "Der Führungsstil richtet sich nach dem Reifegrad des Mitarbeiters: niedrig = direktiv, hoch = delegierend."},
        {"q": "Nenne drei Konfliktarten im Betrieb.", "a": "Sachkonflikt, Beziehungskonflikt, Rollenkonflikt (Interessenkonflikt, Wertekonflikt)."},
        {"q": "Was ist ein Betriebsrat und welche Mitbestimmungsrechte hat er?", "a": "Gewähltes Gremium der Arbeitnehmer. Mitbestimmung bei sozialen (z.B. Arbeitszeit), personellen und wirtschaftlichen Angelegenheiten (BetrVG)."},
    ],
    "zib": [
        {"q": "Was versteht man unter dem Regelkreisprinzip in der Steuerungstechnik?", "a": "Ist-Wert wird mit Soll-Wert verglichen. Bei Abweichung greift ein Regler ein, um den Ist-Wert anzupassen."},
        {"q": "Erläutere den Unterschied zwischen Steuerung und Regelung.", "a": "Steuerung: offen, kein Rückführsignal. Regelung: geschlossen, Ist-Wert wird zurückgeführt und verglichen."},
        {"q": "Nenne drei Betriebsmodi einer SPS.", "a": "STOP (kein Programm aktiv), RUN (Programm läuft), ANLAUF (Initialisierungsphase)."},
        {"q": "Was ist ein Feldbussystem? Nenne zwei Beispiele.", "a": "Kommunikationssystem für industrielle Geräte. Beispiele: PROFIBUS, PROFINET, CAN, Modbus."},
        {"q": "Was versteht man unter Schutzart IP65?", "a": "IP65: Staub dicht (6) und geschützt gegen Strahlwasser aus jeder Richtung (5)."},
    ],
    "ntg": [
        {"q": "Berechne den Strom bei P = 2300 W und U = 230 V.", "a": "I = P / U = 2300 / 230 = 10 A"},
        {"q": "Was besagt das Ohm'sche Gesetz?", "a": "U = R × I. Die Spannung ist das Produkt aus Widerstand und Stromstärke."},
        {"q": "Erläutere den Unterschied zwischen Reihen- und Parallelschaltung von Widerständen.", "a": "Reihe: R_ges = R1 + R2 + ... (Strom gleich, Spannungen addieren sich). Parallel: 1/R_ges = 1/R1 + 1/R2 (Spannung gleich, Ströme addieren sich)."},
        {"q": "Was ist die Formel für die elektrische Leistung?", "a": "P = U × I = U² / R = I² × R"},
        {"q": "Was bedeutet Wirkleistung, Blindleistung und Scheinleistung?", "a": "Wirkleistung P (W): nutzbarer Anteil. Blindleistung Q (var): reaktiver Anteil (Spulen/Kondensatoren). Scheinleistung S (VA): S² = P² + Q²."},
    ],
}


def run(inputs: dict) -> dict:
    subject = str(inputs.get("subject", "")).lower().strip()
    mode = str(inputs.get("mode", "question")).lower().strip()
    topic = str(inputs.get("topic", "")).lower().strip()

    if subject not in QUESTIONS:
        available = ", ".join(QUESTIONS.keys())
        return {"output": f"Unbekanntes Fach '{subject}'. Verfügbar: {available}"}

    pool = QUESTIONS[subject]
    if topic:
        pool = [q for q in pool if topic in q["q"].lower() or topic in q["a"].lower()] or pool

    item = random.choice(pool)

    if mode == "explain":
        return {"output": f"Thema ({subject.upper()}):\nFrage: {item['q']}\nAntwort: {item['a']}\n\nHinweis: Lernhilfe ohne Gewähr auf Prüfungsrelevanz."}
    else:
        return {"output": f"Frage ({subject.upper()}):\n{item['q']}\n\n(Tipp: mode='explain' für Antwort)"}


if __name__ == "__main__":
    for subj in ["bwha", "mikp", "zib", "ntg"]:
        print(run({"subject": subj, "mode": "question"}))
        print()
