import urllib.request
import os
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

urls = {
    1: "https://baitaptracnghiem.com/lam-bai/de-thi-bai-tap-trac-nghiem-lap-trinh-java-online-de-1",
    2: "https://baitaptracnghiem.com/lam-bai/de-thi-bai-tap-trac-nghiem-lap-trinh-java-online-de-2",
    3: "https://baitaptracnghiem.com/lam-bai/de-thi-bai-tap-trac-nghiem-lap-trinh-java-online-de-3",
    4: "https://baitaptracnghiem.com/lam-bai/de-thi-bai-tap-trac-nghiem-lap-trinh-java-online-de-4"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

os.makedirs("c:/Users/DELL/Downloads/ontap_html/scratch", exist_ok=True)

for num, url in urls.items():
    print(f"Downloading Đề {num} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8')
            output_path = f"c:/Users/DELL/Downloads/ontap_html/scratch/de{num}.html"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  Successfully saved to {output_path} ({len(html)} chars)")
        time.sleep(2) # rate limit friendly
    except Exception as e:
        print(f"  Error downloading Đề {num}: {e}")
