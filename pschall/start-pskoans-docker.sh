#!/bin/sh

set -e  # Exit on any error

# Get the canonical directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

# Create koans directory if it doesn't exist
KOANS_DIR="$SCRIPT_DIR/PSKoans"
mkdir -p "$KOANS_DIR"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Error: the Docker daemon is not running or your current user can't manage it."
    echo "Please start Docker first and be sure that you have the privileges to run docker."
    exit 1
fi

# Build image only if it doesn't exist
if ! docker image inspect pskoans-image > /dev/null 2>&1; then
    echo "Building PSKoans Docker image (first time only)..."

    # Build from HEREDOC
    docker build -t pskoans-image - << 'EOF'
FROM mcr.microsoft.com/powershell:lts-7.4-debian-12

# Create a user with the same UID as your host user (probably 1000)
RUN useradd -u 1000 -m -s /bin/bash pskoans-user

# Create workspace directory with proper ownership
WORKDIR /home/pskoans-user/PSKoans
RUN chown pskoans-user:pskoans-user /home/pskoans-user/PSKoans

# Switch to the user
USER pskoans-user

# Pre-install the modules as current user
# We configure the $Editor as 'cat' to avoid extra dependencies
RUN pwsh -c "\
    Install-Module Pester,PSKoans -Force -AllowClobber -Scope CurrentUser; \
    Set-PSKoanSetting -Name Editor -Value 'cat'; \
    Write-Host 'PSKoans environment ready!' -ForegroundColor Green"

# Default command
CMD ["pwsh", "-c", "\
    Write-Host '=== PSKoans Learning Environment ===' -ForegroundColor Green; \
    Write-Host 'Running as user: pskoans-user (UID: 1000)' -ForegroundColor Yellow; \
    Write-Host 'Your workspace: /home/pskoans-user/PSKoans' -ForegroundColor Yellow; \
    Write-Host ''; \
    Write-Host 'Commands:' -ForegroundColor Green; \
    Write-Host '  Show-Karma -Meditate    # Start learning' -ForegroundColor White; \
    Write-Host '  Show-Karma -List        # See all koans' -ForegroundColor White; \
    Write-Host '  Show-Karma              # Check progress' -ForegroundColor White; \
    pwsh"]
EOF

else
    echo "Using existing PSKoans image..."
fi

echo "Starting PSKoans environment..."
echo "Workspace directory: $KOANS_DIR"
echo "Mounted in container as: /home/pskoans-user/PSKoans"
echo "Running as user: pskoans-user (UID: 1000)"
echo "Press Ctrl+D or type 'exit' to leave the environment"
echo ""

# Run the container with the koans directory mounted
docker run -it --rm \
  -v "$KOANS_DIR:/home/pskoans-user/PSKoans" \
  --name pskoans \
  pskoans-image
