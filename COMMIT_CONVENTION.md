# Commit convention

This file will describe the norm used for commits in this repository.

This repository does not use the conventional commit down to the letter.

---

## Commit Message Convention

Each commit message must follow the format:
`[Infinitive verb] <concise description>`

- **Prefix**: The commit message should always begin with an action verb in its infinitive form. The verb should describe the type of change being made.
- **Description**: After the verb, provide a brief description of what has been done in that commit. Avoid past tense or gerunds (form of a verb that ends in "-ing" and functions as a noun in a sentence).
- **Body (Optional)**: There are no specific rules for the commit body. You can add details as necessary in subsequent lines.

### Examples

- `[ADD] a new service endpoint for user management`
- `[FIX] login endpoint handling edge cases`
- `[UPDATE] documentation with new examples`
- `[REMOVE] redundant code from the user service`
- `[EDIT] UI to match updated mockups`

### Common Commit Verbs

| Verb         | Description                                          | Example                                 |
|--------------|------------------------------------------------------|-----------------------------------------|
| **ADD**      | Introduces new functionality, features, or files     | `[ADD] cron jobs to clean expired tokens` |
| **FIX**      | Corrects bugs or issues in the codebase              | `[FIX] the database connection timeout` |
| **UPDATE**   | Improves or modifies existing functionality          | `[UPDATE] the login flow for better UX` |
| **REMOVE**   | Deletes or removes code, files, or dependencies      | `[REMOVE] outdated npm packages`        |
| **EDIT**     | Adjusts or alters existing code without major change | `[EDIT] the README for better clarity`  |
| **REFACTOR** | Refactors code without changing its behavior         | `[REFACTOR] server-side validation logic`|
| **RENAME**   | Renames files or variables                           | `[RENAME] variables to follow naming convention` |
| **MERGE**    | Merges branches or pull requests                     | `[MERGE] branch 'feature-auth' into dev`|

### Additional Notes

- **Prefixes** should always be in uppercase to clearly identify the action.
- Try to keep descriptions concise and to the point. Use the body for further elaboration if needed.
- If the commit is related to workflows or external dependencies, be explicit in the description.

### Examples from this Repository

- `[ADD] Sign In screens with social login buttons`
- `[FIX] SQL error in the database connection setup`
- `[UPDATE] the cron job to check expired tokens`
- `[REMOVE] unused imports in the backend code`
- `[EDIT] forgot password screen layout`
- `[REFACTOR] login and register code to improve readability`
- `[MERGE] remote-tracking branch 'origin/dev-back' into dev`
