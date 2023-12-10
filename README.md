# Vendor Management System with Performance Metrics

This Django-based Vendor Management System (VMS) is designed to handle vendor profiles, track purchase orders, and calculate vendor performance metrics. The system includes core features such as Vendor Profile Management, Purchase Order Tracking, and Vendor Performance Evaluation.

## Table of Contents
1. [Installation](#installation)
2. [API Endpoints](#api-endpoints)
   - [Vendor Profile Management](#1-vendor-profile-management)
   - [Purchase Order Tracking](#2-purchase-order-tracking)
   - [Vendor Performance Evaluation](#3-vendor-performance-evaluation)
3. [Backend Logic](#backend-logic)
4. [Additional Technical Considerations](#additional-technical-considerations)
5. [Technical Requirements](#technical-requirements)
6. [Deliverables](#deliverables)
7. [Submission Guidelines](#submission-guidelines)

## Installation

### Prerequisites
- Python (3.8 or higher)
- Django (latest stable version)
- Django REST Framework (latest stable version)

### Steps
1. Clone the repository:
   ```bash
   git clone git@github.com:sidddhesh100/fatmug-assingment.git
   cd fatmug-assingment
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Unix or MacOS:**
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Create migration files:
   ```bash
   python manage.py makemigrations
   ```

6. Apply migrations:
   ```bash
   python manage.py migrate
   ```

7. create a user:
   ```bash
   python manage.py createsuperuser
   ```
   To create user after running the above command enter username, email id and passowrd

8. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Postman Setup

Setup a postman collection to test the API endpoints

1. **Open Postman**
    - Launch the Postman application on your machine.

2. **Import the Collection**
    - In the Postman app, click on the "Import" button in the top-left corner.
    - Choose the option to "Import From File" and select the downloaded `fatmug.postman_collection.json` file.

4. **Verify Import**
    - Once imported, you should see the new collection in the left sidebar under "Collections."

5. **Environment Setup**
    - Replace the environment HOST_URL with python application running url
    - Also execute the get token api and add the token TOKEN environment variable

6. **Test API endpoints**
    - Test the below API endpoint by changing the request payload, query params and path strings

## API Endpoints

### 2. Create Token api

- **Create a new Toekn:**
  - Endpoint: `POST /api-token-auth/`
  - Request body: JSON data containing username and password used while creating user. Send the toke into request Header.

### 2. Vendor Profile Management

- **Create a new vendor:**
  - Endpoint: `POST /vendor/`
  - Header:
      Authorization: token {{TOKEN}}
  - Request body: JSON data containing vendor details.

- **List all vendors:**
  - Endpoint: `GET /vendors/`
  - Header:
      Authorization: token {{TOKEN}}

- **Retrieve a specific vendor's details:**
  - Endpoint: `GET /vendor/{vendor_id}/`
  - Header:
      Authorization: token {{TOKEN}}

- **Update a vendor's details:**
  - Endpoint: `PUT /vendor/{vendor_id}/`
  - Header:
      Authorization: token {{TOKEN}}
  - Request body: JSON data containing updated vendor details.

- **Delete a vendor:**
  - Header:
      Authorization: token {{TOKEN}}
  - Endpoint: `DELETE /vendor/{vendor_id}/`

### 3. Purchase Order Tracking

- **Create a purchase order:**
  - Endpoint: `POST /order/`
  - Header:
      Authorization: token {{TOKEN}}
  - Request body: JSON data containing purchase order details.

- **List all purchase orders:**
  - Endpoint: `GET /order/`
  - Header:
      Authorization: token {{TOKEN}}

- **Retrieve details of a specific purchase order:**
  - Endpoint: `GET /order/{po_id}/`
  - Header:
      Authorization: token {{TOKEN}}

- **Update a purchase order:**
  - Endpoint: `PUT /order/{po_id}/`
  - Header:
      Authorization: token {{TOKEN}}
  - Request body: JSON data containing updated purchase order details.

- **Delete a purchase order:**
  - Endpoint: `DELETE /order/{po_id}/`
  - Header:
      Authorization: token {{TOKEN}}

### 4. Vendor Performance Evaluation

- **Retrieve a vendor's performance metrics:**
  - Endpoint: `GET /vendor/{vendor_id}/performance`
  - Header:
      Authorization: token {{TOKEN}}

### Backend Logic

#### On-Time Delivery Rate:
- Calculated each time a PO status changes to 'completed'.
- Logic: Count the number of completed POs delivered on or before `delivery_date` and divide by the total number of completed POs for that vendor.

#### Quality Rating Average:
- Updated upon the completion of each PO where a `quality_rating` is provided.
- Logic: Calculate the average of all `quality_rating` values for completed POs of the vendor.

#### Average Response Time:
- Calculated each time a PO is acknowledged by the vendor.
- Logic: Compute the time difference between `issue_date` and `acknowledgment_date` for each PO, then find the average of these times for all POs of the vendor.

#### Fulfilment Rate:
- Calculated upon any change in PO status.
- Logic: Divide the number of successfully fulfilled POs (status 'completed' without issues) by the total number of POs issued to the vendor.

### Additional Technical Considerations

- **Efficient Calculation:**
  - Ensure that the logic for calculating metrics is optimized to handle large datasets without significant performance issues.

- **Data Integrity:**
  - Include checks to handle scenarios like missing data points or division by zero in calculations.

- **Real-time Updates:**
  - Consider using Django signals to trigger metric updates in real-time when related PO data is modified.
