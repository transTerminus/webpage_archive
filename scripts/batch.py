#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess
from pathlib import Path

def parse_env_args(args):
    """Parse key=value pairs into a dictionary"""
    env_vars = {}
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
            env_vars[key] = value
    return env_vars

def clean_directory(src_dir: str, dst_dir: str, processor_script: str, env_vars: dict = None):
    # Create destination directory if it doesn't exist
    dst_path = Path(dst_dir)
    dst_path.mkdir(parents=True, exist_ok=True)
    
    # Copy page.yml if it doesn't exist in destination
    src_yml = Path(src_dir) / "page.yml"
    dst_yml = dst_path / "page.yml"
    if src_yml.exists() and not dst_yml.exists():
        shutil.copy2(src_yml, dst_yml)
        print(f"Copied page.yml to {dst_path}")
    
    # Prepare environment variables
    env = os.environ.copy()  # Copy current environment
    if env_vars:
        env.update(env_vars)
        print("Using environment variables:", env_vars)
    
    # Process each HTML file
    for src_file in Path(src_dir).glob("*.html"):
        # Call the processor script with environment
        cmd = ["node", processor_script, str(src_file), str(dst_path)]
        try:
            subprocess.run(cmd, env=env, check=True)
            print(f"Processed: {src_file.name}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {src_file.name}: {e}", file=sys.stderr)

def main():
    if len(sys.argv) < 4:
        print("Usage: python batch.py <source_dir> <destination_dir> <processor_script> [KEY1=value1] [KEY2=value2] ...")
        print("Example: python batch.py ./raw_pages ./cleaned_pages ./clean_cheerio.js HTML_CLEANER_CONFIG=./config.json DEBUG=true")
        sys.exit(1)
    
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]
    processor_script = sys.argv[3]
    env_vars = parse_env_args(sys.argv[4:])
    
    if not os.path.isdir(src_dir):
        print(f"Error: Source directory '{src_dir}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    if not os.path.isfile(processor_script):
        print(f"Error: Processor script '{processor_script}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    clean_directory(src_dir, dst_dir, processor_script, env_vars)

if __name__ == "__main__":
    main()
