
#  Agentic AI-Powered Omnichannel Conversational Sales Agent

An **end-to-end Agentic AI system** that delivers a **unified, intelligent, and personalized retail experience** across **Web, Mobile, and WhatsApp** channels.
The platform uses **LangChain + LLMs + modular worker agents** to orchestrate sales, inventory, payments, and post-purchase support for ABFRL brands.

---

##  Key Features

* **Agentic AI Orchestration**

  * Central AI Sales Agent coordinates specialized Worker Agents.
* **LLM-Powered Conversational Flow**

  * Natural, context-aware conversations using OpenAI + LangChain.
* **Omnichannel Support**

  * REST API (Web/App) + WhatsApp Bot (Twilio).
* **Retail-Specific Intelligence**

  * Product recommendations, inventory checks, payments, order tracking.
* **Conversation Memory**

  * Maintains user context across interactions.
* **End-to-End Demo Ready**

  * Includes a demo script for full user journey simulation.

---

##  Systm Workflow

```
Customer (Web / App / WhatsApp)
           ↓
FastAPI Backend
           ↓
AI Sales Agent (LangChain + LLM + Memory)
           ↓
Worker Agents
 ├─ Recommendation Agent
 ├─ Inventory Agent
 ├─ Payment Agent
 └─ Post-Purchase Support Agent
```

---

##  Project Structure

```
Agentic-AI-Powered-Coversational-Sales-Agent-for-Retail-ABFRL-/
│
├── app/
│   ├── main.py                  # FastAPI entry point
│   ├── orchestrator.py          # Agentic AI orchestrator (LangChain)
│   ├── llm.py                   # LLM configuration
│   ├── memory.py                # Conversation memory
│   ├── data.py                  # Mock ABFRL retail data
│   │
│   ├── agents/
│   │   ├── recommendation.py
│   │   ├── inventory.py
│   │   ├── payment.py
│   │   └── post_purchase.py
│   │
│   └── whatsapp/
│       └── webhook.py           # WhatsApp bot (Twilio)
│
├── demo/
│   └── demo_script.py           # End-to-end demo
│
├── requirements.txt
├── .env
└── README.md
```

---

##  Tech Stack

* **Backend**: Python, FastAPI , PHP
* **Frontend**: HTML, CSS, JS
* **AI / NLP**: OpenAI, LangChain
* **Memory**: LangChain ConversationBufferMemory
* **Messaging**: Twilio WhatsApp API
* **Deployment Ready**: REST APIs, modular services

---

##  Environment Setup

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
```

---

##  Installation

```bash
git clone https://github.com/your-username/abfrl-agentic-ai.git
cd abfrl-agentic-ai
pip install -r requirements.txt
```

---

##  Run the Backend (API)

```bash
uvicorn app.main:app --reload
```

API Endpoint:

```
POST http://127.0.0.1:8000/chat
```

Example Request:

```json
{
  "message": "Recommend a shirt"
}
```

---

##  WhatsApp Bot Setup (Twilio)

1. Enable **Twilio WhatsApp Sandbox**.
2. Set webhook URL:

```
POST /whatsapp → app/whatsapp/webhook.py
```

3. Send messages via WhatsApp to interact with the AI Sales Agent.

---

##  End-to-End Demo

Run the demo script to simulate a full customer journey:

```bash
python demo/demo_script.py
```

Demo Flow:

1. Product recommendation
2. Inventory check
3. Payment confirmation
4. Order tracking

---

##  What Makes This Agentic AI?

* Central **Sales Agent** decides *what to do next*.
* **Worker Agents** execute domain-specific tasks.
* **LLM + Memory** enables contextual reasoning.
* Easily extensible to new agents (Loyalty, Offers, AR Try-On).

---

##  Future Enhancements

* Vector DB + RAG for large product catalogs
* Real ERP / CRM integrations
* Multi-language support
* Analytics dashboard
* Docker + cloud deployment

---

##  Use Case

Designed for **ABFRL retail brands** to:

* Increase conversions & AOV
* Reduce support load
* Deliver seamless omnichannel experiences
* Enable intelligent, AI-driven sales automation

---


