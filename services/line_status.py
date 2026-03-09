from services.mcp_client import call_mcp_tool


def get_line_status(line):
    return call_mcp_tool("get_line_status", {"line": line})
