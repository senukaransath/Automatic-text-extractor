# 🔍 Selenium Google Search & Data Extraction

Automate Google search using **Python & Selenium**, handle CAPTCHA manually, and extract text from the first search result website.

## ✨ Features

✅ Open Google  
✅ Search for a given keyword  
✅ Handle CAPTCHA manually  
✅ Click the first search result  
✅ Extract a specific text from the opened page  
✅ Print the extracted text in the command line  

🚀 Perfect for web scraping, automation, and research tasks!

---

## 👥 Installation

### 🔹 1️⃣ Install Dependencies
Make sure you have Python installed. Then install Selenium:

```bash
pip install selenium
```

### 🔹 2️⃣ Download WebDriver
Selenium requires a **WebDriver** to control your browser.  
- **[ChromeDriver](https://chromedriver.chromium.org/downloads)**  
- **[GeckoDriver for Firefox](https://github.com/mozilla/geckodriver/releases)**  

Place the WebDriver in the **same folder** as your script or add it to the system `PATH`.

---

## 🚀 Usage

Run the script with:

```bash
python text_extractor.py
```

🔹 **Customize Your Search Query**  
Edit `search_query` inside the script:

```python
search_query = "Innobot Health"  # Change this to any topic
```

🔹 **Extracting Specific Elements**  
Modify the part where text is extracted:

```python
special_text = driver.find_element(By.TAG_NAME, "p").text
```

Replace `"p"` with:
- `"h1"` for main titles
- `"h2"` for subheadings
- `"meta"` for metadata extraction

---

## ❌ Handling "I Am Not a Robot" CAPTCHA

### 🚩 Problem:
Google may detect automation and show a **reCAPTCHA** ("I am not a robot").

### ✅ Solution:
1. **Manual CAPTCHA Handling**  
   The script pauses execution and asks you to solve the CAPTCHA manually:
   ```python
   input("Solve the CAPTCHA and press Enter to continue...")
   ```

2. **Use an Alternative Search Engine**  
   Switch to **DuckDuckGo** (no CAPTCHA issues!):
   ```python
   driver.get("https://duckduckgo.com/")
   ```

3. **Mimic Human Behavior**  
   Add random delays to avoid bot detection:
   ```python
   import time, random
   time.sleep(random.uniform(2, 5))  # Wait 2 to 5 seconds randomly
   ```

---

## 📈 Troubleshooting

### ❓ **Issue: `selenium.common.exceptions.NoSuchElementException`**
- **Cause:** Element not found on the page.
- **Fix:** Increase the **wait time**:
  ```python
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))
  ```

### ❓ **Issue: `StaleElementReferenceException`**
- **Cause:** The page reloaded, and the element changed.
- **Fix:** Re-locate the element before using it:
  ```python
  element = driver.find_element(By.TAG_NAME, "p")  # Find it again
  ```

### ❓ **Issue: `Google Blocks Automation`**
- **Cause:** Google detected the script as a bot.
- **Fix:** Use **DuckDuckGo** or **Google Search API** instead.

---

## 📝 License
This project is **open-source** and free to use under the **MIT License**.  

💡 *Contributions are welcome!* Feel free to improve or modify the script. 

---
🚀 **Enjoy Automating!** Happy Coding! 🤖💻

