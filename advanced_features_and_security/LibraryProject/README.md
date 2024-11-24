# Permissions and Groups in Django 
## Custom Permissions 
The `Post` model includes the following custom permissions: 
- `can_view`: Allows viewing posts. 
- `can_create`: Allows creating posts. 
- `can_edit`: Allows editing posts. 
- `can_delete`: Allows deleting posts. 

## Groups 
The application defines the following groups: 
- `Viewers`: Assigned `can_view` permission. 
- `Editors`: Assigned `can_view`, `can_create`, and `can_edit` permissions. 
- `Admins`: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`). 

## How to Test 
1. Create test users and assign them to groups using the admin interface. 
2. Log in as these users and verify their access: 
- Viewers can only view posts. 
- Editors can view, create, and edit posts. 
- Admins can perform all actions, including deleting posts.