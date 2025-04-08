# AI-Powered Airbnb Booking Assistant with GROQ Integration

This project provides an interactive web interface for an AI-powered Airbnb booking assistant that helps users find and book apartments. It leverages the GROQ LLM model and Gradio framework to create a user-friendly experience for processing natural language booking requests.

The assistant uses the Model context protocol (MCP) tool to interact with Airbnb's services, processing user queries and returning relevant apartment listings. The application combines modern AI capabilities with practical travel booking functionality, making it easier for users to find accommodations that match their specific requirements.

## Repository Structure
```
.
├── app-groq.py    # Main application entry point containing the Gradio interface and AI agent logic
└── requirements.txt     # Python package dependencies required for the application
```

## Usage Instructions
### Prerequisites
- Python 3.6 or higher
- Node.js and npm (for MCP server)
- The following Python packages:
  - gradio
  - praisonaiagents
  - mcp
  - groq

### Installation
1. Clone the repository:
```bash
git clone https://github.com/nsatya02/mcp.git
cd mcp
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install the MCP server:
```bash
npm install -g @openbnb/mcp-server-airbnb
```

### Quick Start
1. Run the application:
```bash
python app-groq.py
```

2. Open your web browser and navigate to the local URL displayed in the terminal (http://localhost:7860)

3. Enter your booking requirements in the text box (e.g., "I want to book an apartment in boston for 2 nights")

4. View the search results displayed in the markdown output


## Data Flow
The application processes booking requests through a pipeline that converts natural language queries into structured Airbnb searches.

```ascii
A[User Input] --> B[Gradio Interface]
B --> C[GROQ LLM]
C --> D[Airbnb MCP]
D --> E[Formatted Results]
E --> F[User Display]
```
