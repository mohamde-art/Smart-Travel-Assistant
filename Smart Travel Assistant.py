from playwright.sync_api import sync_playwright
import csv

# الدول الخليجية والعواصم
gulf_countries = {
    "Saudi Arabia": "Riyadh",
    "United Arab Emirates": "Abu Dhabi",
    "Kuwait": "Kuwait City",
    "Qatar": "Doha",
    "Bahrain": "Manama",
    "Oman": "Muscat"
}

# بيانات نهائية: [الدولة، العاصمة، درجة الحرارة، تكلفة العائلة، تكلفة الفرد]
combined_data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    for country, capital in gulf_countries.items():
        temp = "N/A"
        family_cost = "N/A"
        personal_cost = "N/A"

        # ✅ استخراج بيانات الطقس من AccuWeather
        try:
            page.goto("https://www.accuweather.com/")
            page.wait_for_timeout(3000)

            try:
                page.click("button:has-text('Agree')")
                page.wait_for_timeout(1000)
            except:
                pass

            page.wait_for_selector("input[placeholder='Search your Address, City or Zip Code']", timeout=10000)
            page.fill("input[placeholder='Search your Address, City or Zip Code']", country)
            page.keyboard.press("Enter")
            page.wait_for_timeout(4000)

            page.click(".locations-list .location-name")
            page.wait_for_timeout(4000)

            temp = page.locator("div.body").inner_text()
            print(f"✅ [Weather] {country}: {temp}")
        except Exception as e:
            print(f"⚠️ [Weather] لم يتم استخراج الطقس لـ {country} - الخطأ: {e}")

        # ✅ استخراج تكلفة المعيشة من Numbeo
        try:
            page.goto("https://www.numbeo.com/cost-of-living/")
            page.wait_for_timeout(3000)

            try:
                page.click("button:has-text('Agree')")
                page.wait_for_timeout(1000)
            except:
                pass

            page.wait_for_selector("input[placeholder='Select City']", timeout=10000)
            page.fill("input[placeholder='Select City']", capital)
            page.keyboard.press("Enter")
            page.wait_for_timeout(3000)

            page.click("a.ui-corner-all")
            page.wait_for_timeout(5000)

            family_cost = page.locator("span.emp_number").nth(0).inner_text()
            personal_cost = page.locator("span.emp_number").nth(1).inner_text()
            print(f"✅ [Cost] {capital}: Family: {family_cost}, Personal: {personal_cost}")
        except Exception as e:
            print(f"⚠️ [Cost] لم يتم استخراج تكلفة المعيشة لـ {capital} - الخطأ: {e}")

        # حفظ البيانات في القائمة الموحدة
        combined_data.append([country, capital, temp, family_cost, personal_cost])

    browser.close()

# ✅ حفظ النتائج في ملف CSV واحد
with open("gulf_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Country", "Capital", "Temperature", "Family_Cost", "Personal_Cost"])
    writer.writerows(combined_data)

print("✅ تم حفظ البيانات في ملف gulf_data.csv")

