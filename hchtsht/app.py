#!/usr/bin/env python3
"""
Minimal Flask app for searching and viewing cheatsheets.
Security-focused with input validation and sanitization.
"""

import subprocess
from urllib.parse import unquote

from pathlib import Path
import os

import markdown
from markupsafe import escape
from flask import Flask, render_template, request, abort, send_from_directory

import config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(config)

# Security: Sanitize search input
def sanitize_search_input(search_term):
    """Validate and sanitize search input to prevent command injection."""
    if not search_term:
        return ""

    # Limit length
    if len(search_term) > config.MAX_SEARCH_LENGTH:
        search_term = search_term[:config.MAX_SEARCH_LENGTH]

    # Remove dangerous characters
    # Only allow characters that are safe for ripgrep search
    sanitized = ''.join(
        char for char in search_term 
        if char in config.ALLOWED_SEARCH_CHARS
    )

    return sanitized.strip()

# Security: Validate file path
def validate_filepath(filepath):
    """Ensure requested file is within cheatsheets directory and is a markdown file."""
    if not filepath:
        return None

    try:
        # Decode URL-encoded path
        decoded = unquote(filepath)

        # Convert to absolute path
        requested = (config.CHEATSHEETS_DIR / decoded).resolve()
        cheatsheets_root = config.CHEATSHEETS_DIR.resolve()

        # Security checks
        if not str(requested).startswith(str(cheatsheets_root)):
            return None  # Path traversal attempt

        if not requested.is_file():
            return None  # Not a file

        # Remove extension check or expand it
        if requested.suffix.lower() not in config.ALLOWED_EXTENSIONS:
            return None

        return requested
    except:
        return None

def search_cheatsheets(query):
    """Search markdown files using ripgrep safely."""
    if not query:
        return []

    try:
        # Build and execute command
        cmd = [
            config.RIPGREP_CMD,
            "-il",  # Case-insensitive, list files only
            "--",   # Safety: end of options
            query,
            str(config.CHEATSHEETS_DIR)
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)

        if result.returncode != 0 or not result.stdout:
            return []

        # Process results - get relative paths
        cheatsheets_path = Path(config.CHEATSHEETS_DIR)
        results = []

        for line in result.stdout.strip().splitlines():
            try:
                if line:
                    full_path = Path(line)
                    # Convert to relative path
                    rel_path = full_path.relative_to(cheatsheets_path)
                    results.append(str(rel_path))
            except:
                # Skip if not in cheatsheets directory (shouldn't happen)
                continue

        return results

    except subprocess.TimeoutExpired:
        return []
    except Exception:
        return []


def render_markdown(content):
    """Render markdown to HTML."""
    if not content:
        return ""

    return markdown.markdown(content, extensions=['fenced_code', 'tables'])

@app.route('/')
def index():
    """Home page with search form and results."""
    query = request.args.get('q', '').strip()

    # If no search query, show welcome page
    if not query:
        return render_template('index.html')

    # Sanitize input
    safe_query = sanitize_search_input(query)

    if not safe_query:
        return render_template('index.html', results=[], query=query)

    # Perform search
    results = search_cheatsheets(safe_query)

    return render_template('index.html', results=results, query=query)

@app.route('/view')
def view_file():
    """View a markdown file."""
    filepath = request.args.get('f', '').strip()
    search_query = request.args.get('q', '')  # Keep search query for back link

    # Validate file path
    validated_path = validate_filepath(filepath)

    if not validated_path:
        abort(404)

    try:
        # Read file content
        with open(validated_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if validated_path.suffix.lower() == ".md":

            # Convert markdown to HTML
            html_content = render_markdown(content)

            return render_template('view.html', 
                                 content=html_content,
                                 filepath=filepath,
                                 search_query=search_query)
        else:
            # For non-markdown files, escape and wrap in code block
            lang = validated_path.suffix.lower()[1:]  # Remove dot
            escaped_content = escape(content)
            code_block = f'<pre><code class="language-{lang}">{escaped_content}</code></pre>'
            return render_template('view.html',
                                 content=code_block,
                                 filepath=filepath,
                                 search_query=search_query)

    except:
        abort(404)

@app.route('/static/cheatsheets/<path:filename>')
def cheatsheet_static(filename):
    """Serve static files from cheatsheets directory."""
    return send_from_directory(config.CHEATSHEETS_DIR, filename)

@app.template_filter('dirname')
def dirname(path):
    """Get directory name from path."""
    return os.path.dirname(path) or '.'

# Error handlers
@app.errorhandler(404)
def page_not_found(_):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(_):
    return render_template('500.html'), 500

# Main entry point
if __name__ == '__main__':
    # Security: Disable debug in production
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=False
    )
