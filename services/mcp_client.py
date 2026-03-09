import subprocess
import json


def call_mcp_tool(tool_name, arguments):

    process = subprocess.Popen(
        ["node", "london-tfl-journey-status-mcp-server/mcpServer.js"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    request = {"tool": tool_name, "arguments": arguments}

    process.stdin.write(json.dumps(request) + "\n")
    process.stdin.flush()

    response = process.stdout.readline()

    return response
