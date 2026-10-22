# iTech Backend

The Django backend behind the iTech platform. Three applications cover what the product needs:
accounting, RouterOS device provisioning, and users.

## Stack

| Layer | Choice |
|---|---|
| Backend | Python, Django |
| Apps | `Accounting`, `RouterOS`, `Users` |
| Provisioning | RouterOS / MikroTik API |

## Apps

- **Accounting** — `models.py` holds the accounting entities; this app owns the financial records
  and the rules around them.
- **RouterOS** — talks to MikroTik RouterOS to provision and manage devices, so network
  configuration is driven from the platform rather than by hand.
- **Users** — user accounts, roles and the admin surface.

Each app is a standard Django app with `models.py`, `admin.py`, `apps.py` and its own migrations.

## Running it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env        # DATABASE_URL, SECRET_KEY, DEBUG, RouterOS credentials
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Notes

- Database, secret key and RouterOS credentials come from the environment; nothing sensitive is
  committed.
- `admin.py` registers each app's models with the Django admin, which is what the platform's
  back-office screens are built on.
