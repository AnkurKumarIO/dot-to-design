# Complaint Tracking System - Requirements

## Introduction

This document specifies requirements for a visual complaint tracking system that shows students the progress of their complaints through defined stages: Pending → Validated → Assigned → Completed.

## Glossary

- **Tracking System**: Visual progress indicator showing complaint status
- **Progress Bar**: Visual representation of complaint stages
- **Stage**: A specific step in the complaint resolution workflow
- **Student Dashboard**: Interface where students view their complaint progress
- **Admin Portals**: Validator, Supervisor, and Warden interfaces

## Requirements

### Requirement 1: Four-Stage Complaint Workflow

**User Story:** As a system administrator, I want complaints to follow a clear four-stage workflow, so that progress is standardized and trackable.

#### Acceptance Criteria

1. THE System SHALL define four complaint stages: "Pending", "Validated", "Assigned", "Completed"
2. WHEN a complaint is created, THE System SHALL set status to "Pending"
3. WHEN a validator approves a complaint, THE System SHALL set status to "Validated"
4. WHEN a supervisor assigns a complaint to a worker, THE System SHALL set status to "Assigned"
5. WHEN a worker completes a complaint, THE System SHALL set status to "Completed"

### Requirement 2: Visual Progress Tracking for Students

**User Story:** As a student, I want to see a visual progress bar showing my complaint's current stage, so that I know how far along the resolution process is.

#### Acceptance Criteria

1. THE System SHALL display a progress bar for each complaint in the student dashboard
2. THE System SHALL highlight the current stage in the progress bar
3. THE System SHALL show completed stages with a checkmark or green color
4. THE System SHALL show pending stages in gray or inactive color
5. THE System SHALL update the progress bar in real-time when status changes

### Requirement 3: Validator Portal Updates

**User Story:** As a validator, I want to see only pending complaints and validate them, so that I can focus on my specific role.

#### Acceptance Criteria

1. THE System SHALL show only complaints with status "Pending" in the validator portal
2. WHEN a validator clicks "Validate", THE System SHALL change status to "Validated"
3. THE System SHALL remove validated complaints from the validator's view
4. THE System SHALL display a count of pending validations

### Requirement 4: Supervisor Portal Updates

**User Story:** As a supervisor, I want to see only validated complaints and assign them to workers, so that I can manage work distribution.

#### Acceptance Criteria

1. THE System SHALL show only complaints with status "Validated" in the supervisor portal
2. WHEN a supervisor assigns a complaint, THE System SHALL change status to "Assigned"
3. THE System SHALL remove assigned complaints from the unassigned queue
4. THE System SHALL show assigned complaints in a separate "In Progress" section

### Requirement 5: Worker Portal Updates

**User Story:** As a worker, I want to see only my assigned complaints and mark them complete, so that I can focus on my tasks.

#### Acceptance Criteria

1. THE System SHALL show only complaints with status "Assigned" to the worker
2. WHEN a worker uploads completion photo, THE System SHALL change status to "Completed"
3. THE System SHALL remove completed complaints from the worker's active tasks
4. THE System SHALL show completed tasks in a history section

### Requirement 6: Progress Stage Indicators

**User Story:** As a user, I want to see clear visual indicators for each stage, so that I understand the complaint workflow.

#### Acceptance Criteria

1. THE System SHALL use distinct colors for each stage (gray=pending, blue=validated, orange=assigned, green=completed)
2. THE System SHALL display stage names clearly
3. THE System SHALL show connecting lines between stages
4. THE System SHALL use icons or checkmarks for completed stages
