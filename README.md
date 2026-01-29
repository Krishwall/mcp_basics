# 🚀 MCP Basics - Model Context Protocol Fundamentals

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0+-005571?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Beta-yellow.svg)](STATUS)

**A comprehensive collection of examples demonstrating Model Context Protocol (MCP) implementations**

</div>

---

## 📖 Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Scenarios](#scenarios)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## ℹ️ About

**MCP Basics** is an educational repository showcasing various implementations of the **Model Context Protocol (MCP)**. MCP enables AI models to securely access external tools, services, and data sources through standardized interfaces. This repository contains practical examples ranging from simple calculators to complex feed aggregators.

### What is MCP?

Model Context Protocol (MCP) is a specification that allows AI systems to connect to external tools and data sources in a secure and standardized way. It enables AI models to:
- Access external tools and services
- Retrieve real-time data
- Perform complex operations
- Maintain security and privacy

---

## ✨ Features

- 🔧 **Multiple MCP Implementations**: Various approaches to MCP integration
- 🧮 **Calculator Tools**: Basic arithmetic operations via MCP
- 🌐 **HTTP Transport**: Network-based MCP communication
- 📰 **RSS Feed Integration**: Real-world data fetching capabilities
- 🛠️ **FastAPI Integration**: Modern API framework compatibility
- 📦 **Simple Setup**: Easy installation and configuration

---

## 🛠️ Installation

### Prerequisites

- Python 3.13 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mcp-basics.git
   cd mcp-basics
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # Or if using uv
   uv sync
   ```

3. **Verify installation**
   ```bash
   python main.py
   ```

---

## 🚀 Quick Start

Get started with MCP basics in seconds:

### 1. Simple Calculator (STDIO)

```bash
cd scenario-1
python fastmcp_calculator.py
```

This starts a calculator service using STDIO transport for basic arithmetic operations.

### 2. HTTP Calculator

```bash
cd scenario-1
python fastmcp_calculatorV2.py
```

This starts the same calculator but accessible via HTTP on `localhost:8003`.

### 3. FastAPI MCP Calculator

```bash
cd scenario-2
python fastapi_mcp_calculator.py
```

This demonstrates MCP integration with FastAPI, running on `localhost:8002`.

---

## 🎯 Scenarios

This repository contains multiple scenarios demonstrating different MCP use cases:

### Scenario 1: Basic Calculators

#### `fastmcp_calculator.py`
- **Transport**: STDIO (default)
- **Tools**: Add, Subtract, Multiply, Divide
- **Use Case**: Simple arithmetic operations

#### `fastmcp_calculatorV2.py`
- **Transport**: HTTP
- **Host**: localhost:8003
- **Tools**: Same as above but accessible via HTTP

### Scenario 2: FastAPI Integration

#### `fastapi_mcp_calculator.py`
- **Framework**: FastAPI
- **Transport**: HTTP
- **Host**: localhost:8002
- **Features**: Standard FastAPI endpoints converted to MCP tools

### Scenario 3: Advanced Examples

*Coming soon - More complex MCP implementations*

---

## 📡 Deployment

### Feed Fetcher Service

Located in the `deployment/` directory, this service demonstrates real-world MCP usage:

```bash
cd deployment
python feed.py
```

#### Available Tools:

- **`fcc_news_search(query, max_results)`**: Search FreeCodeCamp news articles
- **`fcc_youtube_search(query, max_results)`**: Search FreeCodeCamp YouTube videos  
- **`fcc_secret_message()`**: Return a motivational message

#### Dependencies:
- `feedparser`: For parsing RSS feeds
- `fastmcp`: For MCP implementation

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/mcp-basics.git
cd mcp-basics

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Thanks to the MCP community for developing this innovative protocol
- Inspired by the potential of secure AI-tool integration
- Built with modern Python frameworks and best practices

---

<div align="center">

**Made with ❤️ for the MCP Community**

⭐ Star this repo if you find it helpful!

</div>