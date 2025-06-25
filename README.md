
# Eventzilla‑Lite (Serverless Event Ticketing Demo)

_A compact, end‑to‑end AWS SAM project you can deploy in under 10 minutes._

## 🛠 Architecture
| Layer | AWS Service(s) | Notes |
|-------|----------------|-------|
| API   | **API Gateway** (REST) | Routes: `/events` (GET/POST), `/book` (POST) |
| Compute | **AWS Lambda** (Python 3.12) | Stateless functions in **src/handlers** |
| Data  | **DynamoDB** | Two tables: `Events` & `Bookings` |
| IaC   | **AWS SAM** | Template: `template.yaml` |
| Front‑end | Static HTML (optional) | `frontend/index.html` fetches the API |

## 🚀 Quick Start

### Prerequisites
* AWS Account with default credentials configured (`aws configure`)
* **AWS SAM CLI** ≥ 1.120  
  ```bash
  brew install aws/tap/aws-sam-cli   # macOS (example)
  ```

### 1 — Build & Deploy
```bash
sam build
sam deploy --guided
# Accept defaults or customise stack + region
```
Deployment creates:
* REST API URL (output `ApiUrl`)
* Lambda functions
* DynamoDB tables

### 2 — Seed an Event
```bash
API_URL=$(aws cloudformation describe-stacks   --stack-name eventzilla-lite   --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue"   --output text)

curl -X POST "$API_URL/events" \
  -H "Content-Type: application/json" \
  -d '{"name":"AWS Workshop","date":"2025-06-25"}'
```

### 3 — List Events
```bash
curl "$API_URL/events"
```

### 4 — (Option) Front‑end
Edit **frontend/index.html** and replace `YOUR_API_URL` with the value of `ApiUrl`, then open the file in your browser.

---

## 📂 Project Structure
```
eventzilla-lite/
├── README.md
├── template.yaml
├── src/
│   └── handlers/
│       ├── create_event.py
│       ├── get_events.py
│       └── book_ticket.py
└── frontend/
    └── index.html
```

Enjoy exploring serverless on AWS 🚀
