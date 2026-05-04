# What you need to set up (required from you)

Before this automation can run, you must provide/configure these items:

1. **Google account with access to Google Sheets + Gmail APIs**
2. **DeepSeek API key** (used for message drafts via OpenAI-compatible API)
3. **n8n instance** (cloud or self-hosted)
4. **Spreadsheet ID** for your `Internship CRM` Google Sheet
5. **Your destination reminder email** (replace `your_email@example.com`)

## Exact configuration checklist

- [ ] Create Google Sheet named `Internship CRM`
- [ ] Import `templates/leads_sheet_headers.csv` into tab `Leads`
- [ ] Enable Google Sheets API + Gmail API in Google Cloud
- [ ] Create OAuth credentials and connect in n8n
- [ ] Add OpenAI credentials in n8n
- [ ] Import both JSON workflows from `automation/n8n/`
- [ ] Update all Google Sheets nodes with your spreadsheet ID
- [ ] Update Gmail node recipient email
- [ ] Add at least one lead row with `status = new`
- [ ] Run Workflow A manually and verify output columns populate
- [ ] Activate Workflow B after successful test

## Data format expectations

- `status` should start as `new` for fresh leads
- `followup_date` must be `YYYY-MM-DD`
- `email_verified` should be `yes` or `no`

## If you want, send me these 5 values and I can finalize a preconfigured version

1. Spreadsheet ID
2. Your reminder email
3. Preferred reminder time (currently 09:00)
4. Follow-up delay in days (currently +4)
5. Preferred DeepSeek model (currently `deepseek-chat`)
