# Airport API

## Overview
Airport API is a Django REST Framework project designed to manage airports, flights, airplanes, crew members, routes, orders, and tickets.  
This service allows users to track flights worldwide, make orders, and view ticket information.  
The API is fully documented using **Swagger** for easy exploration.

---

## Features
- **Airports:** CRUD operations for airports and closest major cities  
- **Flight Routes:** Create, read, update, and delete routes between airports  
- **Airplanes & Airplane Types:** Manage airplane models, types, rows, and seats per row  
- **Crew Members:** Add and manage flight crew  
- **Flights:** Schedule flights with airplanes, routes, and crew assignments  
- **Orders & Tickets:** Users can create orders and tickets (restricted to authenticated users)  
- **Permissions:**  
  - Read-only access for anonymous users  
  - Full access for authenticated users on Orders & Tickets  
- **Swagger Documentation:** Interactive API documentation with all endpoints

---

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd airport-api
```

### Installation & Setup

```bash
python -m venv venv
# Windows: venv\Scripts\activate | Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver