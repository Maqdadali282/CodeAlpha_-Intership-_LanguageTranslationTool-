# CodeAlpha Task 1 — Language Translation Tool

Tkinter GUI. Uses `deep-translator` (Google Translate backend, **no API key needed**).
Optional TTS via `gTTS`.

## Run
```bash
pip install -r requirements.txt
python translator.py
```

## Use
1. Pick source language (or leave "Auto Detect") and target language.
2. Type/paste text into the top box.
3. Click **Translate** → result appears in the bottom box.
4. **Copy Output** copies result to clipboard; **Speak Output** plays it as audio (needs internet, uses temp mp3 + system default player).

## Notes / troubleshooting
- If `deep-translator` throws a connection error, check internet access — it calls Google's translate endpoint under the hood, no key required but it does need network.
- To add more languages, extend the `LANGUAGES` dict at the top of `translator.py` with the ISO code Google Translate uses (e.g. `"vi": "Vietnamese"`).
- For a web version instead of desktop GUI, wrap the same `GoogleTranslator(...).translate()` call in a Flask/Streamlit app — logic is identical.

## For submission
- Rename repo to `CodeAlpha_LanguageTranslationTool` when pushing to GitHub.
- Record a short screen-capture demo (enter text → translate → show output) for the LinkedIn video requirement.
