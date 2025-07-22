#!/bin/bash

# Configuration - easily modify these values as needed
SOURCE_DIR="path/to/your/data"  # Replace with your actual source directory
DEST_SERVER="rzeghlache@195.83.246.95"
DEST_DIR="/data_GPU/rzeghlache/carbure/"
EXCLUDE_FILE="${HOME}/.data_rsync_exclude"

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' not found."
    exit 1
fi

# Create exclude file if doesn't exist
if [ ! -f "$EXCLUDE_FILE" ]; then
    echo "Creating default exclude file at $EXCLUDE_FILE"
    cat > "$EXCLUDE_FILE" << EOF
*.tmp
.DS_Store
._.DS_Store
Thumbs.db
._*
~*
EOF
fi

# Check available space at source to estimate transfer size
SRC_SIZE=$(du -sh "$SOURCE_DIR" | cut -f1)

# Log the transfer for reference
echo "Starting data transfer to remote server at $(date)"
echo "  From: $SOURCE_DIR (Size: $SRC_SIZE)"
echo "  To: $DEST_SERVER:$DEST_DIR"
echo "  Using exclude patterns from: $EXCLUDE_FILE"

# Execute the rsync with reliable options:
# -a: archive mode (preserves permissions, timestamps, etc.)
# -v: verbose output
# -z: compression for faster transfer
# --progress: show progress during transfer
# --stats: show file transfer statistics
# --partial: keep partially transferred files (good for large transfers)
# --exclude-from: use exclude file

rsync -avz --progress --stats --partial \
      --exclude-from="$EXCLUDE_FILE" \
      "$SOURCE_DIR" \
      "$DEST_SERVER:$DEST_DIR"

# Check the exit status
if [ $? -eq 0 ]; then
    echo "Data transfer completed successfully at $(date)"
else
    echo "Error: Data transfer failed with exit code $? at $(date)"
    exit 1
fi