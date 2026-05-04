# Configure this project to use DeepSeek API

You can use DeepSeek instead of OpenAI for draft generation.

## Option A (recommended): n8n OpenAI-compatible Chat Model credentials

DeepSeek supports OpenAI-compatible API format.

1. In n8n, create credentials for **OpenAI-compatible API** (or OpenAI with custom base URL, depending on your n8n version).
2. Set:
   - **Base URL**: `https://api.deepseek.com`
   - **API Key**: your DeepSeek key
3. In `Generate Drafts` node, set model to one of:
   - `deepseek-chat` (recommended for outreach drafting)
   - `deepseek-reasoner` (more reasoning, usually slower/costlier)

## Option B: Replace with HTTP Request node

If your n8n version does not support custom OpenAI base URL, replace the OpenAI node with HTTP Request:

- Method: `POST`
- URL: `https://api.deepseek.com/chat/completions`
- Headers:
  - `Authorization: Bearer <DEEPSEEK_API_KEY>`
  - `Content-Type: application/json`
- JSON body:

```json
{
  "model": "deepseek-chat",
  "messages": [
    {"role": "system", "content": "You write concise, personalized internship outreach messages."},
    {"role": "user", "content": "Generate JSON with keys linkedin_message and email_message for this lead: ..."}
  ],
  "temperature": 0.4
}
```

Then map response from:
- `choices[0].message.content`

## Important parsing note

Your workflow expects valid JSON text from the model response. Keep the prompt instruction:
- "Return only JSON with keys linkedin_message and email_message"

If parsing fails, add a Code node with try/catch fallback and default empty messages.
