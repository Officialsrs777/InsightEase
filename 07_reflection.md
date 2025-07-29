# Reflection

1. **What I Learned**  
   - Gained hands-on experience defining problem statements, user stories, and roadmaps.
   - Integrated the Perplexity Sonar API into a Python workflow, understanding RESTful requests and environment-based key management.
   - Adopted environment variable management using #.env and #python-dotenv to keep secrets secure.
   - Practiced dependency management by generating #requirements.txt and applying #.gitignore best practices.

2. **Challenges & Solutions**  
   - Encountered #ModuleNotFoundError for #requests—resolved by installing dependencies (pip install -r requirements.txt) and documenting them.
   - Handled missing or invalid Sonar API keys gracefully with clear error messaging.
   - Refactored from OpenAI-specific SDK calls to a generic HTTP POST, updating payload structure and endpoint URL.
   - Ensured cross-platform file path compatibility in Git Bash on Windows by adjusting script invocation (py, python3) and path formats.

3. **Next Steps**  
   - Gather user feedback on summary quality and iterate on prompt engineering.  
   - Add automated tests and CI (GitHub Actions) to validate script functionality on each push.  
   - Extend the tool to support auto-transcription and calendar integrations for end-to-end meeting workflows.
   - Enhance developer onboarding documentation with usage examples, troubleshooting tips, and best practices.

