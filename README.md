# Kaihou NLP Engine – spaCy‑based Analyzer

Kaihou NLP Engine is a tiny Python library that analyses the morphosyntax of a sentence with spaCy and prints a friendly description, ready to be integrated into larger translation projects such as Kaihou Engine.

## Core Features
- Universal POS tags and dependency relations (spaCy).
- Human‑readable translations of technical tags.
- Rich‑styled pretty‑printed tree (dark theme).
- Simple CLI (`nlp_engine.cli`) with interactive menu.
- Easy to extend with additional languages.

## Installation
```bash
git clone https://github.com/houtarou-d/kaihou-nlp-engine.git
cd kaihou-nlp-engine
pip install -r requirements.txt
python -m spacy download es_core_news_sm   # or another model
```

## Usage
```bash
# Analyse a sentence (default language)
python -m nlp_engine.cli analyze "The children are playing in the park"

# List supported language codes
python -m nlp_engine.cli list‑langs
```

## Adding a New Language
1. Open `nlp_engine/analyzer.py`.
2. Extend the `model_map` dictionary inside `SpaCyAnalyzer.__init__`, e.g.:
   ```python
   model_map = {"es": "es_core_news_sm", "en": "en_core_news_sm", "it": "it_core_news_sm"}
   ```
3. Run `python -m spacy download <model_name>` to install the model.
4. The CLI will automatically accept the new `--lang` code.

## Relation to Kaihou Engine
It serves as the linguistic analysis base that Kaihou Engine imports to provide precise, context‑aware translations.

## Thank You to

    The spaCy library that provides the NLP backbone
    The Rich library for beautiful terminal output
    The Click library for the CLI framework
    The Python community for its extensive ecosystem
    And of course every contributor who has helped improve Kaihou NLP Engine!

## License
MIT – feel free to adapt and share!
