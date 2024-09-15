# Care-Connect

Care-Connect is a comprehensive patient, doctor, and hospital management system built using the Django MVT (Model-View-Template) framework. The primary goal of this project is to streamline hospital operations by enabling hospital staff to manage patients, doctors, hospital branches, and patient appointments, while also providing doctors with a platform to view and manage their appointments.

# Features

## User Authentication & Role-Based Access Control
Secure Authentication: Provides role-based access for hospital staff, receptionists, and doctors.
Restricted Registration: Only hospital staff can create credentials for receptionists, ensuring secure and controlled access. There is no public registration page available.
Doctor Management: Staff or receptionists can add and manage doctors, and share login credentials with doctors for their access.


## Hospital Staff (Admin/Help Desk/Receptionist) Features
Patient Management: Add, update, and view detailed patient records.
Doctor Management: Add, update, and view doctor information and availability.
Appointment Scheduling: Easily schedule patient appointments through a user-friendly calendar interface.
Medical Records Management: Store and manage electronic health records (EHR) including diagnoses, treatments, and lab results, for easy access and retrieval.

## Doctors 
 Doctors can login check their patient appointments.

# Installation

To get started with Care-connect, follow these installation steps:

    1. Clone the repository to your local machine:
      
          git clone https://github.com/narendrayalamanchi/Care-Connect.git
          
    2. Create a virtual environment and activate it:
      
        python -m venv venv
        .\venv\Scripts\activate
        
    3. Install project dependencies:
      
      pip install -r requirements.txt
      
    4. Configure your database settings in the settings.py file.
      
       Apply database migrations:
       
       python manage.py migrate
    
    5. Create a superuser account:
      
       python manage.py createsuperuser
     
    6. Start the development server:
       
       python manage.py runserver

