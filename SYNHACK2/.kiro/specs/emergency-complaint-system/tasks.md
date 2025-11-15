# Implementation Plan

- [x] 1. Database schema updates for emergency complaints
  - Add `is_emergency` boolean column to complaints table
  - Add `resolved_by` UUID column for warden reference
  - Add `resolved_at` timestamp column
  - Add `resolution_notes` text column
  - Create database index on `is_emergency` and `status` columns for optimized queries
  - _Requirements: 1.1, 1.2, 1.3, 3.2, 3.3, 6.1_

- [x] 2. Backend API endpoint for emergency complaint creation
  - [x] 2.1 Create POST `/api/complaints/emergency` endpoint in complaints route
    - Implement request validation for required fields (title, description, category, location, hostel)
    - Set `is_emergency: true` and `status: 'emergency'` on complaint creation
    - Store complaint in database with emergency flag
    - _Requirements: 1.1, 1.2, 1.3, 1.4_
  
  - [x] 2.2 Implement notification creation for warden and validator
    - Query database to find warden for student's hostel
    - Query database to find validator for student's hostel
    - Create notification records for both warden and validator
    - _Requirements: 2.1, 2.2, 2.3, 2.4_
  
  - [x] 2.3 Add role-based access control
    - Verify user has 'resident' role using @role_required decorator
    - Return 403 error if user is not a student
    - _Requirements: 1.1_

- [x] 3. Backend API endpoint for warden emergency resolution
  - [x] 3.1 Create POST `/api/admin/complaints/<complaint_id>/resolve-emergency` endpoint
    - Implement warden role verification using admin_role check
    - Validate complaint exists and is emergency type
    - Update complaint status to 'resolved'
    - Set resolved_by to warden's user_id and resolved_at to current timestamp
    - Store resolution_notes from request body
    - _Requirements: 3.1, 3.2, 3.3, 3.4_
  
  - [x] 3.2 Create notification for student on resolution
    - Create notification record for student who filed the complaint
    - Include resolution message and timestamp
    - _Requirements: 5.2_
  
  - [x] 3.3 Add validation checks
    - Check if complaint is already resolved (return 400 error)
    - Check if complaint is emergency type (return 400 error if not)
    - Check if user is warden (return 403 error if not)
    - _Requirements: 3.1, 3.2_

- [x] 4. Backend API endpoint for retrieving emergency complaints
  - [x] 4.1 Create GET `/api/admin/complaints/emergency` endpoint
    - Implement query to fetch complaints where `is_emergency = true`
    - Filter by warden's hostel assignment
    - Support optional status filter (emergency/resolved)
    - Join with users table to include student name and details
    - Order by created_at descending
    - _Requirements: 3.5, 4.1, 6.5_
  
  - [x] 4.2 Add role-based filtering
    - For wardens: show only their hostel's emergencies
    - For validators: show emergencies for awareness (read-only)
    - Return appropriate error if user is not warden or validator
    - _Requirements: 4.1, 4.2_

- [x] 5. Frontend emergency complaint submission form
  - [x] 5.1 Add emergency toggle to student complaint form
    - Add checkbox/toggle UI element for emergency flag
    - Display warning message when emergency is selected
    - Add visual indicator (red border/icon) for emergency mode
    - Update form state to track isEmergency boolean
    - _Requirements: 1.1, 1.5_
  
  - [x] 5.2 Update form submission logic
    - Route to `/api/complaints/emergency` endpoint when emergency is selected
    - Route to normal `/api/complaints` endpoint otherwise
    - Handle success/error responses appropriately
    - Display confirmation message on successful emergency submission
    - _Requirements: 1.1, 1.2, 1.3_
  
  - [x] 5.3 Update student dashboard to display emergency complaints
    - Add "Emergency" label/badge to emergency complaints in list view
    - Display distinct visual indicator (red color, icon)
    - Show resolution status and timestamp for resolved emergencies
    - _Requirements: 5.1, 5.2, 5.3, 5.4_

- [x] 6. Frontend warden portal emergency section
  - [x] 6.1 Create EmergencyComplaintsPanel component
    - Implement component structure with state management
    - Create layout with active and resolved sections
    - Add filter controls for hostel and status
    - _Requirements: 3.5, 4.1_
  
  - [x] 6.2 Implement emergency complaints list view
    - Fetch emergency complaints from API on component mount
    - Display complaints in card/list format with key details
    - Show student name, location, description, and timestamp
    - Add visual indicators for emergency status (icons, colors)
    - Implement auto-refresh every 30 seconds
    - _Requirements: 3.5, 4.1, 6.4_
  
  - [x] 6.3 Add "Mark as Resolved" functionality
    - Create resolution modal/form with notes input
    - Implement onClick handler for resolve button
    - Call `/api/admin/complaints/<id>/resolve-emergency` endpoint
    - Update UI to reflect resolved status
    - Show success message on resolution
    - _Requirements: 3.1, 3.2, 3.3_
  
  - [x] 6.4 Integrate emergency section into warden dashboard
    - Add emergency section to existing AdminDashboard component
    - Position emergency section prominently at top
    - Display count of active emergencies
    - Add navigation/tabs to switch between emergency and normal complaints
    - _Requirements: 3.5_

- [x] 7. Frontend validator dashboard emergency awareness
  - [x] 7.1 Add read-only emergency section to validator dashboard
    - Create emergency complaints view component
    - Fetch emergency complaints for validator's hostels
    - Display complaints in read-only format (no action buttons)
    - Add visual indicator that these are handled by wardens
    - _Requirements: 4.1, 4.2, 4.3_
  
  - [x] 7.2 Implement notification display for validators
    - Show notification badge for new emergency complaints
    - Display notification list with emergency alerts
    - Mark notifications as read when viewed
    - _Requirements: 2.2, 4.4_

- [x] 8. Notification system enhancements
  - [x] 8.1 Update notification polling logic
    - Modify frontend to poll `/api/notifications` every 30 seconds
    - Filter and display emergency notifications with high priority
    - Show badge count for unread emergency notifications
    - _Requirements: 2.3, 2.4_
  
  - [x] 8.2 Add notification panel UI
    - Create notification dropdown/panel component
    - Display list of recent notifications
    - Highlight emergency notifications with distinct styling
    - Add "Mark as Read" functionality
    - _Requirements: 2.1, 2.2, 2.4_

- [x] 9. Separate emergency complaints from normal workflow
  - [x] 9.1 Update complaint filtering logic
    - Exclude emergency complaints from validator's pending queue
    - Exclude emergency complaints from supervisor's assignment queue
    - Add filter option to show/hide emergency complaints
    - _Requirements: 6.2, 6.3, 6.5_
  
  - [x] 9.2 Update dashboard statistics
    - Add separate count for emergency complaints
    - Display emergency vs normal complaint metrics
    - Update existing stats queries to exclude emergencies where appropriate
    - _Requirements: 6.4_

- [x] 10. Integration and end-to-end testing
  - [x] 10.1 Test complete emergency workflow
    - Submit emergency complaint as student
    - Verify warden receives notification
    - Verify validator receives notification
    - Resolve complaint as warden
    - Verify student sees resolution
    - _Requirements: All_
  
  - [x] 10.2 Test access control and permissions
    - Verify only students can create emergency complaints
    - Verify only wardens can resolve emergency complaints
    - Verify validators have read-only access
    - Test unauthorized access attempts
    - _Requirements: 3.1, 3.4, 4.3_
  
  - [x] 10.3 Test edge cases and error handling
    - Test with missing required fields
    - Test resolving already resolved complaint
    - Test resolving non-emergency complaint
    - Test with invalid user roles
    - Verify appropriate error messages displayed
    - _Requirements: All_
