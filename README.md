## Flask Application Design for Fixed-Income Backtesting Engine

**HTML Files**

- **index.html**:
    - Landing page for the application.
    - Provides a form for users to input parameters for backtesting.
    - Contains a button to trigger the backtesting process.

- **results.html**:
    - Displays the results of the backtesting process.
    - Includes visualizations such as charts and tables.
    - Provides download options for the results.

**Routes**

- **home**:
    - Maps to the landing page (index.html).

- **backtest**:
    - Receives the form data from the index page.
    - Initiates the backtesting process.
    - Redirects to the results page once the process is complete.

- **results**:
    - Maps to the results page (results.html).
    - Renders the backtesting results.

## Additional Considerations

- The backtesting process should be handled in a separate module or class to maintain code organization.
- The application should use a templating engine (e.g., Jinja2) for rendering HTML files dynamically.
- The application should include error handling mechanisms to gracefully handle any potential issues during the backtesting process.
- The application should be deployed on a web server or platform to make it accessible to users over the internet or intranet.