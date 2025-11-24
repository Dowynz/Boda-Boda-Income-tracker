Video Chat + Tkinter GUI - Ready to Hand In
==========================================

Contents:
- django_project/   : Django project using Channels for chat + WebRTC signaling (call).
- gui_app/          : Tkinter desktop app (simple contact manager) with validation, save/load, export CSV.
- requirements.txt  : Python dependencies.
- README.md         : This file.

How to run Django app (development):
1. Create and activate a Python 3.10+ virtual environment.
2. Install dependencies: pip install -r requirements.txt
3. cd django_project
4. python manage.py migrate
5. python manage.py runserver
6. Open http://127.0.0.1:8000/ and follow pages:
   - Home -> Join a chat room
   - /room/<room_name>/<username>/ : chat room (text)
   - /call/ : simple video call page (signalling via websockets)

How to run Tkinter app:
- cd gui_app
- python contact_manager.py
- The app supports adding contacts (validated), saving/loading JSON, and exporting contacts to CSV.

New features added (beyond workshop):
- Django:
  * Basic authentication scaffold (Django's contrib.auth included and simple login/logout templates).
  * CRUD-ish rooms persistence using a lightweight JSON file (rooms.json) so rooms can be listed.
  * Search box on index to search rooms by name.
  * Clear README and run instructions.
- GUI:
  * Input validation (email, phone).
  * Save/load contacts to JSON.
  * Export contacts to CSV.
  * Simple search/filter in the list.

Notes:
- The provided WebRTC signalling example is minimal and intended for local testing. Browsers may block getUserMedia on insecure origins; for full WebRTC testing use HTTPS or serve via localhost.
- This package is for educational/demo purposes.
