# Zero-shot vs Few-shot Prompting

## Extraction Rules

- Return only valid JSON arrays.
- Use objects with exactly three keys: `name`, `email`, and `role`.
- Normalize names to title case.
- Normalize roles to clean title case.
- Use `null` for missing email addresses.
- Handle email-first records by detecting the email and using the remaining text for name and role.
- Drop duplicate contacts when the same name and email appear more than once.

## Zero-shot Prompt

```text
Extract every contact from the messy input into a valid JSON array.

Each contact must be an object with exactly these keys:
- name
- email
- role

Rules:
- Normalize names to title case.
- Normalize roles to clean title case.
- If an email is missing, use null.
- If the email appears before the name, still extract the correct name, email, and role.
- Remove duplicate contacts when the same name and email appear more than once.
- Return only JSON. Do not include markdown, comments, or explanation.

Input:
1) Jane Doe - jane@acme.io (Engineering Lead)
2) p. mensah, product manager, pmensah@acme.io
3) Kwesi — kwesi.b@acme.io – Designer
4) AMARA OKAFOR <amara.okafor@acme.io> | Data Scientist
5) tunde — (no email yet) — DevOps Engineer
6) "Zoe Lin" zoe.lin@acme.io ;; QA Engineer ;; (contractor)
7) r.silva@acme.io   Roberto Silva   Backend Engineer
8) Jane Doe   jane@acme.io   Engineering Lead     <- duplicate of #1
```

## Zero-shot Output

```json
[
  {
    "name": "Jane Doe",
    "email": "jane@acme.io",
    "role": "Engineering Lead"
  },
  {
    "name": "P. Mensah",
    "email": "pmensah@acme.io",
    "role": "Product Manager"
  },
  {
    "name": "Kwesi",
    "email": "kwesi.b@acme.io",
    "role": "Designer"
  },
  {
    "name": "Amara Okafor",
    "email": "amara.okafor@acme.io",
    "role": "Data Scientist"
  },
  {
    "name": "Tunde",
    "email": null,
    "role": "DevOps Engineer"
  },
  {
    "name": "Zoe Lin",
    "email": "zoe.lin@acme.io",
    "role": "QA Engineer Contractor"
  },
  {
    "name": "Roberto Silva",
    "email": "r.silva@acme.io",
    "role": "Backend Engineer"
  }
]
```

## Few-shot Prompt

```text
Extract contacts from messy text into a valid JSON array.

Output rules:
- Use exactly these keys: name, email, role.
- Normalize names to title case.
- Normalize roles to clean title case.
- Use null when the email is missing.
- If a line is email-first, identify the email first, then extract the name and role from the remaining text.
- Remove duplicates when the same name and email appear again.
- Return only JSON. Do not include markdown or explanations.

Example 1:
Input:
1) ama MENSAH — (no email yet) — data analyst

Output:
[
  {
    "name": "Ama Mensah",
    "email": null,
    "role": "Data Analyst"
  }
]

Example 2:
Input:
1) dev@acme.io   KOFI Boateng   platform engineer

Output:
[
  {
    "name": "Kofi Boateng",
    "email": "dev@acme.io",
    "role": "Platform Engineer"
  }
]

Example 3:
Input:
1) Jane Doe - jane@acme.io (Engineering Lead)
2) Jane Doe   jane@acme.io   Engineering Lead

Output:
[
  {
    "name": "Jane Doe",
    "email": "jane@acme.io",
    "role": "Engineering Lead"
  }
]

Now extract this input:
1) Jane Doe - jane@acme.io (Engineering Lead)
2) p. mensah, product manager, pmensah@acme.io
3) Kwesi — kwesi.b@acme.io – Designer
4) AMARA OKAFOR <amara.okafor@acme.io> | Data Scientist
5) tunde — (no email yet) — DevOps Engineer
6) "Zoe Lin" zoe.lin@acme.io ;; QA Engineer ;; (contractor)
7) r.silva@acme.io   Roberto Silva   Backend Engineer
8) Jane Doe   jane@acme.io   Engineering Lead     <- duplicate of #1
```

## Few-shot Output

```json
[
  {
    "name": "Jane Doe",
    "email": "jane@acme.io",
    "role": "Engineering Lead"
  },
  {
    "name": "P. Mensah",
    "email": "pmensah@acme.io",
    "role": "Product Manager"
  },
  {
    "name": "Kwesi",
    "email": "kwesi.b@acme.io",
    "role": "Designer"
  },
  {
    "name": "Amara Okafor",
    "email": "amara.okafor@acme.io",
    "role": "Data Scientist"
  },
  {
    "name": "Tunde",
    "email": null,
    "role": "DevOps Engineer"
  },
  {
    "name": "Zoe Lin",
    "email": "zoe.lin@acme.io",
    "role": "QA Engineer"
  },
  {
    "name": "Roberto Silva",
    "email": "r.silva@acme.io",
    "role": "Backend Engineer"
  }
]
```

## My Own Input

```text
1) ada LOVELACE <ada@acme.io> | machine learning lead
2) support@acme.io   Malik Stone   Customer Success Manager
3) Esi — (no email yet) — security analyst
4) ada lovelace ada@acme.io machine learning lead
```

## Zero-shot Output For My Input

```json
[
  {
    "name": "Ada Lovelace",
    "email": "ada@acme.io",
    "role": "Machine Learning Lead"
  },
  {
    "name": "Malik Stone",
    "email": "support@acme.io",
    "role": "Customer Success Manager"
  },
  {
    "name": "Esi",
    "email": null,
    "role": "Security Analyst"
  }
]
```

## Few-shot Output For My Input

```json
[
  {
    "name": "Ada Lovelace",
    "email": "ada@acme.io",
    "role": "Machine Learning Lead"
  },
  {
    "name": "Malik Stone",
    "email": "support@acme.io",
    "role": "Customer Success Manager"
  },
  {
    "name": "Esi",
    "email": null,
    "role": "Security Analyst"
  }
]
```

## Analysis

The few-shot prompt produced the more consistent result because the examples demonstrated the exact rules for missing email values, email-first ordering, and duplicate removal. The zero-shot prompt followed most of the instructions, but it treated `(contractor)` as part of Zoe Lin's role, which made the output less clean than intended.

The positive instructions were the strongest part of both prompts: normalize names, use `null`, remove duplicates, and return only JSON. The few-shot prompt also used examples to pin the output format and show the edge-case behavior instead of only describing it. I avoided negative instructions except for "do not include markdown or explanations" because the most important goal was a clean JSON array.
