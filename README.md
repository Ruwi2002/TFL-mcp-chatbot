# TfL MCP Chatbot 🚇

A command-line AI travel assistant that retrieves real-time London Underground information using the Transport for London (TfL) API through a Model Context Protocol (MCP) wrapper.

This project demonstrates how a conversational system can interact with real-world APIs using an agentic architecture, where a chatbot communicates with an MCP server that exposes transport data as callable tools.

---

## Features

The chatbot currently supports:

- Checking London Underground line status
- Retrieving next train arrival times
- Detecting tube lines and stations from natural language
- Using an MCP server wrapper to access TfL data
- Modular Python backend architecture

Example queries:

central line status  
is the jubilee line delayed  
next train at oxford circus  
next train at waterloo  

---

## System Architecture

The system follows an agentic architecture:

```
User
 ↓
CLI Chatbot (Python)
 ↓
Intent Detection (utils)
 ↓
Service Layer (services)
 ↓
MCP Client
 ↓
MCP Server (Node.js)
 ↓
Transport for London API
 ↓
Live Transport Data
```

This architecture demonstrates how AI systems can interact with APIs through MCP-based tools instead of direct REST calls.

---

## Project Structure

```
tfl-mcp-chatbot/
│
├── chatbot.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── config/
│   └── stations.py
│
├── services/
│   ├── arrivals.py
│   ├── line_status.py
│   └── mcp_client.py
│
├── utils/
│   └── detect.py
│
├── tests/
│   └── api_test.py
│
├── docs/
│   ├── Screenshots/
│   └── Report.docx
│
└── london-tfl-journey-status-mcp-server/
```

---

## Technologies Used

- Python
- Node.js
- Model Context Protocol (MCP)
- Transport for London API
- Git
- GitHub

---

## Installation

Clone the repository:

```
git clone https://github.com/Ruwi2002/tfl-mcp-chatbot.git
```

Navigate to the project folder:

```
cd tfl-mcp-chatbot
```

Install Python dependencies:

```
pip install -r requirements.txt
```

---

## Running the MCP Server

Navigate to the MCP server folder:

```
cd london-tfl-journey-status-mcp-server
```

Install dependencies:

```
npm install
```

Start the MCP server:

```
npm start
```

---

## Running the Chatbot

Return to the project root and run:

```
python chatbot.py
```

Example session:

```
You: central line status
Bot: The Central line currently has Good Service.

You: next train at oxford circus
Bot: Next Central line train arrives in 2 minutes.
```

Type `exit` to stop the chatbot.

---

## Future Improvements

- Journey planning between stations
- Web-based chatbot interface
- LLM-based natural language understanding
- Multi-line service summaries
- Real-time disruption alerts

---

## Project Purpose

This project was developed as part of a university Final Year Project exploring how conversational AI systems can interact with real-world APIs using the Model Context Protocol (MCP).

The prototype demonstrates how transport data can be accessed through MCP tools and presented to users via a conversational interface.

---

## License

This project is intended for educational and research purposes.