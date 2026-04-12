# Ampalone LinkedIn Page – Full Stack

## Project Structure
```
ampalone/
├── app.py           ← Flask backend (all API routes)
├── database.py      ← SQLite database setup & seed data
├── requirements.txt ← Python dependencies
├── ampalone.db      ← Auto-created on first run
└── static/
    ├── index.html   ← LinkedIn page (frontend)
    └── admin.html   ← Admin dashboard
```

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the server
```bash
python app.py
```

### 3. Open in browser
| URL | Page |
|-----|------|
| http://localhost:5000 | LinkedIn Page |
| http://localhost:5000/admin | Admin Dashboard |

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/company | Get company info |
| PUT | /api/company | Update company info |
| GET | /api/stats | Get all stats |
| PUT | /api/stats/:id | Update a stat |
| GET | /api/posts | Get all posts |
| POST | /api/posts | Create new post |
| PUT | /api/posts/:id | Update a post |
| DELETE | /api/posts/:id | Delete a post |
| POST | /api/contact | Submit contact form |
| GET | /api/contacts | Get all leads |
| DELETE | /api/contacts/:id | Delete a lead |

---

## Deploy to ampalone.com

1. Upload all files to your server's `public_html` folder
2. Install Python + pip on your hosting server
3. Run `pip install -r requirements.txt`
4. Start with `python app.py` or use **gunicorn**:
   ```bash
   pip install gunicorn
   gunicorn -w 4 app:app
   ```
5. Point your domain to port 5000 via your hosting panel
6.
