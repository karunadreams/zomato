# Zomato AI Restaurant Recommendation System

An AI-powered service that suggests restaurants based on user preferences using a real-world Zomato dataset and Large Language Models (LLMs).

## Features
- Personalized recommendations based on location, budget, and cuisine.
- Human-like explanations for each recommendation.
- Multi-interface support (CLI and Web UI).

## Quick Start

### 1. Prerequisites
- Python 3.9+
- Groq API Key (Sign up at [console.groq.com](https://console.groq.com))

### 2. Installation
```bash
# Clone the repository
git clone <repo-url>
cd zomato

# Install the package in editable mode
pip install -e .
```

### 3. Environment Setup
Copy the example environment file and add your API keys:
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### 4. Usage
The system provides a CLI tool named `milestone1`.

```bash
# Check if the system is ready
milestone1 doctor

# Get project info
milestone1 info
```

## Documentation
- [Problem Statement](docs/problem-statement.md)
- [Architecture](docs/architcure.md)
- [Edge Cases](docs/edge-cases.md)
- [Phase 0 Scope](docs/phase0-scope.md)
- [Dataset Contract](docs/dataset-contract.md)
