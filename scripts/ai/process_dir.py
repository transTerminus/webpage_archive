import os
import argparse
import tempfile
import subprocess
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_file_content(file_path):
    """Read content from a file with various encodings."""
    encodings = ['utf-8', 'gbk', 'gb2312', 'gb18030']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    
    logging.error(f"Failed to read {file_path} with any supported encoding")
    return None

def process_file(file_path, prompt_template, gen_script_path, output_dir):
    """Process a single file using the provided prompt template."""
    # Create output path in dst directory
    rel_path = os.path.relpath(file_path, start=args.src)
    output_path = os.path.join(output_dir, rel_path)
    
    # Skip if output file already exists
    if os.path.exists(output_path):
        logging.info(f"Skipping {file_path} - output file already exists: {output_path}")
        return True
        
    content = read_file_content(file_path)
    if content is None:
        return False

    # Format the prompt template with the file content
    try:
        input_content = prompt_template.format(file=content)
    except KeyError as e:
        logging.error(f"Invalid placeholder in template: {e}")
        return False

    # Create temporary file for input
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as temp_input:
        temp_input.write(input_content)
        temp_input_path = temp_input.name

    try:
        # Run gen.py
        cmd = [
            'python', gen_script_path,
            temp_input_path, output_path
        ]
        
        subprocess.run(cmd, check=True)
        logging.info(f"Successfully processed {file_path} -> {output_path}")
        return True

    except subprocess.CalledProcessError as e:
        logging.error(f"Error processing {file_path}: {e}")
        return False

    finally:
        os.unlink(temp_input_path)

def main():
    parser = argparse.ArgumentParser(description='Process files using a prompt template')
    parser.add_argument('--src', required=True, help='Source directory containing input files')
    parser.add_argument('--dst', required=True, help='Destination directory for output files')
    parser.add_argument('--prompt', required=True, help='Path to prompt template file')
    parser.add_argument('--gen', required=True, help='Path to gen.py script', default='scripts/ai/gen.py')
    parser.add_argument('--pattern', default='*.*', help='File pattern to match (default: *.*)')
    
    global args
    args = parser.parse_args()

    # Read prompt template
    try:
        with open(args.prompt, 'r', encoding='utf-8') as f:
            prompt_template = f.read()
    except Exception as e:
        logging.error(f"Failed to read prompt template: {e}")
        return

    # Create destination directory if it doesn't exist
    os.makedirs(args.dst, exist_ok=True)

    # Process all files in source directory
    src_path = Path(args.src)
    for file_path in src_path.rglob(args.pattern):
        if file_path.is_file():
            process_file(str(file_path), prompt_template, args.gen, args.dst)

if __name__ == "__main__":
    main()