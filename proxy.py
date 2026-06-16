#!/usr/bin/env python3
import os
import sys
import subprocess

# ==================== Proxy for Telegram API only ====================
# Separate proxy for Telegram API
PROXY = 'http://jobayere31-zone-abc-region-bd:Ti5c2g9eBTIG@43.131.1.47:4950'

# Set the environment
my_env = os.environ.copy()
my_env['HTTP_PROXY'] = PROXY
my_env['HTTPS_PROXY'] = PROXY

# But add your APIs to NO_PROXY (they will bypass the proxy)
my_env['NO_PROXY'] = 'yourapi.com,yourapi2.com,yourapi3.com'
# =========================================================================

print("🌐 Proxy Launcher (Telegram API only))")
print("🚀 Starting main.py...")

try:
    result = subprocess.run(
        [sys.executable, "main.py"] + sys.argv[1:],
        env=my_env,
        capture_output=False
    )
    sys.exit(result.returncode)
except KeyboardInterrupt:
    print("\n⏹️ Closed")
    sys.exit(0)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)