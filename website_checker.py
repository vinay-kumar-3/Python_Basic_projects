print("🔍 WEBSITE URL CHECKER 🔍 \n")

url = input("🌐 Enter the Website URL: ")

if url.startswith("https://"):
    print("🔐 This website uses HTTPS (secure)")
elif url.startswith("http://"):
    print("💀 This website uses HTTP (not secure)")
else:
    print("❌ This doesn't look like a complete URL")

