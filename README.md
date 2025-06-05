# SpaceX Launch Explorer

A web application for browsing and managing SpaceX rocket launches using the public SpaceX API and a custom user system. The app offers a sleek, interactive SCI-FI-style interface, dynamic data integration, and user-friendly features such as favorites, filters, and animations.

---

## Features

### User Authentication and Security
- User registration and login system built with **Django Auth**
- Secure session management
- Favorites feature available only to logged-in users
- Optional login via **Google OAuth**

### External API Integration
- Real-time data fetched from the [SpaceX API](https://api.spacexdata.com/v4/launches/)
- Launch details include:
  - Name, date, description, images
  - Links to YouTube videos and Wikipedia articles
- Additional rocket data fetched via `/v4/rockets/{id}` (e.g. name, mass, engine details)

### RESTful Architecture
- `GET` requests for fetching external API data
- `POST` and `DELETE` methods for managing favorites
- Logical routing and resource handling following REST principles

---

## Core Application Features

- **Launch Sorting**  
  Sort launches by:
  - Name (A–Z / Z–A)
  - Date (ascending / descending)

- **Launch Details View**  
  - Full launch information
  - Rocket specifications
  - Mission success/failure status
  - Image gallery and external links

- **Favorites System**  
  - Add/remove launches to/from your favorites
  - Favorites are user-specific and stored in the database
  - Duplicate prevention
  - Dedicated page to view saved favorites

- **Visual Effects and UI**  
  - Custom CSS styling (cards, grid layout, buttons, hover effects)
  - **Animated starfield background** using Canvas and JavaScript
  - **Fade-in animations** for launch cards
  - **Scroll-to-top button** for better navigation

---

## Database

- **Database Engine**: PostgreSQL
- **Local Models**:
  - `User`: Django’s built-in user model
  - `FavoriteLaunch`: Links users with their favorite launches
- **CRUD Operations**:
  - Add and remove favorite launches
  - Check if a launch is already in a user’s favorites
  - Prevent duplicate entries

---

## Technologies Used

| Layer        | Technologies                  |
|--------------|-------------------------------|
| **Backend**  | Python, Django                |
| **Frontend** | HTML5, CSS3, JavaScript       |
| **Database** | PostgreSQL                    |
| **API**      | SpaceX API                    |
| **UI/UX**    | Custom design, Canvas effects |

---

## Screenshots

![Screenshot 2025-05-09 115427](https://github.com/user-attachments/assets/7892c33f-47f1-43c6-8ea0-3dbfd813693d)
![Screenshot 2025-05-09 115516](https://github.com/user-attachments/assets/23ce9099-cd90-41bd-b747-3ae54396f058)
![Screenshot 2025-05-09 115531](https://github.com/user-attachments/assets/0e9af765-f030-4e84-b8a3-0da9a180bf9d)


---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/spacex-launch-explorer.git
   cd spacex-launch-explorer
2. **Create .env file with the following variables:**
```bash
  SECRET_KEY=<djangosecretkey>
  DB_NAME=<name-of-database>
  DB_USER=<database-user>
  DB_PASSWORD=<password-for-database-user>
  DB_HOST=<database-host>
  DB_PORT=<database-port>
  
  CLIENT_ID=<google-client-id>
  CLIENT_SECRET=<google-secret>
