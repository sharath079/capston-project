#!/bin/bash
# Setup script for Zepto Data & AI Platform

echo "Setting up Zepto Data & AI Platform environment..."

# Step 1: Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 2: Upgrade pip
pip install --upgrade pip

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Confirm installation
echo "Environment setup complete."
echo "Activate with: source venv/bin/activate"
