# 🤝 Contributing to StudyFlow

Thank you for considering contributing to StudyFlow! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)

---

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of experience level, background, or identity.

### Expected Behavior

- Be respectful and considerate
- Use welcoming and inclusive language
- Accept constructive criticism gracefully
- Focus on what's best for the project
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Personal or political attacks
- Publishing private information
- Other unprofessional conduct

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic knowledge of Flask and web development
- Familiarity with HTML/CSS/JavaScript

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/HackDecouverteStudyApp.git
   cd HackDecouverteStudyApp
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/HackDecouverteStudyApp.git
   ```

### Set Up Development Environment

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize database**:
   ```bash
   python init_db.py
   ```

4. **Run development server**:
   ```bash
   python app.py
   ```

---

## 💡 How to Contribute

### Types of Contributions

We welcome:
- 🐛 **Bug fixes**
- ✨ **New features**
- 📝 **Documentation improvements**
- 🎨 **UI/UX enhancements**
- ⚡ **Performance optimizations**
- 🧪 **Test coverage**
- 🔧 **Code refactoring**

### Find an Issue

1. Browse [open issues](https://github.com/YOUR_REPO/issues)
2. Look for issues labeled:
   - `good first issue` - Great for newcomers
   - `help wanted` - We need assistance
   - `bug` - Something isn't working
   - `enhancement` - New feature or improvement

3. Comment on the issue to let others know you're working on it

### No Issue? Create One!

Before starting work on something new:
1. Check if an issue already exists
2. Create a new issue describing your idea
3. Wait for feedback from maintainers
4. Once approved, start working

---

## 🔄 Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# OR
git checkout -b fix/your-bug-fix
```

**Branch naming conventions**:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Adding tests

### 2. Make Changes

- Write clear, concise code
- Follow coding standards (see below)
- Add comments for complex logic
- Update documentation if needed

### 3. Test Your Changes

```bash
# Run the app and test manually
python app.py

# Test all features affected by your changes
# - Create test accounts
# - Create test sessions
# - Test edge cases
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat: add user profile pictures"
```

**Commit message format**:
```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples**:
```
feat: add file preview for images
fix: resolve chat message duplication bug
docs: update deployment guide with SSL instructions
refactor: simplify session creation logic
```

### 5. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 6. Create Pull Request

1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Select your branch
4. Fill out the PR template (see below)
5. Submit!

---

## 📏 Coding Standards

### Python (Backend)

**Style Guide**: Follow [PEP 8](https://pep8.org/)

```python
# Good
def calculate_session_duration(start_time, end_time):
    """
    Calculate duration between two times.
    
    Args:
        start_time (datetime): Session start time
        end_time (datetime): Session end time
    
    Returns:
        float: Duration in hours
    """
    duration = end_time - start_time
    return duration.total_seconds() / 3600

# Bad
def calc(s,e):
    return (e-s).total_seconds()/3600
```

**Best Practices**:
- Use descriptive variable names
- Add docstrings to functions
- Keep functions small and focused
- Avoid deep nesting (max 3 levels)
- Use list comprehensions for simple loops
- Handle errors with try/except blocks

### JavaScript (Frontend)

**Style Guide**: Use modern ES6+ syntax

```javascript
// Good
const messages = await fetchMessages(sessionId);
messages.forEach(msg => displayMessage(msg));

// Bad
var messages = fetchMessages(sessionId);
for (var i = 0; i < messages.length; i++) {
    displayMessage(messages[i]);
}
```

**Best Practices**:
- Use `const` and `let`, avoid `var`
- Use arrow functions
- Use template literals for strings
- Use async/await over callbacks
- Add comments for complex logic
- Use meaningful variable names

### HTML/CSS

**HTML**:
- Use semantic HTML5 elements
- Add ARIA labels for accessibility
- Keep nesting minimal
- Use proper indentation (2 or 4 spaces)

**CSS**:
- Follow BEM naming convention (optional)
- Use CSS variables for colors/spacing
- Mobile-first responsive design
- Keep specificity low
- Group related styles

```css
/* Good */
.session-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 16px;
    padding: 1.5rem;
}

.session-card__title {
    font-size: 1.5rem;
    font-weight: 700;
}

/* Bad */
div.card {
    background: purple;
    padding: 20px;
}
```

---

## 🧪 Testing Guidelines

### Manual Testing Checklist

Before submitting a PR, test:

- [ ] **Authentication**
  - [ ] Sign up with new account
  - [ ] Log in and out
  - [ ] Access protected pages without login (should redirect)

- [ ] **Sessions**
  - [ ] Create new session
  - [ ] Edit existing session
  - [ ] Delete session
  - [ ] Join session via invitation

- [ ] **Chat**
  - [ ] Send messages
  - [ ] Messages appear for other users (test in two browsers)
  - [ ] Upload files to chat

- [ ] **Files**
  - [ ] Upload study materials
  - [ ] Preview images and PDFs
  - [ ] Download files
  - [ ] Delete files (only as owner/creator)

- [ ] **Responsive Design**
  - [ ] Test on mobile (DevTools responsive mode)
  - [ ] Test on tablet
  - [ ] Test on desktop

- [ ] **Browser Compatibility**
  - [ ] Chrome/Edge
  - [ ] Firefox
  - [ ] Safari (if available)

### Automated Testing (Future)

We plan to add:
- Unit tests with pytest
- Integration tests
- End-to-end tests with Selenium

---

## 🔀 Pull Request Process

### Before Submitting

1. **Update from upstream**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Test thoroughly** (see checklist above)

3. **Update documentation** if needed

4. **Check code style**:
   ```bash
   # Format Python code
   black app.py
   
   # Check for issues
   flake8 app.py
   ```

### PR Template

When creating a PR, include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Testing
- [ ] Tested manually
- [ ] Added unit tests (if applicable)
- [ ] All existing tests pass

## Screenshots (if UI changes)
[Add screenshots here]

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed my code
- [ ] Commented complex code
- [ ] Updated documentation
- [ ] No breaking changes
- [ ] Tested on multiple browsers

## Related Issues
Closes #123
```

### Review Process

1. **Automated checks**: CI/CD runs (if configured)
2. **Code review**: Maintainer reviews code
3. **Feedback**: Address any requested changes
4. **Approval**: Once approved, PR is merged
5. **Celebration**: Your contribution is live! 🎉

---

## 🐛 Bug Reports

### Before Reporting

1. **Search existing issues** - Your bug may already be reported
2. **Try latest version** - Bug might be fixed
3. **Reproduce consistently** - Ensure it's reproducible

### Bug Report Template

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Screenshots
[Add screenshots if applicable]

## Environment
- OS: [e.g., Windows 11, macOS 14]
- Browser: [e.g., Chrome 120]
- Python version: [e.g., 3.10.5]

## Additional Context
Any other relevant information
```

---

## ✨ Feature Requests

### Feature Request Template

```markdown
## Feature Description
Clear description of the feature

## Problem It Solves
What problem does this solve?

## Proposed Solution
How should it work?

## Alternatives Considered
Any alternative solutions?

## Additional Context
Mockups, examples, or references
```

---

## 📞 Getting Help

- **Discord/Slack**: [If you have a community chat]
- **GitHub Discussions**: Ask questions
- **Documentation**: Check existing docs first
- **Email**: [maintainer email if public]

---

## 🙏 Recognition

All contributors will be:
- Listed in the project README
- Acknowledged in release notes
- Forever appreciated! ❤️

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to StudyFlow!** 🎉

Your efforts help make studying more collaborative and enjoyable for everyone.

---

**Last Updated**: November 30, 2025
