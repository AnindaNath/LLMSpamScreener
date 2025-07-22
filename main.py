import argparse
import os
import sys

from email_parser import parse_email_file
from llm_classifier import classify_email

# Placeholder for email parsing and LLM integration

def main():
    parser = argparse.ArgumentParser(description="Offline AI-powered Spam Email Classifier")
    parser.add_argument('inputs', nargs='+', help='Paths to .eml files or plain text files to classify')
    parser.add_argument('--model', default='llama2', help='LLM model to use with Ollama (default: llama2)')
    parser.add_argument('--output', default=None, help='Output file to save results (default: print to stdout)')
    args = parser.parse_args()

    # Placeholder: batch process files
    results = []
    for path in args.inputs:
        if not os.path.isfile(path):
            print(f"File not found: {path}", file=sys.stderr)
            continue
        subject, body = parse_email_file(path)
        label, confidence = classify_email(subject, body, model=args.model)
        results.append({
            'file': path,
            'label': label,
            'confidence': confidence
        })

    # Output results
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            for r in results:
                f.write(f"{r['file']}, {r['label']}, {r['confidence']:.2f}\n")
    else:
        for r in results:
            print(f"{r['file']}: {r['label']} (confidence: {r['confidence']:.2f})")

if __name__ == '__main__':
    main() 