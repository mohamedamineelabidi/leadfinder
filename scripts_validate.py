import json,sys
from pathlib import Path

files=[
 'automation/n8n/workflow_lead_intake_and_drafts.json',
 'automation/n8n/workflow_daily_followup_reminders.json'
]
errors=[]
for f in files:
    p=Path(f)
    if not p.exists():
        errors.append(f"Missing file: {f}")
        continue
    data=json.loads(p.read_text())
    for key in ['name','nodes','connections','active','version']:
        if key not in data:
            errors.append(f"{f}: missing key {key}")
    names={n.get('name') for n in data.get('nodes',[])}
    for src,conn in data.get('connections',{}).items():
        if src not in names:
            errors.append(f"{f}: connection source '{src}' missing in nodes")
        for lane in conn.get('main',[]):
            for edge in lane:
                tgt=edge.get('node')
                if tgt not in names:
                    errors.append(f"{f}: connection target '{tgt}' missing in nodes")
print('Validation complete')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('All workflow checks passed')
