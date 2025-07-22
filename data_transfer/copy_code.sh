#!/bin/bash
# Configuration - easily modify these values as needed
SOURCE_DIR="/home/youven/code/HPC_workshop"  # Replace with your actual source directory
DEST_SERVER="rzeghlache@195.83.246.95"
DEST_DIR="/data_GPU/rzeghlache/"
EXCLUDE_FILE="${SOURCE_DIR}/rsync_ignore.text"

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' not found."
    exit 1
fi

# Check if exclude file exists
if [ ! -f "$EXCLUDE_FILE" ]; then
    echo "Warning: Exclude file '$EXCLUDE_FILE' not found. Creating empty one."
    touch "$EXCLUDE_FILE"
fi

# Log the transfer for reference
echo "Starting code transfer to remote server at $(date)"
echo "  From: $SOURCE_DIR"
echo "  To: $DEST_SERVER:$DEST_DIR"
echo "  Using exclude patterns from: $EXCLUDE_FILE"

# Execute the rsync with reliable options:
# -a: archive mode (preserves permissions, timestamps, etc.)+
# -v: verbose output
# -z: compression for faster transfer
# -h: human-readable output
# --progress: show progress during transfer
# --stats: show file transfer statistics
# --delete: remove files on destination that are no longer in source (optional)

rsync -avzh --progress --stats \
      --exclude-from="$EXCLUDE_FILE" \
      "$SOURCE_DIR" \
      "$DEST_SERVER:$DEST_DIR"

# Check the exit status
if [ $? -eq 0 ]; then
    echo "Transfer completed successfully at $(date)"
else
    echo "Error: Transfer failed with exit code $? at $(date)"
    exit 1
fi