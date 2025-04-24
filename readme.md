# Pingpoint

**Pingpoint** is a fast, developer-friendly CLI tool for diagnosing the health of any HTTP endpoint.
Run one command to check DNS resolution, SSL/TLS status, and HTTP response behavior for websites, APIs, and services.

> Like `ping`, `curl`, and `openssl s_client` had a baby.

---

## 🚀 Features

- 🔍 **DNS Check** – Resolve domain names to IP addresses  
- 🔒 **SSL/TLS Check** – Verify secure connection and TLS version  
- 🌐 **HTTP Behavior Check** – Send requests with different configurations  
- ✅ Supports both raw domains and full URLs  
- 🧪 CLI-first, scriptable, and built for speed

---

## 📦 Installation

```bash
pip install pingpoint
```

## ⚡ Usage

```bash
pingpoint check-dns example.com
pingpoint check-ssl https://example.com
pingpoint check-http https://example.com
pingpoint run-all https://example.com
```

## 📋 Example Output

```
DNS Check:
Resolved to IP: 93.184.216.34

SSL Check:
SSL Version: TLSv1.3

HTTP Checks:
Default: Status: 200, Content: <!doctype html>...
No SSL Verify: Status: 200, Content: <!doctype html>...
Custom User-Agent: Status: 200, Content: <!doctype html>...
Increased Timeout: Status: 200, Content: <!doctype html>...
All Options: Status: 200, Content: <!doctype html>...
```

## 🧰 Built With

- Python 3.6+
- Click
- Requests
- Socket / SSL

## 🪪 License

MIT

## 🙋‍♂️ Author

Created by Zack Adams