# Simple Data Analyzer

A small Python command-line program that summarizes student marks from a CSV file. It reports the number of students, average, highest and lowest marks, and pass/fail counts. A mark of **40 or higher** is counted as a pass.

## Requirements

- Python 3
- pandas

## Setup

1. Clone the repository and move into its directory:

   ```bash
   git clone https://github.com/albin2122/simple-data-analyzer.git
   cd simple-data-analyzer
   ```

2. (Optional) Create and activate a virtual environment:

   **Windows (PowerShell):**
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependency:

   ```bash
   python -m pip install pandas
   ```

## Usage

Run the analyzer from the repository directory:

```bash
python analyzer.py
```

On systems where Python is invoked as `python3`, use:

```bash
python3 analyzer.py
```

The script reads `students.csv` from the current directory and prints the summary in the terminal.

## Dataset

The included `students.csv` is a synthetic sample with 100 student records. It has two columns:

| Column | Description |
| --- | --- |
| `name` | Student label |
| `mark` | Numeric mark |

To analyze another dataset, replace `students.csv` with a CSV that uses these column names and contains numeric marks. Keep the file in the repository directory when running the script.

## Project files

- `analyzer.py` — loads the CSV and calculates summary statistics.
- `students.csv` — sample student data.
