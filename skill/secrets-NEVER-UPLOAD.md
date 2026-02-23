# Secrets — LOCAL ONLY

> **WARNING: This file must NEVER be included in a skill ZIP, uploaded to Claude.ai, committed to a public repository, or shared with anyone.**
>
> Store this file locally on your machine only. If you use Git, add it to `.gitignore`.

## Moodle Instance

```
MOODLE_URL=https://your-moodle-instance.example.com
MOODLE_ADMIN_USER=
MOODLE_ADMIN_PASSWORD=
MOODLE_WS_TOKEN=
```

## Database (if applicable)

```
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

## API Keys

```
# Add any API keys used for integrations here
EXAMPLE_API_KEY=
```

## Environment Variables

```
# Copy these to your .env file or export them in your shell profile
export MOODLE_URL=""
export MOODLE_TOKEN=""
```

## Notes
- Rotate credentials regularly.
- Use environment variables or a secrets manager in production.
- Never paste credentials into Claude chat sessions.
