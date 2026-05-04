# Internship Automation Project - Implementation Guide

## What you now have
- `automation/n8n/workflow_lead_intake_and_drafts.json`
- `automation/n8n/workflow_daily_followup_reminders.json`
- `templates/leads_sheet_headers.csv`

## End-to-end setup steps

1. Create Google Sheet `Internship CRM`.
2. Import `templates/leads_sheet_headers.csv` into sheet tab `Leads`.
3. Create Google Cloud credentials for Sheets + Gmail APIs.
4. In n8n, configure credentials:
   - Google Sheets OAuth2
   - Gmail OAuth2
   - OpenAI API key
5. Import both workflow JSON files from `automation/n8n/`.
6. In each Google Sheets node, set Spreadsheet ID and tab `Leads`.
7. In `Send Reminder Email`, replace `your_email@example.com` with your real address.
8. Test workflow A with one row where `status = new`.
9. Verify that `msg_linkedin`, `msg_email`, and `followup_date` populate.
10. Activate workflow B after successful test.

## Operational rules
- Keep LinkedIn sending manual or low volume.
- Only automate drafts + reminders.
- Update `status` every day (`sent`, `replied`, `interview`, etc.).

## Recommended cadence
- Add 10 leads/day
- Send 5 personalized outreaches/day
- Follow up at +4 days, then +9 days
- Stop after 2 follow-ups if no response
