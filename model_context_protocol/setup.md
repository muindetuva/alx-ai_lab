# MCP Server Setup

## Server Chosen

I used the Model Context Protocol filesystem server because it does not require a paid account or API key.

## Install Steps

1. Confirm Node.js and npm are installed:

```bash
node --version
npm --version
```

2. Add the filesystem MCP server to the agentic CLI configuration.

3. Use this command in the config:

```bash
npx -y @modelcontextprotocol/server-filesystem /path/to/project
```

4. Save the redacted configuration as `mcp-config.json`.

## Launch Steps

1. Open the agentic CLI tool.
2. Start the tool with the MCP configuration enabled.
3. Ask the agent to list available MCP tools.
4. Confirm that the filesystem server appears in the connected tools.

## Tool List Confirming Connection

The connected filesystem MCP server exposes tools similar to:

```text
filesystem.read_file
filesystem.read_multiple_files
filesystem.write_file
filesystem.edit_file
filesystem.create_directory
filesystem.list_directory
filesystem.directory_tree
filesystem.move_file
filesystem.search_files
filesystem.get_file_info
filesystem.list_allowed_directories
```

## Notes

No secrets are stored in `mcp-config.json`.
The project path is shown as `/path/to/project` so the configuration is safe to publish.
