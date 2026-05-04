# Internship Outreach System (End-to-End)

This playbook turns your internship search into a repeatable system you can run every day.

## 1) Outcome and success metrics

**Primary outcome:** secure internship interviews for AI/Data/Software roles.

**KPIs to track weekly:**
- New leads added
- Personalized messages sent
- Positive replies
- Interview invitations
- Conversion rate = interviews / messages sent

Suggested 6-week baseline:
- 300 qualified contacts
- 150 personalized messages
- 20–30 positive replies
- 8–12 interviews

---

## 2) Stack (cheap and simple)

- **Google Sheets**: CRM database
- **n8n (self-hosted)**: reminders + message drafting workflow
- **Gmail**: direct outreach
- **ChatGPT**: CV/message personalization
- **Apollo/Hunter/Lusha (free tiers first)**: contact discovery/verification
- **Optional Mailmeteor**: small campaign batches

Start manually first; automate only repetitive low-risk steps.

---

## 3) CRM design (single source of truth)

Create one sheet named `Leads` with these columns:

1. `company`
2. `city`
3. `target_role`
4. `job_link`
5. `contact_name`
6. `contact_title`
7. `linkedin_url`
8. `email`
9. `email_verified` (yes/no)
10. `source`
11. `priority` (high/med/low)
12. `cv_version`
13. `msg_linkedin`
14. `msg_email`
15. `date_added`
16. `date_contacted`
17. `followup_date`
18. `status` (new/sent/replied/interview/rejected/no-response)
19. `last_action`
20. `notes`

Add a second sheet `Dashboard` with formulas:
- total leads
- contacts this week
- replies this week
- interviews this week
- response rate

---

## 4) Lead targeting strategy

Target contacts in this order:
1. Talent Acquisition / Recruiter
2. Campus Recruiter
3. HR Business Partner
4. Hiring Manager (Engineering/Data)
5. Alumni from your school in target team

For each company, capture **2–4 contacts max** (quality over quantity).

Search operators:
- `site:linkedin.com/in "Company" "Talent Acquisition"`
- `site:linkedin.com/in "Company" "Recruiter"`
- `site:linkedin.com/in "Company" "Engineering Manager"`
- `site:linkedin.com/in "Company" "Data"`

---

## 5) Personalization framework (what increases replies)

Each message must include:
1. **Who you are** (1 line)
2. **Why this company** (1 specific reason)
3. **Role scope** (AI/Data/Software)
4. **Proof** (1 project/skill relevant to them)
5. **Clear CTA** (ask for process/contact)

Use a short 60–90 word style for LinkedIn; 120–170 words for email.

---

## 6) n8n workflows to implement

## Workflow A — Lead enrichment + draft generation

Trigger: new row in `Leads` with `status = new`.

Steps:
1. Google Sheets Trigger
2. IF node: has email?
3. OpenAI node: generate `msg_linkedin` + `msg_email` using row context
4. Function node: set `followup_date = date_contacted + 4 days` (or from today if not contacted yet)
5. Google Sheets Update row

Output: row is ready-to-send with drafts.

## Workflow B — Daily follow-up reminders

Trigger: Cron daily at 09:00.

Steps:
1. Read rows where `followup_date = today` and `status in (sent, no-response)`
2. Send summary reminder to email/Telegram:
   - Name
   - Company
   - Last message date
   - Suggested follow-up text

Keep LinkedIn sending manual to reduce account risk.

---

## 7) Standard operating routine (daily + weekly)

## Daily block (1h50)
- 30 min: add 10 qualified leads
- 30 min: personalize 5 messages
- 20 min: send LinkedIn requests
- 20 min: send emails
- 10 min: update CRM statuses

## Weekly review (45 min)
- Review conversions by company and contact type
- Drop low-quality sources
- Improve message templates using best-performing variants
- Decide next week target sectors/companies

---

## 8) Anti-spam and quality rules

- Never mass-send generic text.
- Keep outreach under safe limits (especially LinkedIn).
- Always mention one concrete company-specific detail.
- Verify emails before sending.
- Stop follow-ups after 2 attempts if no response.

---

## 9) 14-day launch plan

Day 1–2:
- Build Sheets CRM + status taxonomy
- Draft 3 CV variants (AI/Data/Software)

Day 3–5:
- Add first 50 leads
- Send first 20 personalized contacts

Day 6–7:
- Run follow-up cycle #1
- Improve templates from reply signals

Week 2:
- Reach 120 total leads
- 60 sent messages
- 2 follow-up cycles
- Review interview conversion and adjust targeting

---

## 10) Copy/paste templates

### LinkedIn connect
Hi [Name], I’m Mohamed Amine, an engineering student focused on AI, data, and software development. I’m exploring 2026 internships at [Company] and would be glad to connect.

### LinkedIn after acceptance
Hi [Name], thank you for connecting. I’m seeking a summer/PFE internship in AI, data engineering, data analysis, or software engineering. I’m especially interested in [Company] because of [specific reason]. Would it be okay if I shared my CV, or could you point me to the right contact/process?

### Email
Subject: Internship Application – AI/Data/Software Engineering – Mohamed Amine El Abidi

Dear [Name],

I hope you are well. I’m Mohamed Amine El Abidi, an engineering student looking for a summer/PFE 2026 internship in AI, data engineering, data analysis, or software engineering.

I’m particularly interested in [Company] because of [specific reason]. I have hands-on experience in Python, ML, Power BI, backend development, and automation projects.

If possible, I’d be grateful to be considered for a relevant internship, or redirected to the correct recruitment contact.

Best regards,
Mohamed Amine El Abidi
LinkedIn: [link]
GitHub: [link]
Portfolio: [link]

### Follow-up (4–5 days)
Hi [Name], I’m following up on my earlier message regarding internship opportunities at [Company]. If helpful, I can resend my CV. I’d appreciate any guidance on the right person or process for AI/Data/Software Engineering internships.
