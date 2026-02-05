# Simple YAML Config Project

## What this demonstrates
- YAML config file loaded into Python
- Validation with Pydantic models
- Environment variable overrides
- Hot reload when config.yaml changes
- Simple API to read config and toggle feature flags

## Setup
1. Create a virtual environment
   - `python -m venv .venv`
   - `source .venv/bin/activate` on Linux or macOS
   - `.venv\Scripts\activate` on Windows

2. Install dependencies
   - `pip install -r requirements.txt`

3. Validate YAML online before editing
   - Use **https://jsonformatter.org/yaml-validator** or **https://www.yamllint.com/**

## Run
- Start the app
  - `python app.py`
- Open `http://127.0.0.1:8000/config` to see current config

## Hot reload config
- Edit `config.yaml` and save
- The watcher prints `Config reloaded` and the app uses the new values
- For production, prefer a controlled admin endpoint and secret management

## Toggle a feature flag
- `curl -X POST http://127.0.0.1:8000/toggle-feature/new_ui`
- This updates `config.yaml` and triggers reload

## Notes and best practices
- **Do not store secrets** in YAML. Use environment variables or a secret manager.
- Validate config changes before deploying using yamllint or CI checks.
- For critical runtime changes use an authenticated admin API and safe reload logic.
