import json
import os
import re
import sys

def update_files(payload_json_str):
    try:
        data = json.loads(payload_json_str)
    except Exception as e:
        print(f"Error parsing JSON payload: {e}")
        sys.exit(1)

    # 1. Update P1.json
    with open("P1.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Updated P1.json successfully.")

    # 2. Update default input values directly inside index.html
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Regex replacement for default input values
        html_content = re.sub(r'id="input-md-salary"\s+value="[^"]*"', f'id="input-md-salary" value="{data.get("md_salary", 110000)}"', html_content)
        html_content = re.sub(r'id="input-ops-salary"\s+value="[^"]*"', f'id="input-ops-salary" value="{data.get("ops_salary", 84000)}"', html_content)
        html_content = re.sub(r'id="input-sales-salary"\s+value="[^"]*"', f'id="input-sales-salary" value="{data.get("sales_salary", 75000)}"', html_content)
        html_content = re.sub(r'id="input-wh-salary"\s+value="[^"]*"', f'id="input-wh-salary" value="{data.get("wh_salary", 75000)}"', html_content)
        html_content = re.sub(r'id="input-super-rate"\s+value="[^"]*"', f'id="input-super-rate" value="{data.get("super_rate", 11.5)}"', html_content)

        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        print("Updated index.html default input values successfully.")

if __name__ == "__main__":
    # Expect payload passed as first argument or via environment variable
    payload = os.getenv("CLIENT_PAYLOAD", "{}")
    if len(sys.argv) > 1:
        payload = sys.argv[1]
    update_files(payload)