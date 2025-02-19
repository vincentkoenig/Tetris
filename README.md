# Tetris in Python mit Pygame

Ein klassisches Tetris-Spiel, entwickelt mit **Python** und **Pygame**.
Das Spiel enthält ein **Highscore-System**, das automatisch den besten Punktestand speichert.

---

## 🚀 Installation

### 1️⃣ Python installieren
Falls du Python noch nicht installiert hast, lade es herunter und installiere es von der offiziellen Website:
👉 [Python Download](https://www.python.org/downloads/)

### 2️⃣ Pygame installieren
Pygame ist erforderlich, um das Spiel auszuführen. Installiere es mit folgendem Befehl:
```bash
pip install pygame
```

### 3️⃣ Code herunterladen
Lade den Code als ZIP-Datei herunter oder klone das Repository:
```bash
git clone https://github.com/dein-github/tetris-python.git
```

---

## 🎮 Spiel starten

Navigiere im Terminal oder in der Eingabeaufforderung in den Ordner des Spiels und starte das Skript:
```bash
python tetris.py
```

---

## 🕹️ Steuerung
| Taste       | Aktion                 |
|------------|------------------------|
| ⬅️ Links   | Tetromino nach links   |
| ➡️ Rechts  | Tetromino nach rechts  |
| ⬇️ Unten   | Tetromino schneller fallen lassen |
| Space      | Tetromino drehen       |
| ❌ ESC     | Spiel beenden          |

---

## 🎯 Features
✅ Verschiedene Tetromino-Formen <br>
✅ Kollisionserkennung <br>
✅ Rotationsmechanismus <br>
✅ Automatisches Speichern des Highscores <br>
✅ Dynamisches Spielfeld mit 10x20 Blöcken <br>
✅ Zeilenlöschung, wenn eine Reihe voll ist <br>

---

## 🛠️ Code-Übersicht

### Hauptkomponenten:
- **`tetris.py`** → Das Hauptskript mit der Spiel-Logik
- **`highscore.txt`** → Speichert den höchsten Punktestand

### Wichtige Funktionen:
- `get_random_tetromino()`: Erstellt ein zufälliges Tetromino
- `rotate()`: Dreht das aktuelle Tetromino
- `is_valid_move()`: Prüft, ob eine Bewegung möglich ist
- `clear_full_rows()`: Entfernt volle Reihen und erhöht den Score

---

## 📌 Highscore-System

- Der **aktuelle Score** erhöht sich um **100 Punkte** für jede gelöschte Reihe.
- Der **Highscore** wird gespeichert und bleibt auch nach einem Neustart bestehen.
- Die Highscore-Datei `highscore.txt` wird automatisch erstellt und aktualisiert.

---

## ❓ Fehlerbehebung
Falls du auf Probleme stößt:
- Prüfe, ob Python und Pygame korrekt installiert sind.
- Starte das Spiel aus dem richtigen Verzeichnis.
- Falls das Problem weiter besteht, erstelle ein **Issue** in deinem GitHub-Repository.

---

## 📜 Lizenz
Dieses Projekt steht unter der **MIT-Lizenz**.
Fühle dich frei, es zu verwenden, zu modifizieren und weiterzuentwickeln! 😊

---

Viel Spaß mit deinem eigenen Tetris-Spiel! 🎮

 
