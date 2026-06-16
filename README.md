📋 Complete README.md (One-Click Copy)

```markdown
# 🚀 Proxy Launcher for Telegram Bot (India Region)

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://t.me/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Overview

**Proxy Launcher** is a smart solution for Telegram bots facing connectivity issues in **India** and other regions where Telegram is **partially blocked or throttled** by ISPs.

This script **only routes Telegram API calls** through a proxy while keeping all your other APIs (game servers, databases, etc.) running **directly** without proxy overhead.

---

## 🎯 The Problem

### ❌ Without Proxy Launcher
```bash
python main.py

[ERROR] HTTPSConnectionPool(host='api.telegram.org', port=443): 
Max retries exceeded with url: /botTOKEN/getMe
[ERROR] Bot fails to start
✅ Your custom APIs work (but bot is dead)
```

✅ With Proxy Launcher

```bash
python launcher.py

✅ api.telegram.org → Through proxy → Connected!
✅ Your APIs → Direct connection → Working!
✅ Bot is fully functional
```

---

🔧 How It Works

```mermaid
graph LR
    A[Your Bot] --> B{Proxy Launcher}
    B --> C[Telegram API]
    B --> D[Your APIs]
    C --> E[Proxy Server]
    E --> F[api.telegram.org]
    D --> G[Direct Connection]
    G --> H[Your Servers]
```

Key Features

Feature Description
Selective Proxying Only Telegram API uses proxy
NO_PROXY Support Your APIs bypass proxy automatically
Zero Code Changes No modifications needed in main.py
India Region Ready Bypasses ISP-level blocking
Flexible Configuration Easy to add/remove API domains

---

🚀 Quick Start

Step 1: Create launcher.py

Copy and paste this complete code:

```python
#!/usr/bin/env python3
"""
Proxy Launcher for Telegram Bot (India Region)
Routes ONLY Telegram API through proxy.
"""

import os
import sys
import subprocess

# ==================== Proxy Configuration ====================
# Replace with your actual proxy
PROXY = 'http://username:password@ip:port'

# ==================== Environment Setup ====================
my_env = os.environ.copy()

# Telegram API goes through proxy
my_env['HTTP_PROXY'] = PROXY
my_env['HTTPS_PROXY'] = PROXY

# ==================== CRITICAL: NO_PROXY List ====================
# Add ALL your custom API domains here (they bypass the proxy)
my_env['NO_PROXY'] = (
    'yourapi1.com,'          # Your API 1
    'yourapi2.com,'          # Your API 2
    'yourapi3.com,'          # Your API 3
    'localhost,127.0.0.1'    # Local server
)
# =============================================================

print("=" * 60)
print("🌐 Proxy Launcher (Telegram API only)")
print("📍 Region: India (Telegram is blocked)")
print(f"📡 Proxy: {PROXY.split('@')[1] if '@' in PROXY else PROXY}")
print("=" * 60)
print("🚀 Starting main.py...")
print("-" * 60)

# ==================== Run main.py ====================
try:
    result = subprocess.run(
        [sys.executable, "main.py"] + sys.argv[1:],
        env=my_env,
        capture_output=False
    )
    sys.exit(result.returncode)
except KeyboardInterrupt:
    print("\n⏹️ Bot stopped by user")
    sys.exit(0)
except FileNotFoundError:
    print("❌ ERROR: main.py not found!")
    print("📁 Make sure main.py is in the same folder")
    sys.exit(1)
except Exception as e:
    print(f"❌ ERROR: {e}")
    sys.exit(1)
```

---

Step 2: Update NO_PROXY with Your APIs

Find all API domains in your main.py:

```bash
grep -r "requests.get\|requests.post" main.py
```

Example output:

```python
requests.get("https://like-v351.onrender.com/...")
requests.get("https://info-api-ob54.vercel.app/...")
requests.get("https://access-to-jwt-navy.vercel.app/...")
```

Update NO_PROXY:

```python
my_env['NO_PROXY'] = (
    'like-v351.onrender.com,'
    'info-api-ob54.vercel.app,'
    'access-to-jwt-navy.vercel.app,'
    'api-otrss.garena.com,'
    'ticket.kiosgamer.co.id,'
    'localhost,127.0.0.1'
)
```

---

Step 3: Run Your Bot

```bash
python launcher.py
```

---

📋 Complete Example with Real APIs

```python
#!/usr/bin/env python3
"""
Proxy Launcher for Telegram Bot
Example with real APIs (Free Fire, Like System, etc.)
"""

import os
import sys
import subprocess

# ==================== Proxy Configuration ====================
PROXY = 'http://jobayere31-zone-abc-region-bd:Ti5c2g9eBTIG@43.131.1.47:4950'

# ==================== Environment Setup ====================
my_env = os.environ.copy()
my_env['HTTP_PROXY'] = PROXY
my_env['HTTPS_PROXY'] = PROXY

# ==================== NO_PROXY List ====================
my_env['NO_PROXY'] = (
    'yourapi.com,'
    'yourapi.com,'
    'yourapi.com,'
    'yourapi.com,'
    'yourapi.com,'
    'localhost,127.0.0.1'
)
# =============================================================

print("=" * 60)
print("🌐 Proxy Launcher (Telegram API only)")
print("📍 Region: India (Telegram is blocked)")
print(f"📡 Proxy: {PROXY.split('@')[1] if '@' in PROXY else PROXY}")
print("=" * 60)
print("🚀 Starting main.py...")

try:
    result = subprocess.run(
        [sys.executable, "main.py"] + sys.argv[1:],
        env=my_env,
        capture_output=False
    )
    sys.exit(result.returncode)
except KeyboardInterrupt:
    print("\n⏹️ Bot stopped")
    sys.exit(0)
except FileNotFoundError:
    print("❌ ERROR: main.py not found!")
    sys.exit(1)
except Exception as e:
    print(f"❌ ERROR: {e}")
    sys.exit(1)
```

---

🛠️ Configuration Options

Environment Variables

Variable Purpose
HTTP_PROXY Proxy for HTTP requests
HTTPS_PROXY Proxy for HTTPS requests
NO_PROXY Domains that bypass the proxy

How to Find Your API Domains

Search your main.py for:

```bash
grep -r "requests.get\|requests.post" main.py
```

Common APIs to Add to NO_PROXY

```python
# Game APIs
'api.example.com,'
'game-server.com,'

# Database APIs
'db.example.com,'
'api.mongodb.com,'

# Third-party APIs
'thirdparty-api.com,'

# Local servers
'localhost,127.0.0.1'
```

---

✅ Benefits

Benefit Description
Works in India Bypasses ISP-level Telegram blocking
Faster APIs Your APIs run directly (no proxy overhead)
Zero Code Changes No modifications to main.py
Selective Routing Only Telegram uses proxy
Easy to Debug Clear logs show what's happening
Flexible Easily add/remove domains from NO_PROXY

---

🔍 Troubleshooting

Issue 1: Bot Still Not Working

Check if proxy is active:

```bash
curl -x http://username:pass@ip:port https://api.telegram.org
```

Expected response:

```json
{"ok":true,"result":{"username":"BotFather"}}
```

---

Issue 2: Some APIs Fail

Solution: Add the failing domain to NO_PROXY

```python
my_env['NO_PROXY'] = (
    'failing-api.com,'  # Add this
    'other-apis.com'
)
```

---

Issue 3: Bot Starts but Slow

Solution: Add more domains to NO_PROXY

```python
# The more domains in NO_PROXY, the faster your bot
my_env['NO_PROXY'] = 'api1.com,api2.com,api3.com,api4.com'
```

---

Issue 4: Check What's Using Proxy

Add this to your main.py:

```python
import os
print(f"🚀 Proxy: {os.environ.get('HTTP_PROXY', 'None')}")
print(f"🚫 NO_PROXY: {os.environ.get('NO_PROXY', 'None')}")
```

---

📁 Project Structure

```
your-bot-folder/
├── launcher.py          # Proxy launcher script (this file)
├── main.py              # Your actual bot code (unchanged)
├── requirements.txt     # Your bot dependencies
└── README.md           # This file
```

---

🎯 Quick Commands

Run with Proxy (Recommended)

```bash
python launcher.py
```

Run Without Proxy (For Testing)

```bash
python main.py
```

Check Proxy Status

```bash
curl -x http://username:pass@ip:port https://api.telegram.org
```

Find All API Calls

```bash
grep -r "requests\." main.py
```

---

🌍 Which Countries Need This?

Country Telegram Status Need Proxy?
🇮🇳 India Partially Blocked ✅ Yes
🇨🇳 China Fully Blocked ✅ Yes
🇮🇷 Iran Fully Blocked ✅ Yes
🇷🇺 Russia Throttled ✅ Yes
🇵🇰 Pakistan Intermittent ✅ Yes
🇧🇩 Bangladesh Partially Blocked ✅ Yes
🇺🇸 USA Fully Working ❌ No
🇬🇧 UK Fully Working ❌ No
🇩🇪 Germany Fully Working ❌ No

---

📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

💡 Pro Tips

1. Make it Executable

```bash
chmod +x launcher.py
./launcher.py
```

2. Create an Alias

Add to ~/.bashrc or ~/.bash_profile:

```bash
alias botrun='python /path/to/launcher.py'
```

3. Run in Background

```bash
nohup python launcher.py > bot.log 2>&1 &
```

4. Monitor Logs

```bash
tail -f bot.log
```

---

🤝 Contributing

Found a bug or have a suggestion? Feel free to:

· Open an Issue
· Submit a Pull Request
· Share your experience

---

📧 Support

If you need help:

1. Check the Troubleshooting section
2. Verify your proxy is working
3. Make sure all APIs are in NO_PROXY
4. Contact your proxy provider for issues

---

🎉 Summary

Proxy Launcher is the simplest way to run your Telegram bot in India and other blocked regions:

✅ Just 3 steps:

1. Update NO_PROXY with your APIs
2. Run python launcher.py
3. Your bot works!

✅ No code changes needed
✅ Your APIs stay fast
✅ Only Telegram uses proxy

---

📊 Before & After

Before (Without Launcher) After (With Launcher)
❌ Telegram API blocked ✅ Telegram API works
❌ Bot fails to start ✅ Bot starts successfully
✅ Your APIs work ✅ Your APIs work (faster)
❌ No solution ✅ Simple solution

---

🇮🇳 Now your Telegram bot works perfectly in India! 🚀

https://img.shields.io/github/stars/yourusername/proxy-launcher.svg?style=social
https://img.shields.io/github/forks/yourusername/proxy-launcher.svg?style=social

---

Made with ❤️ for Telegram bot developers in India

```