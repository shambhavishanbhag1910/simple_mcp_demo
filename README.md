# Agentic AI Infrastructure: Local Runtime Bridge using MCP

A secure, local communication runtime bridge that interfaces a cloud-based Large Language Model (Claude Desktop) with a local machine execution environment using the **Model Context Protocol (MCP)**. 

This project demonstrates how to build an active backend connection using standard I/O (`stdio`) transport channels to safely run local Python operations and system-level diagnostics directly through an AI chat framework.

---

## 🛠️ System Architecture

Rather than allowing an LLM to guess calculations or work in isolation, this architecture sets up a structural host-client relationship. The cloud interface securely invokes a localized Python runtime managed inside an isolated virtual environment.

* **MCP Host:** Claude Desktop App
* **MCP Server:** FastMCP Python Runtime Framework
* **Communication Layer:** Standard Input/Output (`stdio`) Pipes
* **Environment Isolation:** Anaconda Virtual Environment Wrapper

---

## 🚀 Key Technical Implementation Details

* **Cross-Environment Automation:** Engineered a customized execution syntax configuration (`cmd.exe /c conda run`) to map external host applications seamlessly into target virtual environment directories without system PATH conflicts.
* **Deterministic Tool Schemas:** Implemented secure tool decorators (`@mcp.tool`) capable of executing native mathematical computations and running safe numerical handlers (e.g., zero-division guards).
* **Dynamic Resource Manifests:** Exposed runtime container parameters, platform properties, and resource variables to the client interface dynamically via a unified URI infrastructure.

---

## 📦 Project Structure

```text
├── .gitignore              # Prevents environment tracking leaks
├── README.md               # Architecture documentation
└── server.py               # Active MCP Server logic and tool schemas
```

## Activate your specific virtual environment
conda activate mcp

# Install required dependencies
pip install fastmcp