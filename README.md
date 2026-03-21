# Physio Clinic

Physio Clinic is a full-stack web application designed to allow clients to browse physiotherapists, book appointments, and manage their bookings. Physiotherapists can view and manage their schedules, block time periods, and add internal notes.

This README outlines the project, features, deployment details, user instructions, technologies used, and how to contribute or test locally.

---

## Project Overview

Physio Clinic is a medical appointment scheduling platform with the following goals:

- Provide a client-friendly booking experience
- Support physiotherapists in managing their schedules
- Ensure secure authentication and role-based views
- Offer an intuitive, mobile-friendly interface

This project implements CRUD functionality for bookings and slots, Agile methodology tracking, and appropriate user stories.

The application is deployed to Heroku and can be accessed at:

**https://physio-clinic-d609e92202b3.herokuapp.com/**

---

### User Goals

#### As a Patient (Client):

- To easily browse a list of qualified physiotherapists and view their specializations.
- To check real-time availability and book an appointment without needing to call the clinic.
- To manage personal bookings, including viewing upcoming sessions and having the ability to cancel if plans change.
- To provide additional context to the specialist by leaving notes during the booking process.

#### As a Physiotherapist (Staff):

- To have an automated, organized schedule that generates slots for the weeks ahead.
- To manually manage availability by blocking specific times for breaks or personal leave.
- To see client details and notes for each appointment in a clear dashboard.
- To maintain professional boundaries by having the authority to cancel or modify slots as needed.

### Site Owner Goals
- Service Automation: Reduce administrative overhead by allowing clients to book slots directly through the platform.
- Efficiency: Ensure that physiotherapists' working hours are fully utilized through automated slot generation and easy-to-manage schedules.
- Data Integrity: Maintain an accurate database of specialists, clients, and appointments with built-in protections against scheduling overlaps.
- Professionalism: Provide a secure, user-friendly interface that builds trust between the clinic and its patients.


---

### Target Audience
* **Patients (Clients):** Individuals seeking physical therapy who prefer a quick, digital way to book appointments without phone calls.
* **Physiotherapists (Medical Staff):** Professionals who need an organized, automated way to manage their daily schedule and patient flow.
* **Clinic Administrators:** System owners who manage staff credentials and ensure the integrity of the medical practitioner list.

### User Requirements and Expectations
* **Security & Access Control:** * Patients expect their booking data to be private.
    * Staff accounts must be created exclusively by a Superuser to prevent unauthorized individuals from posing as medical professionals.
* **Simplicity:** A clean, intuitive interface that allows booking a slot in just a few clicks.
* **Automation:** The system should handle repetitive tasks, such as generating daily slots for the upcoming weeks.
* **Reliability:** * Users expect real-time updates (a slot should disappear once booked).
    * Prevention of double-booking or booking in the past.
* **Visual Clarity:** Clear distinction between "Available", "Booked", and "Blocked" time slots using a color-coded system.

## Agile Methodology

The development of **Physio Clinic** followed Agile principles, utilizing a GitHub Projects board for task tracking, prioritization, and sprint planning.

### User Stories

To ensure a user-centric approach, the project was broken down into granular User Stories. Each story includes specific **Acceptance Criteria** to define the boundaries of the feature.

| ID | User Role | Requirement | Goal/Benefit |
|:---|:----------|:------------|:-------------|
| #1 | Visitor | Register as a client | To book appointments online |
| #2 | User | Login & Role-based redirect | To access personal dashboard |
| #5 | Client | Book an available slot | To schedule a session |
| #8 | Physio | View personal schedule | To manage daily workload |
| #10| Physio | Update booking notes | To keep track of patient treatment |
| #11| Physio | Block time slots | To manage breaks or vacations |

### Project Management (Kanban)
The project was managed using a MoSCoW prioritization technique (Must-have, Should-have, Could-have):
* **Must-have:** Authentication, Booking logic, Dashboards.
* **Should-have:** Admin management, Slot blocking, Notes.
* **Could-have:** Email confirmations (under development).

![Project Board Screenshot](docs/screenshots/project_board.png)
*Figure: GitHub Project Board showcasing the development workflow and task statuses.*

### 🛠 Development Workflow
For this project, I employed a **Trunk-Based Development** strategy:
* **Rapid Iteration:** Due to the solo nature of the project and the need for rapid prototyping, all features were integrated directly into the main branch after local successful testing.
* **Feature Atomicity:** Each commit message was mapped to a specific User Story ID (e.g., `feat: implement slot blocking #3`) to maintain traceability despite the lack of Pull Requests.
* **Continuous Integration:** Regular pushes ensured that the environment (Heroku/Render) stayed synchronized with the latest stable code.

### 🎯 Project Milestones

| Milestone | Status | Key Features |
|:----------|:-------|:-------------|
| **Phase 1: Foundation** | Done | Authentication, Role-based access, Admin CRUD |
| **Phase 2: MVP Booking** | Done | Physio browsing, Real-time booking logic, Basic Dashboards |
| **Phase 3: Management** | Done | Slot blocking, Internal notes, Cancellations, Media handling |
| **Phase 4: Future** | Backlog | Email notifications, Treatment history, Automated Payroll |

## Design

### Colours
The colour palette was chosen to reflect a professional, trustworthy, and calm medical environment. I focused on a "Clean Clinical" theme with high-contrast elements for accessibility.

* **Primary Blue (`#007bff`):** Used for primary action buttons (e.g., "Book an appointment") to guide the user toward key actions.
* **Slate Dark (`#343a40`):** Used for the navigation bar to provide a solid, professional frame for the content.
* **Success Green (`#198754`):** Used for "Available" status badges and positive actions like "Save Slot".
* **Danger Red (`#dc3545`):** Used for "Cancel" and "Delete" actions to warn the user of destructive operations.

### Fonts
The site utilizes a **Sans-Serif** typography stack (standard web fonts like Roboto/Arial). This ensures maximum readability across all devices, which is a critical requirement for healthcare platforms to remain accessible to all patient demographics, including those with visual impairments.

### Structure

#### Website Pages
The site is designed with a responsive layout, featuring a navigation bar for easy access and a hamburger menu for smaller screens.

| Page | Description | Desktop | Tablet | Mobile |
|:---|:---|:---:|:---:|:---:|
| **Home** | Landing page with a list of active physiotherapists and their specializations. | [<img src="docs/screenshots/home_dsktp.png" width="180">](docs/screenshots/home_dsktp.png) | [<img src="docs/screenshots/home_tab.png" width="100">](docs/screenshots/home_tab.png) | [<img src="docs/screenshots/home_mob.png" width="60">](docs/screenshots/home_mob.png) |
| **Registration** | Public form for visitors to register as new patients. | [<img src="docs/screenshots/reg_dsktp.png" width="180">](docs/screenshots/reg_dsktp.png) | [<img src="docs/screenshots/reg_tab.png" width="100">](docs/screenshots/reg_tab.png) | [<img src="docs/screenshots/reg_mob.png" width="60">](docs/screenshots/reg_mob.png) |
| **Login** | Secure authentication portal for clients and staff. | [<img src="docs/screenshots/login_dsktp.png" width="180">](docs/screenshots/login_dsktp.png) | [<img src="docs/screenshots/login_tab.png" width="100">](docs/screenshots/login_tab.png) | [<img src="docs/screenshots/login_mob.png" width="60">](docs/screenshots/login_mob.png) |
| **Choose a physiotherapist** | First view to booking and choose a physiotherapist. | [<img src="docs/screenshots/physio_dsktp.png" width="180">](docs/screenshots/physio_dsktp.png) | [<img src="docs/screenshots/physio_tab.png" width="180">](docs/screenshots/physio_tab.png) | [<img src="docs/screenshots/physio_mob.png" width="60">](docs/screenshots/physio_mob.png) |
| **Booking Selection** | Real-time availability grid for selecting specific time slots. On the physiotherapist's account, this is for information purposes only. Bookings are disabled. | [<img src="docs/screenshots/booking_dsktp.png" width="180">](docs/screenshots/booking_dsktp.png) | [<img src="docs/screenshots/booking_tab.png" width="100">](docs/screenshots/booking_tab.png) | [<img src="docs/screenshots/booking_mob.png" width="60">](docs/screenshots/booking_mob.png) |
| **Client Dashboard** | Personal area for patients to manage their upcoming appointments. | [<img src="docs/screenshots/client_dash_dsktp.png" width="180">](docs/screenshots/client_dash_dsktp.png) | [<img src="docs/screenshots/client_dash_tab.png" width="100">](docs/screenshots/client_dash_tab.png) | [<img src="docs/screenshots/client_dash_mob.png" width="60">](docs/screenshots/client_dash_mob.png) |
| **Physiotherapists Dashboard** | Overview hub for physiotherapists showing their daily stats. | [<img src="docs/screenshots/staff_dash_dsktp.png" width="180">](docs/screenshots/staff_dash_dsktp.png) | [<img src="docs/screenshots/staff_dash_tab.png" width="100">](docs/screenshots/staff_dash_tab.png) | [<img src="docs/screenshots/staff_dash_mob.png" width="60">](docs/screenshots/staff_dash_mob.png) |
| **My Schedule** | Professional tool for staff to block slots, add notes, or cancel sessions. | [<img src="docs/screenshots/schedule_dsktp.png" width="180">](docs/screenshots/schedule_dsktp.png) | [<img src="docs/screenshots/schedule_tab.png" width="100">](docs/screenshots/schedule_tab.png) | [<img src="docs/screenshots/schedule_mob.png" width="60">](docs/screenshots/schedule_mob.png) |
| **Create Slot** | Professional tool for staff to block slots, add notes, or cancel sessions. | [<img src="docs/screenshots/slot_dsktp.png" width="180">](docs/screenshots/slot_dsktp.png) | [<img src="docs/screenshots/slot_tab.png" width="100">](docs/screenshots/slot_tab.png) | [<img src="docs/screenshots/slot_mob.png" width="60">](docs/screenshots/slot_mob.png) |
| **404 Page** | A 404 page appears when a page cannot be found.  | [<img src="docs/screenshots/404_dsktp.png" width="180">](docs/screenshots/404_dsktp.png) | [<img src="docs/screenshots/404_tab.png" width="100">](docs/screenshots/404_tab.png) | [<img src="docs/screenshots/404_mob.png" width="60">](docs/screenshots/404_mob.png) |

#### Database

- Built with **Python** and the **Django** framework.
- Uses **PostgreSQL** for the deployed production version and **SQLite3** for development.
- The relational database schema ensures high data integrity between users and time-sensitive slots.

#### Database Schema
<img src="docs/screenshots/database_schema.png" width="800">


This relational diagram illustrates the complex connections between our three core models, linked via Django's default User model:
* **ClientProfile** is linked to User via `OneToOneField`.
* **Physiotherapist** is linked to User via `OneToOneField`.
* **BookingSlot** acts as the linking entity, holding a `ForeignKey` to Physiotherapist and a nullable `ForeignKey` to User (as Client).

##### User Model (Django Built-in)
- `id` (PrimaryKey)
- `username` / `password`
- `email`
- `first_name` / `last_name`
- `is_staff` / `is_superuser`

##### ClientProfile Model
- `user` (OneToOneField to User)
- `phone` (CharField)
- `insurance_number` (CharField)

##### Physiotherapist Model
- `user` (OneToOneField to User)
- `specialization` (CharField)
- `short_description` (CharField)
- `bio` (TextField)
- `photo` (ImageField)
- `working_from` / `working_to` (TimeFields)
- `last_generated_until` (DateField)
- `is_active` (BooleanField)

##### BookingSlot Model
- `physiotherapist` (ForeignKey)
- `client` (ForeignKey, null=True)
- `date` (DateField)
- `start_time` / `end_time` (TimeFields)
- `status` (Available, Booked, Blocked)
- `physio_note` (CharField)
- `client_note` (TextField)
- `blocked_reason` (CharField)

## Technologies Used

### Languages & Frameworks

- **HTML5 / CSS3** – Used to build the structural and visual foundation of the application.
- **Python (3.12+)** – The primary programming language for backend development.
- **Django (5.2)** – The high-level Python framework used to build the core logic, ORM models, and secure authentication system.

### Libraries & Tools

- **PostgreSQL** – Professional relational database used for production.
- **Psycopg2-binary** – PostgreSQL adapter for Python, enabling seamless database communication.
- **Gunicorn** – A high-performance WSGI HTTP Server used for production deployment on Heroku.
- **WhiteNoise** – Optimized middleware used to serve static files directly through Django, ensuring high efficiency in production.
- **Pillow** – Imaging library used to process and manage physiotherapist profile photos.
- **Dj-database-url** – Utility to allow the use of the `DATABASE_URL` environment variable for seamless database configuration on Heroku.
- **Python-dotenv** – Used to manage sensitive environment variables (like SECRET_KEY and DB credentials) during development.
- **Bootstrap 5** – (via CDN) Used for rapid development of a responsive, mobile-first user interface.
- **Heroku** – Cloud platform used for hosting and managing the live application.
- **Git / GitHub** – Used for version control and project task management (Kanban).

## Features

### Header & Footer

The navigation and site structure are designed to be intuitive, providing a seamless experience across all devices while adapting to the user's role.

#### Dynamic Navigation Bar
The Header (Navbar) is the central navigation hub. It uses Django's authentication logic to display relevant links based on whether a user is a Guest, a Patient, or a Staff member.

- **Guest View**: Provides a clean interface with "Login" and "Register" actions for new or returning visitors.
<img src="docs/screenshots/header_guest.png">
- **Patient View**: Greets the user by name and provides direct access to "My Dashboard" to manage personal appointments.
<img src="docs/screenshots/header_client.png">
- **Physiotherapist (Staff) View**: Displays professional tools such as "Physio Dashboard" and "Schedule" for real-time slot management.
<img src="docs/screenshots/header_phis.png">
- **Responsive Design**: On smaller screens (Tablets/Mobile), the navigation links collapse into a "hamburger" menu to maintain usable screen space. <br>
<img src="docs/screenshots/header_mob.png">

#### Footer
The Footer provides a consistent anchor at the bottom of every page, ensuring branding and authorship are always visible.
- **Minimalist Design**: Focuses on essential information without cluttering the user interface.
<img src="docs/screenshots/footer_dskt.png">
- **Copyright & Attribution**: Displays the clinic name and developer credits, reinforcing a professional project standard.<br>
<img src="docs/screenshots/footer_mob.png">

### **Home Page**
The Home Page is designed to provide users with a quick overview of the clinic's services and immediate access to the booking system.

| Element Name | Description | Image Reference (Click to enlarge) |
|:---|:---|:---:|
| **Welcome Section** | A high-impact hero area with a clear heading and mission statement about secure and fast appointment booking. | [<img src="docs/screenshots/home_hero.png" width="180">](docs/screenshots/home_hero.png) |
| **Specialist Cards** | Individual blocks showcasing each physiotherapist’s profile photo, specialization, and a brief biography to help patients choose the right expert. A "View available slots" button on each specialist card that directs the user straight to that specific doctor's real-time schedule. | [<img src="docs/screenshots/home_cards.png" width="180">](docs/screenshots/home_cards.png) |
| **General Booking CTA** | A primary "Book an appointment" button. As the clinic scales and staff numbers increase, this button redirects users to a full directory of all specialists. | [<img src="docs/screenshots/home_cta_book.png" width="180">](docs/screenshots/home_cta_book.png) |

<details>
<summary>Click to view Responsive Comparison (Desktop, Tablet, Mobile)</summary>

#### **Responsive Comparison**
The landing page layout is fully responsive, ensuring a seamless experience across desktop, tablet, and mobile devices.

| Desktop View | Tablet View | Mobile View |
|:---:|:---:|:---:|
| [<img src="docs/screenshots/home_dsktp.png" width="180">](docs/screenshots/home_dsktp.png) | [<img src="docs/screenshots/home_tab.png" width="100">](docs/screenshots/home_tab.png) | [<img src="docs/screenshots/home_mob.png" width="60">](docs/screenshots/home_mob.png) |
</details>

### **Authentication (Registration & Login)**
The application uses Django’s built-in authentication system to ensure that patient data remains private and that only authorized users can manage appointments.

| Element Name | Description | Image Reference (Click to enlarge) |
|:---|:---|:---:|
| **Client Registration** | A comprehensive form that collects essential user data (Name, Username, Email, and Password). Includes real-time validation for unique usernames and password security. | [<img src="docs/screenshots/reg_dsktp.png" width="180">](docs/screenshots/reg_dsktp.png) |
| **Login Page** | A secure entry point for existing users. Once authenticated, the system redirects the user to their specific dashboard based on their role (Patient or Staff). | [<img src="docs/screenshots/login_dsktp.png" width="180">](docs/screenshots/login_dsktp.png) |

> [!IMPORTANT]
> **User Access Control (Defensive Design):**
> If an unauthenticated (guest) user attempts to book a slot, the system automatically redirects them to the **Login Page**. Access to the booking confirmation and personal dashboards is strictly restricted to logged-in users only.

### **Choose a Physiotherapist Page**
This intermediate page acts as a comprehensive directory. It allows patients to browse the full list of medical staff, ensuring scalability as the clinic grows and more specialists join the team.

| Element Name | Description | 
|:---|:---|
| **Page Title** | A direct and user-friendly title that guides the patient in the first step of the booking process. | 
| **Specialist List** | A clean, minimalist list of all registered physiotherapists. Each name is a unique link. | 
| **Selection Link** | A click on a name redirects the user directly to that specific physiotherapist’s dynamic availability grid for booking. | 

<details>
<summary>Click to view Responsive Comparison (Desktop, Tablet, Mobile)</summary>

#### **Responsive Comparison**
This list maintains a consistent and readable layout across all screen sizes, from large monitors to mobile touchscreens.

| Desktop View | Tablet View | Mobile View |
|:---:|:---:|:---:|
| [<img src="docs/screenshots/physio_dsktp.png" width="180">](docs/screenshots/physio_dsktp.png) | [<img src="docs/screenshots/physio_tab.png" width="180">](docs/screenshots/physio_tab.png) | [<img src="docs/screenshots/physio_mob.png" width="60">](docs/screenshots/physio_mob.png) |
</details>

### **Booking Selection Page**
This page allows patients to view and reserve specific time slots with their chosen physiotherapist. The interface is designed to be clean and intuitive, ensuring a smooth booking process.

| Element Name | Description | Image Reference (Click to enlarge) |
|:---|:---|:---:|
| **Dynamic Header** | Clearly states the name of the physiotherapist the patient is currently booking with to ensure clarity. | [<img src="docs/screenshots/booking_header.png" width="180">](docs/screenshots/booking_header.png) |
| **Appointment Cards** | Instead of a complex table, slots are presented as individual cards, each showing the specific date and time interval. Each slot includes an optional text area ("Tell us more...") where patients can provide brief details about their symptoms or needs before confirming. Only available slots are displayed. Once a slot is booked, it immediately disappears from the view to prevent double-booking (Defensive Design). Upon clicking the "Book Slot" button, the reservation is processed, and the user is automatically redirected to their **My Dashboard** to view the confirmed appointment. | [<img src="docs/screenshots/booking_card.png" width="180">](docs/screenshots/booking_card.png) |

<details>
<summary>Click to view Responsive Comparison (Desktop, Tablet, Mobile)</summary>

#### **Responsive Comparison**
The card-based layout is highly flexible, automatically adjusting the number of columns to suit the user's screen width.

| Desktop View | Tablet View | Mobile View |
|:---:|:---:|:---:|
| [<img src="docs/screenshots/booking_dsktp.png" width="180">](docs/screenshots/booking_dsktp.png) | [<img src="docs/screenshots/booking_tab.png" width="120">](docs/screenshots/booking_tab.png) | [<img src="docs/screenshots/booking_mob.png" width="60">](docs/screenshots/booking_mob.png) |

</details>

### **Client Dashboard ("My Dashboard")**
The Client Dashboard serves as a personal management hub for patients, allowing them to track their upcoming sessions and manage their treatment schedule in real-time.

| Element Name | Description | Image Reference (Click to enlarge) |
|:---|:---|:---:|
| **Dashboard Header** | A clear section title ("My Appointments") that confirms the user is viewing their personal booking history. | [<img src="docs/screenshots/dashboard_title.png" width="180">](docs/screenshots/dashboard_title.png) |
| **Appointments Table** | A structured list displaying all future bookings with essential details: Date, Time interval, and the assigned Physiotherapist:<br> **Patient Comments** displays the specific notes or symptoms provided by the patient during the booking process, ensuring the reason for the visit is recorded. <br> **Cancellation Tool** - a dedicated "Cancel" button for each appointment. Clicking this removes the booking and immediately restores the slot's "Available" status for others.| [<img src="docs/screenshots/dashboard_table.png" width="180">](docs/screenshots/dashboard_table.png) |
| **New Booking CTA** | A primary blue button that redirects the user back to the **Choose a Physiotherapist Page** to schedule additional sessions. | [<img src="docs/screenshots/dashboard_new_booking.png" width="180">](docs/screenshots/dashboard_new_booking.png) |

<details>
<summary>Click to view Responsive Comparison (Desktop, Tablet, Mobile)</summary>

#### **Responsive Comparison**
The dashboard table is optimized for readability, ensuring that patients can easily manage their health schedule even on small mobile screens.

| Desktop View | Tablet View | Mobile View |
|:---:|:---:|:---:|
| [<img src="docs/screenshots/client_dash_dsktp.png" width="180">](docs/screenshots/client_dash_dsktp.png) | [<img src="docs/screenshots/client_dash_tab.png" width="120">](docs/screenshots/client_dash_tab.png) | [<img src="docs/screenshots/client_dash_mob.png" width="60">](docs/screenshots/client_dash_mob.png) |

</details>

### **Physiotherapist Dashboard**
The Physiotherapist Dashboard is a specialized management portal designed for medical staff. It provides a comprehensive overview of their professional profile and direct control over their daily schedule and patient interactions.

| Element Name | Description | Image Reference (Click to enlarge) |
|:---|:---|:---:|
| **Personal Greeting** | A personalized welcome header that confirms the professional's identity upon secure login. | [<img src="docs/screenshots/physio_welcome.png" width="180">](docs/screenshots/physio_welcome.png) |
| **Quick Info Block** | Displays the specialist's core professional data, such as their specific field of Physical Therapy and defined working hours. | [<img src="docs/screenshots/physio_quick_info.png" width="180">](docs/screenshots/physio_quick_info.png) |
| **Schedule Management CTA** | A prominent "Open schedule" button that leads to a detailed administrative view for managing vacations, breaks, and manual slot adjustments. | [<img src="docs/screenshots/physio_open_schedule.png" width="180">](docs/screenshots/physio_open_schedule.png) |
| **Upcoming Slots Table** | A real-time overview of the schedule, showing Available, Booked, and Blocked slots at a glance. | [<img src="docs/screenshots/physio_upcoming_table.png" width="180">](docs/screenshots/physio_upcoming_table.png) |
| **Internal Notes Tool** <br> **Emergency Cancellation** | For booked appointments, specialists can add private medical or administrative notes ("Internal note") that are not visible to patients. Allows the physiotherapist to cancel a booked session directly from the dashboard if necessary, automatically notifying the system. | [<img src="docs/screenshots/physio_notes_tool.png" width="180">](docs/screenshots/physio_notes_tool.png) |

<details>
<summary>Click to view Responsive Comparison (Desktop, Tablet, Mobile)</summary>

#### **Responsive Comparison**
The dashboard is fully responsive, allowing specialists to check their schedule or update patient notes on the go via tablet or smartphone.

| Desktop View | Tablet View | Mobile View |
|:---:|:---:|:---:|
| [<img src="docs/screenshots/staff_dash_dsktp.png" width="180">](docs/screenshots/staff_dash_dsktp.png) | [<img src="docs/screenshots/staff_dash_tab.png" width="120">](docs/screenshots/staff_dash_tab.png) | [<img src="docs/screenshots/staff_dash_mob.png" width="60">](docs/screenshots/staff_dash_mob.png) |

</details>

### **Physiotherapist Schedule Management**
This advanced administrative interface allows staff to have full granular control over their availability, patient bookings, and time blocking.

| Element Name | Description | Image Reference (Click to enlarge) |
|:---|:---|:---:|
| **Add Manual Slot** | A primary action button that redirects to a dedicated form for creating new time intervals in the schedule. | [<img src="docs/screenshots/schedule_add_btn.png" width="180">](docs/screenshots/schedule_add_btn.png) |
| **Comprehensive Table** | A detailed list of all slots with real-time status updates (Available, Booked, Blocked) and patient information. | [<img src="docs/screenshots/schedule_main_table.png" width="180">](docs/screenshots/schedule_main_table.png) |
| **Slot Blocking** | Specialists can block available slots for personal reasons (breaks, meetings). A "Reason" must be provided before clicking the yellow "Block" button. | [<img src="docs/screenshots/slot_manage.png" width="180">](docs/screenshots/slot_manage.png) |
| **Direct Deletion** | The red "Delete" button allows for the permanent removal of any slot from the database if it was created in error. | [<img src="docs/screenshots/slot_manage.png" width="180">](docs/screenshots/slot_manage.png) |
| **Create Slot Form** | A secure form featuring Django validation to prevent overlapping times. It allows for setting the Date, Start/End times, Status, and adding specific Client Notes. | [<img src="docs/screenshots/slot_dsktp.png" width="180">](docs/screenshots/slot_dsktp.png) |
| **Status Feedback** | An alert system (Django Messages) provides immediate confirmation of actions, such as "Slot status updated to Blocked." | [<img src="docs/screenshots/schedule_alert.png" width="180">](docs/screenshots/schedule_alert.png) |

<details>
<summary>Click to view Responsive Comparison (Desktop, Tablet, Mobile)</summary>

#### **Responsive Comparison**
The management table is designed with overflow handling, ensuring that staff can manage their schedule effectively even on smaller mobile devices during clinic rounds.

| Desktop View | Tablet View | Mobile View |
|:---:|:---:|:---:|
| [<img src="docs/screenshots/schedule_dsktp.png" width="180">](docs/screenshots/schedule_dsktp.png) | [<img src="docs/screenshots/schedule_tab.png" width="120">](docs/screenshots/schedule_tab.png) | [<img src="docs/screenshots/schedule_mob.png" width="60">](docs/screenshots/schedule_mob.png) |

</details>

## **Testing Accounts**
To facilitate comprehensive testing of role-specific functionalities, the following pre-configured accounts are available. 

> [!TIP]
> **Client Accounts:** While you can use the credentials below, we encourage creating a new account via the [Registration Page](#) to test the full user journey.

### **Physiotherapist Accounts (Staff Access)**
These accounts provide access to the **Physiotherapist Dashboard**, schedule management, and internal note-taking features.

| Specialization | Username | Password |
| :--- | :--- | :--- |
| **Superuser** | `Kateryna` | `23142314` |
| **Orthopedic** | `lilia_kraft` | `VaDhLQ@Xx3DP3d@` |
| **Neurological** | `anna_levski` | `2EhLA@vFJ77CqsL` |
| **Geriatric** | `melissa_kel` | `6Gpy6pULUaSi@Ry` |

### **Test Client Account (User Access)**
| Role | Username | Password |
| :--- | :--- | :--- |
| **Active Patient** | `test_client` | `Password123!` |

---

## **Features Overview**

### **1. Secure Authentication**
* **Multi-Role System:** Automated redirection logic that sends Physiotherapists to the Staff Dashboard and Clients to the Personal Booking Dashboard.
* **Identity Protection:** Secure registration for new clients with real-time validation.
* **Session Management:** Secure Login/Logout functionality with CSRF protection to prevent unauthorized access.

### **2. Patient (Client) Features**
* **Specialist Directory:** Browse a complete list of clinic physiotherapists with detailed professional profiles.
* **Real-time Booking:** View dynamic availability grids and book slots instantly.
* **Personalized Care:** Ability to leave symptoms or specific requests in a "Patient Note" during booking.
* **Appointment Management:** A dedicated "My Dashboard" to track upcoming visits or cancel appointments if plans change.

### **3. Medical Staff (Physiotherapist) Features**
* **Professional Dashboard:** Centralized view of the daily and weekly schedule.
* **Advanced Scheduling:** * **Time Blocking:** Ability to block slots for lunch, vacations, or holidays with a mandatory reason.
    * **Manual Slot Creation:** Add custom availability periods beyond standard hours.
* **Clinical Records:** Add "Internal Notes" to booked slots for private medical tracking (invisible to patients).
* **Administrative Control:** Full authority to cancel bookings or unblock previously restricted time periods.

---

## **Validation**

### **HTML Validation**
The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML structure of each page. All templates were checked by URI (for live Heroku pages) and by Direct Input (for authenticated views).

| Page | Status | Screenshot (Click to view) |
|:---|:---:|:---:|
| **Home Page** | Pass | [<img src="docs/validation/html_home.png" width="600">](docs/validation/html_home.png) |
| **Choose Physiotherapist** | Pass | [<img src="docs/validation/html_choose.png" width="600">](docs/validation/html_choose.png) |
| **Booking Selection** | Pass | [<img src="docs/validation/html_booking.png" width="600">](docs/validation/html_booking.png) |
| **Client Dashboard** | Pass | [<img src="docs/validation/html_client_dash.png" width="600">](docs/validation/html_client_dash.png) |
| **Physio Dashboard** | Pass | [<img src="docs/validation/html_staff_dash.png" width="600">](docs/validation/html_staff_dash.png) |
| **Login / Register** | Pass | [<img src="docs/validation/html_auth.png" width="600">](docs/validation/html_auth.png) |

---

### **CSS Validation**
The [W3C Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to test the custom `style.css` file.

| File | Status | Screenshot (Click to view) |
|:---|:---:|:---:|
| **style.css** | No Errors | [<img src="docs/validation/css_validation.png" width="600">](docs/validation/css_validation.png) |

---

### **JavaScript Validation (JSHint)**
The custom JavaScript used for the auto-dismissing alert messages was validated using [JSHint](https://jshint.com/).

| Metric | Result |
|:---|:---|
| **ES Version** | ES6 (Directively enabled via `/* jshint esversion: 6 */`) |
| **Errors** | 0 |
| **Warnings** | 0 |
| **Undefined Variables** | `bootstrap` (Expected as it is an external library loaded via CDN) |

 [<img src="docs/validation/js_val.png" width="900">](docs/validation/js_val.png)
---

### **Python (PEP8) Validation**

All custom Python logic across the project apps (`accounts`, `bookings`, `clinic`) has been validated against the [PEP8 Style Guide](https://peps.python.org/pep-0008/). 

To ensure high-quality, readable code, the following workflow was applied:
1. **Automated Formatting:** [autopep8](https://pypi.org/project/autopep8/) was used to resolve initial indentation and spacing issues.
2. **Manual Refactoring:** Complex logic and long strings (e.g., in `settings.py` and `views.py`) were manually refactored to fit the 79-character limit.
3. **Strict Verification:** Final validation was performed using the `pycodestyle` tool, excluding virtual environment and automatically generated migration files.

| App / File | Status | Validation Method |
|:---|:---:|:---|
| **Accounts App** | Pass | pycodestyle & autopep8 |
| **Bookings App** | Pass | pycodestyle & autopep8 |
| **Clinic App** | Pass | pycodestyle & autopep8 |
| **Project Configuration** | Pass | Manual refactoring & pycodestyle |

#### **PEP8 Terminal Verification**
The screenshot below confirms a "clean" run of the validation command, showing no PEP8 violations in the custom codebase.

[<img src="docs/validation/python_pep8_pass.png" width="700">](docs/validation/python_pep8_pass.png)
---

### **Lighthouse Audit**
Lighthouse was used to test the performance, accessibility, best practices, and SEO of the application for both Desktop and Mobile users.

| Page | Lighthouse (Desktop) | Lighthouse (Mobile) |
|:---|:---:|:---:|
| **Home Page** | [<img src="docs/validation/lh_home_dsktp.png" width="200">](docs/validation/lh_home_dsktp.png) | [<img src="docs/validation/lh_home_mob.png" width="200">](docs/validation/lh_home_mob.png) |
| **Choose Physiotherapist** | [<img src="docs/validation/lh_list_dsktp.png" width="200">](docs/validation/lh_list_dsktp.png) | [<img src="docs/validation/lh_list_mob.png" width="200">](docs/validation/lh_list_mob.png) |
| **Booking Selection** | [<img src="docs/validation/lh_book_dsktp.png" width="200">](docs/validation/lh_book_dsktp.png) | [<img src="docs/validation/lh_book_mob.png" width="200">](docs/validation/lh_book_mob.png) |
| **Client Dashboard** | [<img src="docs/validation/lh_client_dsktp.png" width="200">](docs/validation/lh_client_dsktp.png) | [<img src="docs/validation/lh_client_mob.png" width="200">](docs/validation/lh_client_mob.png) |
| **Physio Dashboard** | [<img src="docs/validation/lh_phis_db_dsktp.png" width="200">](docs/validation/lh_phis_db_dsktp.png) | [<img src="docs/validation/lh_phis_db_mob.png" width="200">](docs/validation/lh_phis_db_mob.png) |
| **Schedule** | [<img src="docs/validation/lh_schedule_dsktp.png" width="200">](docs/validation/lh_schedule_dsktp.png) | [<img src="docs/validation/lh_schedule_mob.png" width="200">](docs/validation/lh_schedule_mob.png) |
| **Create Slot** | [<img src="docs/validation/lh_slot_dsktp.png" width="200">](docs/validation/lh_slot_dsktp.png) | [<img src="docs/validation/lh_slot_mob.png" width="200">](docs/validation/lh_slot_mob.png) |
| **Register** | [<img src="docs/validation/lh_registr_dsktp.png" width="200">](docs/validation/lh_registr_dsktp.png) | [<img src="docs/validation/lh_registr_mob.png" width="200">](docs/validation/lh_registr_mob.png) |
| **Login** | [<img src="docs/validation/lh_login_dsktp.png" width="200">](docs/validation/lh_login_dsktp.png) | [<img src="docs/validation/lh_login_mob.png" width="200">](docs/validation/lh_login_mob.png) |
| **404 Page** | [<img src="docs/validation/lh_404_dsktp.png" width="200">](docs/validation/lh_404_dsktp.png) | [<img src="docs/validation/lh_404_mob.png" width="200">](docs/validation/lh_404_mob.png) |


---

### **WAVE Accessibility Audit**
The WAVE (Web Accessibility Evaluation Tool) was used to ensure the application is accessible. Secure pages were audited using the WAVE Browser Extension.

| Page | WAVE Result Image |
|:---|:---:|
| **Home Page** | [<img src="docs/validation/wave_home_1.png" width="250">](docs/validation/wave_home_1.png) [<img src="docs/validation/wave_home_2.png" width="250">](docs/validation/wave_home_2.png) | 
| **Choose Physiotherapist** | [<img src="docs/validation/wave_list_1.png" width="250">](docs/validation/wave_list_1.png) [<img src="docs/validation/wave_list_2.png" width="250">](docs/validation/wave_list_2.png)  | 
| **Booking Selection** | [<img src="docs/validation/wave_book_1.png" width="250">](docs/validation/wave_book_1.png)[<img src="docs/validation/wave_book_2.png" width="250">](docs/validation/wave_book_2.png)[<img src="docs/validation/wave_book_3.png" width="250">](docs/validation/wave_book_3.png) |
| **Client Dashboard** | [<img src="docs/validation/wave_client_1.png" width="250">](docs/validation/wave_client_1.png) [<img src="docs/validation/wave_client_2.png" width="250">](docs/validation/wave_client_2.png)|
| **Physio Dashboard** | [<img src="docs/validation/wave_phis_db_1.png" width="250">](docs/validation/wave_phis_db_1.png) [<img src="docs/validation/wave_phis_db_2.png" width="250">](docs/validation/wave_phis_db_2.png) [<img src="docs/validation/wave_phis_db_3.png" width="250">](docs/validation/wave_phis_db_3.png)|
| **Schedule** | [<img src="docs/validation/wave_schedule_1.png" width="250">](docs/validation/wave_schedule_1.png) [<img src="docs/validation/wave_schedule_2.png" width="250">](docs/validation/wave_schedule_2.png) [<img src="docs/validation/wave_schedule_3.png" width="250">](docs/validation/wave_schedule_3.png) [<img src="docs/validation/wave_schedule_4.png" width="250">](docs/validation/wave_schedule_4.png) [<img src="docs/validation/wave_schedule_5.png" width="250">](docs/validation/wave_schedule_5.png) |
| **Create slot** | [<img src="docs/validation/wave_slot_1.png" width="250">](docs/validation/wave_slot_1.png) [<img src="docs/validation/wave_slot_2.png" width="250">](docs/validation/wave_slot_2.png)|
| **Register** | [<img src="docs/validation/wave_register_1.png" width="250">](docs/validation/wave_register_1.png) [<img src="docs/validation/wave_register_2.png" width="250">](docs/validation/wave_register_2.png)|
| **Login** | [<img src="docs/validation/wave_login_1.png" width="250">](docs/validation/wave_login_1.png) [<img src="docs/validation/wave_login_2.png" width="250">](docs/validation/wave_login_2.png)|
| **404 Page** | [<img src="docs/validation/wave_404_1.png" width="250">](docs/validation/wave_404_1.png) [<img src="docs/validation/wave_404_2.png" width="250">](docs/validation/wave_404_2.png)|

---

### **Detailed Accessibility Summary**

| Category | Status | Observations |
|:---|:---:|:---|
| **Errors** | **0** | No red accessibility errors were identified across audited pages. |
| **Contrast Errors** | **0** | Text-to-background contrast ratios are compliant with WCAG standards. |
| **Features** | **High** | Proper use of alternative text for images and linked form labels. |
| **Structural Elements** | **Verified** | Correct hierarchy of headings (H1-H3) and use of semantic HTML5 landmarks. |
| **ARIA** | **Optimized** | ARIA roles and labels are used to enhance navigation for screen readers. |

## **Manual Testing**

To ensure the application is robust and secure, extensive manual testing was performed across all user roles. The testing focused on logical constraints, defensive design, and user feedback (Django Messages).

### **1. Authentication & Access Control**
The system uses custom decorators and logic to ensure users only access what they are authorized to see.

| Feature | Action | Expected Result | Actual Result | Status |
|:---|:---|:---|:---|:---:|
| **Role-Based Login** | Log in as a **Physiotherapist** | Automatically redirected to `physio_dashboard` | As expected | **Pass** |
| **Role-Based Login** | Log in as a **Client** | Automatically redirected to `client_dashboard` | As expected | **Pass** |
| **Unauthorized Access**| Try to access Physiotherapist views as a **Client** | System returns `403 Forbidden` (Access denied) | As expected | **Pass** |
| **Unauthorized Access**| Try to access Client Dashboard as a **Physio** | System returns `403 Forbidden` (Access denied) | As expected | **Pass** |
| **Unauthenticated** | Try to access any dashboard without logging in | Redirected to Login page immediately | As expected | **Pass** |

### **2. Patient (Client) Booking Flow**
Testing the "Happy Path" and edge cases for appointment management.

| Feature | Action | Expected Result | Actual Result | Status |
|:---|:---|:---|:---|:---:|
| **Slot Selection** | Click "Book" on an available slot | Redirected to specialist's booking page | As expected | **Pass** |
| **Booking Success** | Submit booking with an optional note | Slot status changes to "Booked", redirected to Dashboard | As expected | **Pass** |
| **Cancellation** | Cancel an upcoming appointment | Slot becomes "Available" for others, removed from dashboard | As expected | **Pass** |
| **Defensive Design** | Try to book a slot that has just passed | View filters out past slots automatically from the grid | As expected | **Pass** |
| **Past Data Protection**| Try to cancel a past appointment (yesterday) | No "Cancel" option available for historical data | As expected | **Pass** |

### **3. Staff (Physiotherapist) Management**
Testing schedule control and data integrity for medical staff.

| Feature | Action | Expected Result | Actual Result | Status |
|:---|:---|:---|:---|:---:|
| **Manual Creation** | Create a slot for a future date/time | Slot is saved and visible in the schedule | As expected | **Pass** |
| **Overlap Shield** | Try to create a slot at an existing time | Error: "A slot for this date and time already exists" | As expected | **Pass** |
| **Past Date Shield** | Try to create a slot for a past date | Form Validation Error: "You cannot create a slot in the past" | As expected | **Pass** |
| **Time Blocking** | Block an available slot with a reason | Status changes to "Blocked", reason is recorded | As expected | **Pass** |
| **Delete Safety** | Try to delete a slot that is already "Booked" | Error: "Please cancel the booking first" to protect data | As expected | **Pass** |
| **Internal Notes** | Update "Physio Note" on a patient's booking | Success message "Note updated", private data saved | As expected | **Pass** |
| **Staff Cancel** | Cancel a booking on behalf of a patient | Slot reset to "Available", Success message displayed | As expected | **Pass** |

---

### **Automated Testing**

Automated tests were implemented using the **Django Testing Framework** to ensure the reliability of the core booking logic and security constraints.

#### **1. Areas of Testing**
The test suite in `bookings/tests.py` focuses on:
* **Model Integrity:** Validating the `BookingSlot` data structure and string outputs.
* **Role-Based Access Control (RBAC):** Ensuring that clients cannot access physiotherapists' schedules and unauthorized users are redirected.
* **Defensive Design:**
    * Verifying that available slots can be successfully booked.
    * Ensuring that slots in the past **cannot** be booked, even if a request is sent directly to the URL.
* **Data Consistency:** Checking that `IntegrityError` is avoided by providing all required fields (like working hours) during profile creation.

#### **2. Test Execution & Results**
To run the tests, the following command was used:
`python3 manage.py test bookings`

**Results Summary:**
| Test Method | Purpose | Result |
|:---|:---|:---:|
| `test_slot_model_creation` | Validates BookingSlot model structure | **Pass** |
| `test_booking_home_access` | Verifies visibility of specialist list for clients | **Pass** |
| `test_physio_dashboard_protection` | Confirms security of staff-only views | **Pass** |
| `test_booking_process_success` | Validates end-to-end booking logic | **Pass** |
| `test_prevent_booking_past_date` | Confirms protection against historical bookings | **Pass** |

**Terminal Output Snapshot:**
```text
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 10.565s

OK
Destroying test database for alias 'default'...
```
---

## **Bugs**

### **Fixed Bugs**

During the development and testing phases, several bugs were identified and resolved. Special attention was given to Accessibility (WAVE) and Performance (Lighthouse) audits to ensure a professional user experience.

| # | Bug Title | Issue Description | Resolution |
|:---:|:---|:---|:---|
| **1** | **Static Files 404** | CSS styles and physiotherapist images returned 404 errors on the local server. | Corrected `STATICFILES_DIRS` in `settings.py` and added `staticfiles_urlpatterns` to `urls.py` for local debugging. |
| **2** | **Broken Profile Images** | Images didn't load because the template used a `slice` filter, looking for `A.webp` instead of `Anna.webp`. | Removed the `:slice` filter to ensure the filename matches the actual static asset name. |
| **3** | **Missing Form Labels** | WAVE Audit flagged 138 errors where form inputs lacked a linked `<label>` tag. | Added `<label>` tags with unique `id` attributes and used the `visually-hidden` class for screen reader accessibility. |
| **4** | **Orphaned Form Labels** | Labels existed but were not programmatically linked to their respective `textarea` or `input`. | Used the `for` attribute in labels to match the `id` of the input (e.g., `for="note-{{ slot.id }}"`). |
| **5** | **Low Contrast Errors** | Action buttons (`btn-outline-danger`) had insufficient contrast against the light blue `table-info` background. | Switched to solid Bootstrap classes (`btn-danger`, `btn-warning`) to meet WCAG AA contrast standards. |
| **6** | **Skipped Heading Levels** | Heading hierarchy jumped from `H1` to `H5`, confusing screen readers and search engines. | Realigned the hierarchy by changing `H5` to `H2`, maintaining the visual style via Bootstrap's `.h5` utility class. |
| **7** | **Empty Buttons** | Buttons containing only FontAwesome icons lacked descriptive text for accessibility. | Added `<span class="visually-hidden">` text and `aria-label` attributes to provide context to screen readers. |
| **8** | **Internal Server Error (500)** | The Schedule page crashed after an update to the table layout. | Identified a mismatch in column counts between `<thead>` and `<tbody>` and restored the missing "Time" column. |
| **9** | **Redundant Links** | Adjacent elements (titles and buttons) were pointing to the same URL, causing navigation "noise". | Added unique `aria-label` context to buttons to differentiate their purpose from surrounding text. |
| **10** | **Persistent Alerts** | Flash messages (success/error) remained on the screen indefinitely, obstructing the UI. | Implemented a JavaScript `setTimeout` function to automatically dismiss Bootstrap alerts after 15 seconds. |

---

### **Known Bugs**

* **Overlapping Slots:** Currently, the system allows a physiotherapist to manually create overlapping time slots. A validation logic to check for time conflicts is planned for the next version.
* **Browser Caching:** Due to aggressive static file caching, some layout changes might require a "Hard Refresh" (Ctrl+F5) to appear correctly for returning users.

---

### Known Issues

- No critical bugs detected at the time of submission.
- Minor UI differences may occur on very small screen widths, but functionality remains unaffected.

## Credits

### Content

All textual content used in this project, including physiotherapist descriptions, short bios, and interface copy, was generated with the assistance of artificial intelligence (AI).  
The content is fictional and intended solely for educational and demonstration purposes.

### Images

All images of physiotherapists displayed in this project were generated using artificial intelligence (AI).  
These images do not represent real individuals. Any resemblance to real persons, living or deceased, is purely coincidental.

The use of AI-generated images and content ensures that no real individuals are misrepresented and that no personal data is used without consent.

### Ethical Considerations

This project was developed as part of an educational portfolio.  
To avoid misinformation and the misuse of real identities, all names, images, and professional descriptions are fictional and AI-generated.

No real medical advice is provided by this application.

---

## Local Deployment

To run this project locally:

1. Clone the repository

```bash
git clone https://github.com/Katerynakulik/physio-clinic.git
cd physio-clinic
```

2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create .env file based on .env.example, including:

```bash
DEBUG=True
SECRET_KEY=<your secret key>
DATABASE_URL=sqlite:///db.sqlite3
```

5. Run migrations

```bash
python3 manage.py migrate
```

6. Run development server

```bash
python3 manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Conclusion & Mentor Evaluation

The **Physio Clinic** project successfully demonstrates a well-structured, full-stack Django application that meets the core requirements of a Full-Stack Toolkit portfolio project.

### Strengths of the Project

- **Clear CRUD implementation**
  - Clients can create, read, and delete bookings.
  - Physiotherapists can update slot statuses, unblock slots, and manage schedules.
  - Slot notes are properly handled and cleared when bookings are cancelled.

- **Role-based user experience**
  - Clients and physiotherapists have clearly separated dashboards.
  - Access control is enforced both in views and UI navigation.

- **User experience and validation**
  - Booking past time slots is prevented.
  - Booking without a required comment is blocked with user feedback.
  - Visual status indicators (Available / Booked / Blocked) improve usability.

- **Responsive and accessible design**
  - The application adapts well across desktop, tablet, and mobile devices.
  - Lighthouse scores above 90% demonstrate good performance, accessibility, and SEO practices.
