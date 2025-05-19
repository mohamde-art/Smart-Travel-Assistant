# Smart-Travel-Assistant
# 🌍 Gulf Data Scraper

This project is an automated web scraper that collects **weather data** and **cost of living information** for the Gulf countries using [Playwright](https://playwright.dev/python/). It gathers temperature, family expenses, and personal expenses for each capital and stores them in a single CSV file.

## 📊 Description

The script performs two main tasks:

1. **Weather Data**: Scrapes current temperature for each Gulf country from **[AccuWeather](https://www.accuweather.com/)**.
2. **Cost of Living**: Scrapes family and individual cost of living for each Gulf capital from **[Numbeo](https://www.numbeo.com/cost-of-living/)**.

The results are combined and saved in a single CSV file: `gulf_data.csv`.

## 🌐 Targeted Countries

- Saudi Arabia 🇸🇦 – Riyadh  
- United Arab Emirates 🇦🇪 – Abu Dhabi  
- Kuwait 🇰🇼 – Kuwait City  
- Qatar 🇶🇦 – Doha  
- Bahrain 🇧🇭 – Manama  
- Oman 🇴🇲 – Muscat  

## 💾 Output Format

The output CSV file `gulf_data.csv` will have the following structure:

| Country | Capital | Temperature | Family_Cost | Personal_Cost |
|---------|---------|-------------|-------------|----------------|
| Saudi Arabia | Riyadh | 42°C Sunny | 8500 SAR | 3000 SAR |
| ... | ... | ... | ... | ... |

## 📦 Requirements

- Python 3.7+
- Playwright (Python)

## ⚙️ Installation & Usage

1. Install required packages:

```bash
pip install playwright
playwright install

Features
Automated web scraping using Playwright.

Combines weather and cost of living data.

Handles cookie consent popups automatically.

Error-handling for missing or unavailable data.

📁 Output
gulf_data.csv: Combined data file including weather and cost of living for each Gulf country.

🔐 Notes
A stable internet connection is required.

Browser will open in non-headless mode by default (can be changed).

Some websites might update their structure, requiring selector adjustments.
