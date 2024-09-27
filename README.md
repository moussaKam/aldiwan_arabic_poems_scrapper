# Poetry Scraper & Extractor

This project consists of two scripts that download and extract Arabic poetry data from the [Aldiwan](https://www.aldiwan.net) website:

1. **`main.py`**: Downloads poems in HTML format.
2. **`extract_data_from_html.py`**: Extracts and processes poem text, poet names, and tags into a structured format.

## Installation
1. Clone the repository.
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Download poems**:  
   Run `main.py` to download poems from `poem_0.html` to `poem_124999.html`:

    ```bash
    python main.py
    ```

2. **Extract data**:  
   Run `extract_data_from_html.py` to parse and export poems as `poems.jsonl`:

    ```bash
    python extract_data_from_html.py
    ```

## Output
- **`poems_html/`**: Contains the downloaded HTML files.
- **`poems.jsonl`**: JSON file with poet names, poem texts, and tags.

## Requirements
- `pandas`
- `beautifulsoup4`