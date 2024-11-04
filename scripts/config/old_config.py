import yaml
import json
import re
import argparse
import sys

def parse_results(json_data):
    # Create dictionary to store results
    results = {}
    
    # Parse each entry in the success array
    for entry in json_data["success"]:
        url = entry[0]
        filename = entry[1].split('workspace_news/')[-1]  # Get filename part after workspace_news/
        md5 = entry[2]
        
        # Extract title from filename (everything after _ and before .html)
        title = re.search(r'_(.+?)\.html', filename).group(1)
        
        # Store as dictionary
        results[filename] = {
            "link": url,
            "md5": md5,
            "title": title,
            "snippet": ""  # Empty snippet as not provided in input
        }
    
    return results

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert JSON results to YAML format')
    parser.add_argument('input', help='Input JSON file path')
    parser.add_argument('output', help='Output YAML file path')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Read input JSON
        with open(args.input, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Parse into desired format
        results = parse_results(data)
        
        # Write YAML output
        with open(args.output, 'w', encoding='utf-8') as f:
            yaml.dump(results, f, allow_unicode=True, sort_keys=False)
            
        print(f"Successfully converted {args.input} to {args.output}")
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {args.input}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()