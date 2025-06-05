# MCP Server - Job Assistant

Project Idea: Develop an MCP server that connects to a Gmail account to automatically read and parse emails, identifying recruiter outreach, interview schedules, and follow-ups for streamlined job application management.

Reference Link: https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file

Requirements:
1. UV
2. Claude Desktop

First time - For UV enabled project creation
uv init mcp-server-demo
cd mcp-server-demo
uv add "mcp[cli]"

You can install this server in Claude Desktop and interact with it right away by running:
mcp install server.py


✅ 1. Enable the Gmail API
Go to the Google Cloud Console.
Create a new project (or select an existing one).
Go to APIs & Services > Library and enable the Gmail API.
Go to APIs & Services > Credentials:
Create OAuth 2.0 Client ID credentials.
Download the credentials.json file.
