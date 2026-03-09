import subprocess
import json


def call_mcp_tool(tool_name, arguments):
    """
    Calls a tool from the MCP server using JSON-RPC 2.0 over stdio.
    """

    process = subprocess.Popen(
        ["node", "london-tfl-journey-status-mcp-server/mcpServer.js"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # MCP JSON-RPC request
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": tool_name, "arguments": arguments},
    }

    try:
        # Send request to MCP server
        process.stdin.write(json.dumps(request) + "\n")
        process.stdin.flush()

        # Read response
        response = process.stdout.readline()

        if not response:
            error = process.stderr.read()
            return f"MCP Error: {error}"

        return response.strip()

    except Exception as e:
        return f"MCP Client Error: {str(e)}"
