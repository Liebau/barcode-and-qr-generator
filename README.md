# Code128-Barcode aus Text (CLI)

Kleines CLI-Tool, das beliebigen Text in einen **Code128-Barcode (PNG)** rendert. Benötigt Python 3.

## Installation

```bash
python3 -m pip install -r requirements.txt
```

Erforderliche Pakete: `python-barcode`, `Pillow`.

## Nutzung

```bash
# Einfachster Aufruf (interaktive Eingabe)
python3 generate_barcode.py

# Direkt mit Payload und Zieldatei
python3 generate_barcode.py "0,23468 g" -o barcode.png
```

- Ohne Argumente fragt das Tool nach dem Text.
- `-o/--output` setzt den Dateinamen (Endung `.png` wird automatisch ergänzt).

## Optionen

- `payload` (optional): Text/Zahl, die codiert werden soll (ansonsten Eingabeaufforderung).
- `-o, --output PATH` (optional): Zieldatei, Standard: `barcode.png`.

## Hinweise

- Nutzt **Code128** aus `python-barcode` mit `ImageWriter` (Pillow); erzeugt eine lesbare Beschriftung unter dem Barcode.
- Module-Breite/-Höhe, Schriftgröße, Abstand und Quiet-Zone sind sinnvoll vorkonfiguriert.
- Die PNG-Endung wird bei Bedarf ergänzt.

## Fehlerbehebung

- `ModuleNotFoundError: No module named 'barcode'` → Abhängigkeiten installieren:
  ```bash
  python3 -m pip install -r requirements.txt
  ```
- Leere Eingabe bricht mit Meldung ab („Kein Text angegeben – Abbruch.“).

## Lizenz

Verwendung auf eigenes Risiko. (Lizenztext hier ergänzen, falls gewünscht.)
