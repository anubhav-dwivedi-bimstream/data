import sys
sys.stdout.reconfigure(encoding='utf-8')

from google_play_scraper import app
import json

# Fetch app data
result = app("com.theastrotime")

# --------- PRINT CLEAN & FORMATTED DATA ----------
print("\n📱 APP INFO\n")
print("Name:", result.get("title", "N/A"))
print("Developer:", result.get("developer", "N/A"))
print("Rating:", result.get("score", "N/A"))
print("Installs:", result.get("installs", "N/A"))
print("Updated:", result.get("updated", "N/A"))

# Shortened description
desc = result.get("description", "")
print("\nDescription (shortened):\n", desc[:300], "...\n")

# Screenshots
print("Screenshots:")
for s in result.get("screenshots", [])[:5]:   # Only first 5
    print("-", s)

# --------- SAVE FULL RESULT TO FILE ----------
with open("astrotime_app_data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print("\nFull JSON saved to: astrotime_app_data.json")
