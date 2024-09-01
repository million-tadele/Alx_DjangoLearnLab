## Permissions and Groups Setup

### Custom Permissions:
- `can_view`: Allows users to view books.
- `can_create`: Allows users to create new books.
- `can_edit`: Allows users to edit existing books.
- `can_delete`: Allows users to delete books.

### User Groups:
- **Editors**: Can create and edit books.
- **Viewers**: Can only view books.
- **Admins**: Have all permissions including the ability to delete books.

### Enforcing Permissions in Views:
- The `@permission_required` decorator is used in views to enforce permissions.
- Example: 
  - `@permission_required('your_app_name.can_edit', raise_exception=True)` is used to protect the edit book view.
