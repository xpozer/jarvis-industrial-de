"""VDE Norm Lookup — metadata and source references only. No protected norm text."""

VDE_INDEX = {
    "VDE 0100": {
        "title_de": "Errichten von Niederspannungsanlagen",
        "title_en": "Low-voltage electrical installations",
        "publisher": "VDE Verlag",
        "series": "DIN VDE 0100",
        "parts": ["Teil 100", "Teil 410", "Teil 430", "Teil 520", "Teil 540", "Teil 600"],
        "source": "https://www.vde-verlag.de",
        "note_de": "Offizielle Texte über VDE Verlag beziehen.",
        "note_en": "Obtain official texts via VDE Verlag.",
    },
    "VDE 0105": {
        "title_de": "Betrieb von elektrischen Anlagen",
        "title_en": "Operation of electrical installations",
        "publisher": "VDE Verlag",
        "series": "DIN VDE 0105",
        "parts": ["Teil 100"],
        "source": "https://www.vde-verlag.de",
        "note_de": "Offizielle Texte über VDE Verlag beziehen.",
        "note_en": "Obtain official texts via VDE Verlag.",
    },
    "DGUV V3": {
        "title_de": "Elektrische Anlagen und Betriebsmittel",
        "title_en": "Electrical systems and equipment",
        "publisher": "DGUV",
        "series": "DGUV Vorschrift 3",
        "source": "https://www.dguv.de/publikationen",
        "note_de": "Offizielle Texte über DGUV Publikationen beziehen.",
        "note_en": "Obtain official texts via DGUV publications.",
    },
}


def run(inputs: dict) -> dict:
    norm_id = inputs.get("norm_id", "").strip().upper()
    query = inputs.get("query", "").strip().lower()

    for key, data in VDE_INDEX.items():
        if key in norm_id or norm_id in key:
            lines = [
                f"{key} — {data['title_de']}",
                f"Herausgeber: {data['publisher']}",
                f"Quelle: {data['source']}",
                f"Hinweis: {data['note_de']}",
            ]
            if "parts" in data:
                lines.append(f"Teile: {', '.join(data['parts'])}")
            if query:
                lines.append(f"(Suchbegriff '{query}' — bitte in offiziellem Dokument nachschlagen)")
            lines.append("\n⚠ Kein geschützter Normtext. Nur Metadaten.")
            return {"result": "\n".join(lines)}

    return {"result": f"Keine Metadaten für '{norm_id}' gefunden. Bitte direkt beim VDE Verlag oder DGUV nachschlagen."}


if __name__ == "__main__":
    print(run({"norm_id": "VDE 0100"}))
