# MCP Paint & Keynote Integration

An intelligent agent system that combines mathematical calculations with automated presentation creation using Model Context Protocol (MCP) and Google's Gemini AI. The system can perform complex mathematical operations and automatically create Keynote presentations with the results.

## 🚀 Features

### Mathematical Operations
- **Basic Arithmetic**: Addition, subtraction, multiplication, division
- **Advanced Math**: Power, square root, cube root, factorial
- **Trigonometric Functions**: Sine, cosine, tangent
- **Logarithmic Functions**: Natural logarithm
- **Specialized Tools**: String to ASCII conversion, exponential sums, Fibonacci sequences

### Presentation Automation
- **Keynote Integration**: Create, open, and manipulate Keynote presentations via AppleScript
- **Shape Management**: Add rectangles and text shapes to presentations
- **PowerPoint Support**: Create and modify PowerPoint presentations using python-pptx

### AI-Powered Agent
- **Iterative Problem Solving**: Uses Google Gemini AI to break down complex problems
- **Tool Orchestration**: Automatically selects and chains mathematical operations
- **Result Visualization**: Creates presentations to display calculation results

## 📋 Prerequisites

- **Python 3.13+**
- **macOS** (for Keynote integration)
- **Keynote** application installed
- **Google Gemini API Key**

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd agents2-s4-paint-mcp
   ```

2. **Install dependencies**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## 🎯 Usage

### Running the AI Agent

The main agent script (`talk2mcp.py`) demonstrates the complete workflow:

```bash
python3 talk2mcp.py
```

This will:
1. Connect to the MCP server
2. Use Gemini AI to solve the problem: "Find ASCII values of 'INDIA', calculate exponential sums, create a Keynote presentation, add a rectangle, and display the result"
3. Execute the solution step by step

### Available Tools

The MCP server provides these mathematical tools:

```python
# Basic operations
add(a: int, b: int) -> int
subtract(a: int, b: int) -> int
multiply(a: int, b: int) -> int
divide(a: int, b: int) -> float

# Advanced operations
power(a: int, b: int) -> int
sqrt(a: int) -> float
cbrt(a: int) -> float
factorial(a: int) -> int
log(a: int) -> float

# Trigonometric functions
sin(a: int) -> float
cos(a: int) -> float
tan(a: int) -> float

# Specialized functions
strings_to_chars_to_int(string: str) -> list[int]
int_list_to_exponential_sum(int_list: list) -> float
fibonacci_numbers(n: int) -> list
```

### Presentation Tools

```python
# Keynote operations (macOS only)
create_and_open_keynote_presentation() -> None
add_rectangle_in_keynote_presentation() -> None
add_text_in_keynote_presentation(text: str) -> None

# PowerPoint operations
create_presentation() -> str
add_rectangle_in_presentation(pr_name: str) -> None
add_text_in_presentation(pr_name: str, text: str) -> None
```

## 🔧 Development

### Running the MCP Server

For development and testing:

```bash
# Development mode (with transport)
python3 mcpserver.py dev

# Production mode (stdio transport)
python3 mcpserver.py
```

### Project Structure

```
agents2-s4-paint-mcp/
├── mcpserver.py          # MCP server with all mathematical and presentation tools
├── talk2mcp.py          # Main AI agent that orchestrates the workflow
├── example2.py          # Additional examples and demonstrations
├── test.py              # Test scripts
├── test.ipynb           # Jupyter notebook for interactive testing
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project configuration
└── README.md           # This file
```

### Key Components

1. **MCP Server** (`mcpserver.py`): Implements all mathematical and presentation tools using FastMCP
2. **AI Agent** (`talk2mcp.py`): Orchestrates the workflow using Gemini AI and MCP client
3. **Error Handling**: Robust error handling for AppleScript execution and subprocess calls

## 🐛 Troubleshooting

### Common Issues

1. **JSON Parsing Errors**: Fixed by proper string escaping in AppleScript functions
2. **Keynote Not Opening**: Ensure Keynote is installed and accessible
3. **API Key Issues**: Verify your Gemini API key is correctly set in `.env`

### Debug Mode

Enable debug output by setting environment variables:
```bash
export DEBUG=1
python3 talk2mcp.py
```

## 📝 Example Workflows

### Mathematical Problem Solving
```python
# The agent can solve complex problems like:
# 1. Convert "INDIA" to ASCII values: [73, 78, 68, 73, 65]
# 2. Calculate exponential sums: e^73 + e^78 + e^68 + e^73 + e^65
# 3. Create a presentation with the result
```

### Presentation Automation
```python
# Automatically create and populate presentations
create_and_open_keynote_presentation()
add_rectangle_in_keynote_presentation()
add_text_in_keynote_presentation("Your calculated result here")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini AI for intelligent problem solving
- Model Context Protocol (MCP) for tool integration
- FastMCP for simplified MCP server implementation
- AppleScript for Keynote automation
- python-pptx for PowerPoint manipulation

---

**Note**: This project requires macOS for Keynote integration. PowerPoint functionality works cross-platform.
