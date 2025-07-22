# Offline AI-Powered Spam Email Classifier

This tool uses a locally hosted LLM (e.g., Ollama with LLaMA2 or Mistral) to classify emails as spam or not spam, entirely offline for maximum privacy.

## Features
- Batch processing of .eml and plain text files
- Command-line interface
- Outputs classification label and confidence score
- All inference is local (no internet required)
- Practical use of prompt engineering and email parsing

## Requirements
- Python 3.8+
- [Ollama](https://ollama.com/) running locally with a supported model (e.g., llama2, mistral)
- `requests` Python package

## Setup
1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install and run Ollama with your chosen model:
   ```bash
   ollama run llama2
   # or
   ollama run mistral
   ```

## Usage
```bash
python main.py path/to/email1.eml path/to/email2.txt --model llama2
```
- You can specify multiple files for batch processing.
- Use `--output results.csv` to save results to a file.

## Privacy
- All email content and inference remain on your machine.
- No data is sent to the cloud or any external service.

## Example Output
```
email1.eml: spam (confidence: 0.97)
email2.txt: not spam (confidence: 0.85)
```

## Notes
- The tool uses prompt engineering to instruct the LLM to return a JSON object with label and confidence.
- For best results, ensure your Ollama server is running and the model is downloaded. 