# Grocery Price Tracker

A small CLI tool for comparing prices between Trader Joe's and Roche Bros (or any local grocery store). 

Built as my final project for the [InnoVets Codex Intro to Python](https://www.innovets.org/programs/codex) program.

## How It Works

1. Take a photo of your receipt and drop it in the `receipts/` folder
2. A folder automation triggers the script
3. The app uses Google Gemini to extract items and prices from the receipt image
4. You pick which store the receipt is from and categorize each item
5. Everything gets saved to `input.csv` for tracking and comparison

## Setup

1. Install dependencies:
```
   pip install google-genai python-dotenv pydantic pick
```

2. Create a `.env` file:
```
   KEY=your_gemini_api_key
   FILE_PATH=path/to/receipts/folder
```

3. Run it:
```
   python main.py
```

## Note on the API

Gemini offers 20 free API calls per day, which is plenty for personal receipt tracking. Fair warning though — the script is noticeably slow. Not sure if that's Gemini's response time or my code. Probably both.

## Output

Results are written to `input.csv` with columns: date, store, item name, unit price (in cents), unit, and category.