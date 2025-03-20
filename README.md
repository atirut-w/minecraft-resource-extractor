# Minecraft Resource Extractor

A Python utility to extract all assets from a Minecraft client JAR and the assets index.

## Overview

This tool extracts:
1. Assets directly from the Minecraft client JAR file
2. Assets from the Minecraft assets directory using a specified asset index

It combines both sources into a single organized output directory.

## Requirements

- Python 3.6+
- A copy of Minecraft (Java Edition)

## Usage

```bash
python extractor.py <asset_path> <index> <jar_path> [--output OUTPUT_DIR]
```

### Arguments

- `asset_path`: Path to Minecraft's assets folder (typically `~/.minecraft/assets`)
- `index`: Asset index number to extract (e.g., 19 for Minecraft 1.21.4)
- `jar_path`: Path to the Minecraft JAR file
- `--output`: (Optional) Output directory for extracted assets (default: `./extracted_assets`)

### Example

```bash
python extractor.py ~/.minecraft/assets 19 ~/.minecraft/versions/1.21.4/1.21.4.jar --output ./my_extracted_assets
```

## How It Works

1. Extracts all files under the `assets/` directory from the JAR
2. Copies assets from the specified index in the assets directory
3. Fixes directory structure to ensure proper organization
4. Merges all resources into a consistent structure
