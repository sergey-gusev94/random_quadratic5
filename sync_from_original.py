#!/usr/bin/env python3
"""
Script to sync random_quadratic folder from the original project.
Deletes the local random_quadratic folder and copies from random_quadratic project.
"""

import shutil
from pathlib import Path


def main():
    script_dir = Path(__file__).parent
    
    target_dir = script_dir / "random_quadratic"
    source_dir = script_dir.parent / "random_quadratic" / "random_quadratic"
    
    print(f"Source: {source_dir}")
    print(f"Target: {target_dir}")
    
    # Validate source exists
    if not source_dir.exists():
        print(f"Error: Source directory not found: {source_dir}")
        return 1
    
    # Delete target if it exists
    if target_dir.exists():
        print(f"\nDeleting: {target_dir}")
        shutil.rmtree(target_dir)
        print("Deleted.")
    
    # Copy source to target
    print(f"\nCopying from source...")
    shutil.copytree(source_dir, target_dir)
    print("Done.")
    
    return 0


if __name__ == "__main__":
    exit(main())
