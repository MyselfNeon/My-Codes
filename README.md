## *Website Monitor Bot* 🌐

*A fully automated monitoring and interaction bot for XenForo forums built using Pyrogram, curl_cffi, aiohttp, Flask, and asynchronous scraping with BeautifulSoup, backed by MongoDB.*

---

### ✨ *Features*

- **Cloudflare 403 Auto-Bypass :** *Advanced self-healing system that automatically rotates browser fingerprints to bypass Cloudflare blocks, featuring a Circuit Breaker that seamlessly fails over to a multi-key ScraperAPI pool when natively blocked.*
- **XenForo Account Integration:** *Authenticated interactions using your Netscape cookies stored securely in MongoDB.*
- **Advanced Forum Actions:** *Directly react, reply (with an advanced HTML-to-BBCode translation engine), and report forum posts straight from Telegram.*
- **Automated Monthly Reports:** *A background scheduler that scrapes specific forum sections, tracks active/removed threads, and automatically generates rich Graph.org summary reports.*
- **Rich Bot Statistics:** *Monitor uptime, weekly cycle stats, browser identity success rates, and live ScraperAPI credit usage via a dedicated Telegram command with inline toggle buttons.*
- **Persistent Database:** *Uses asynchronous MongoDB to safely store targets, authorized users, system states, and session cookies across reboots.*
- **Smooth Manual Healing:** *Use a command to seamlessly force a browser header rotation without rebooting the bot.*

---

### 🧩 *How It Works*

*The bot continuously:*
*1. Fetches URLs using `curl_cffi` to mimic real browser fingerprints (Safari, Chrome, Edge) and TLS signatures.*
*2. Parses pages with BeautifulSoup to detect user status changes, new/removed threads, and CAPTCHA challenges.*
*3. If blocked by a 403 error, it triggers an **Auto-Heal Protocol** to rotate headers. If blocks persist, it routes traffic through ScraperAPI for a cooldown period.*
*4. Saves all target data, admin IDs, session cookies, and scan snapshots securely in MongoDB.*
*5. Sends intelligent Telegram alerts, auto-deleting older status messages to reduce chat clutter.*
---

### 🚀 *Installation*

**Method 1: Local / Virtual Environment**
```bash
git clone [https://github.com/MyselfNeon/Platinmods](https://github.com/MyselfNeon/Platinmods)
cd Platinmods
pip install --no-cache-dir -r requirements.txt
python main.py
```

**Method 2: Docker Deployment**
```bash
docker build -t webmonitor-bot .
docker run -d --env-file .env webmonitor-bot
```

---

### ⚙️ *Configuration (Environment Variables)*

*Set these in your `.env` file or hosting provider:*

```env
# Telegram Credentials
API_ID=123456
API_HASH="your_api_hash"
BOT_TOKEN="your_bot_token"

# Authorization Config (Comma separated)
OWNER_ID="123456789,987654321"

# Database Config (MongoDB)
DB_URI="mongodb+srv://<user>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority"
DB_NAME="MonitorDB"

# Multi-Key ScraperAPI Fallback (Space separated keys)
SCRAPERAPI_KEY="key1 key2 key3"

# Application Config (Seconds)
MIN_CHECK_INTERVAL=8
MAX_CHECK_INTERVAL=10
PORT=8080
```

---

### 🧪 *Commands*

*The bot is fully managed via Telegram commands.*[span_22](start_span)[span_22](end_span)

**Monitoring & Status:**
- `/start` - *Check Bot Status & Get your Chat ID*[span_23](start_span)[span_23](end_span)
- `/check` - *Force an instant manual scan and view system health*[span_24](start_span)[span_24](end_span)
- `/stats` - *View rich bot statistics, ScraperAPI usage, and toggle bypass modes*[span_25](start_span)[span_25](end_span)
- `/mr` - *Fetch and generate a real-time Monthly Report via Graph.org*[span_26](start_span)[span_26](end_span)
- `/list` - *Show currently configured targets and authorized users*[span_27](start_span)[span_27](end_span)

**XenForo Actions:**
- `/add_cookie` - *Reply to a `.txt` file to securely load Netscape cookies into the database*[span_28](start_span)[span_28](end_span)
- `/react {link} {reaction_id}` - *Send a reaction to a specific forum post*[span_29](start_span)[span_29](end_span)
- `/reply {link} {text}` - *Reply to a forum thread (supports advanced BBCode quotation)*[span_30](start_span)[span_30](end_span)
- `/report {link} {reason}` - *Report a specific forum post*[span_31](start_span)[span_31](end_span)

**Admin & System Control:**
- `/swap` - *Smoothly initiate a Manual Header Swap to bypass blocks*[span_32](start_span)[span_32](end_span)
- `/restart` - *Hard restart the bot server*[span_33](start_span)[span_33](end_span)
- `/setcmd` - *Automatically update the bot's command menu in Telegram*[span_34](start_span)[span_34](end_span)

**Target Management (Admin Only):**
- `/add_user <Name> <URL>` - *Add a new user to track*[span_35](start_span)[span_35](end_span)
- `/del_user <Name>` - *Remove a tracked user*[span_36](start_span)[span_36](end_span)
- `/add_forum <Name> <URL>` - *Add a new forum section to track*[span_37](start_span)[span_37](end_span)
- `/del_forum <Name>` - *Remove a tracked forum*[span_38](start_span)[span_38](end_span)

**Access Control (Admin Only):**
- `/auth <User_ID>` - *Authorize a user to use the bot and receive alerts*[span_39](start_span)[span_39](end_span)
- `/unauth <User_ID>` - *Revoke user access*[span_40](start_span)[span_40](end_span)

---

### 🌐 *Deployment*

### *Render / Railway / Replit*

***1. Add your environment variables (DB_URI, BOT_TOKEN, PORT, etc.)***[span_41](start_span)[span_41](end_span)
***2. Set `KEEP_ALIVE_URL` in `main.py` if using a pinging service***[span_42](start_span)[span_42](end_span)
***3. Deploy the application using the included `Dockerfile`***[span_43](start_span)[span_43](end_span)
***4. The bot will automatically start the Flask health-check server and background tasks to stay awake***[span_44](start_span)[span_44](end_span)[span_45](start_span)[span_45](end_span)

---

## ❤️ *Author*

***Neon [MyselfNeon](https://t.me/myselfneon)***
