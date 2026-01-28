#!/bin/bash
set -e

echo "Starting Login System Installation..."

# 1. Check Prerequisites
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is not installed."
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "Error: npm is not installed."
    exit 1
fi

# 2. Create necessary directories
echo "Ensuring directory structure..."
mkdir -p public

# 3. Install Dependencies
echo "Installing Node.js dependencies..."
npm install

echo "------------------------------------------------"
echo "Installation Complete!"
echo "To start the application, run: node server.js"
echo "------------------------------------------------"
