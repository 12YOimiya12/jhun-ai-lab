"""
Cloudflare Worker entry point for the Flask app.
Uses the cloudflare/python-workers runtime.

To deploy:
1. Install wrangler: npm install -g wrangler
2. Login: wrangler login
3. Deploy: wrangler deploy

Alternatively, for Cloudflare Pages + Workers hybrid:
- Static files (CSS/JS/HTML) → Cloudflare Pages
- API routes → Cloudflare Workers
"""

# This file serves as the entry point for Cloudflare Workers.
# When using @cloudflare/python-workers, this is the main module.

# For now, we provide both deployment options:
# Option A: Full Python Worker (worker.py)
# Option B: Static export for Cloudflare Pages + separate API Worker

import sys
import os

# Add the app directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app


# Cloudflare Workers entry point
async def fetch(request, env, ctx):
    """Handle incoming requests for Cloudflare Workers."""
    # This would use a WSGI-to-ASGI adapter in production
    # For now, we document the deployment approach
    pass


# For local development
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
