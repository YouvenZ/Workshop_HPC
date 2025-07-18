#!/bin/bash

# Configuration - easily modify these values as needed
SOURCE_IMAGE="path/to/your/image.sif"  # Replace with your actual source image path
DEST_SERVER="rzeghlache@195.83.246.95"
DEST_DIR="/data_GPU/rzeghlache/containers/"

# Check if source file exists
if [ ! -f "$SOURCE_IMAGE" ]; then
    echo "Error: Source image '$SOURCE_IMAGE' not found."
    exit 1
fi

# Get file size for info
IMAGE_SIZE=$(du -h "$SOURCE_IMAGE" | cut -f1)

# Log the transfer for reference
echo "Starting image transfer to remote server at $(date)"
echo "  Image: $SOURCE_IMAGE ($IMAGE_SIZE)"
echo "  To: $DEST_SERVER:$DEST_DIR"

# Execute the rsync with reliable options:
# -a: archive mode (preserves permissions, timestamps, etc.)
# -v: verbose output
# -z: compression for faster transfer
# -h: human-readable output
# --progress: show progress during transfer
# --stats: show file transfer statistics

rsync -avzh --progress --stats \
      "$SOURCE_IMAGE" \
      "$DEST_SERVER:$DEST_DIR"

# Check the exit status
if [ $? -eq 0 ]; then
    echo "Image transfer completed successfully at $(date)"
else
    echo "Error: Image transfer failed with exit code $? at $(date)"
    exit 1
fi