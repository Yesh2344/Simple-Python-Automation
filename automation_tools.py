#!/usr/bin/env python3
"""
Simple Python Automation Tool
"""

import argparse
import os
import shutil
import csv
import json

def list_files(directory):
    """List all files in a directory"""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for file in files:
        print(file)

def copy_files(source, destination):
    """Copy all files from source to destination"""
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        if os.path.isfile(s):
# Added comment
            shutil.copy2(s, d)
            print(f"Copied: {item}")

def csv_to_json(csv_file, json_file):
    """Convert a CSV file to JSON"""
    data = []
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)
    
    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)
    
    print(f"Converted {csv_file} to {json_file}")

def main():
    parser = argparse.ArgumentParser(description="Simple Python Automation Tool")
    parser.add_argument("action", choices=["list", "copy", "convert"], help="Action to perform")
    parser.add_argument("--source", help="Source directory or file")
    parser.add_argument("--destination", help="Destination directory or file")

    args = parser.parse_args()

    if args.action == "list":
        if not args.source:
            print("Please provide a source directory using --source")
            return
        list_files(args.source)
    elif args.action == "copy":
        if not args.source or not args.destination:
            print("Please provide both source and destination directories using --source and --destination")
            return
        copy_files(args.source, args.destination)
    elif args.action == "convert":
        if not args.source or not args.destination:
            print("Please provide both source CSV file and destination JSON file using --source and --destination")
            return
        csv_to_json(args.source, args.destination)

if __name__ == "__main__":
    main()