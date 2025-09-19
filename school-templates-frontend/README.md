# School Templates Frontend

This is a minimal React + TypeScript frontend scaffold for the School Site.

Dev:
```powershell
cd school-templates-frontend
npm install
$env:REACT_APP_API_URL="http://localhost:8000/api"; npm start
```

Build:
```powershell
npm run build
# copy the build/ contents to Django static files or configure Django to serve the build
```

Backend integration notes are in the project root README.
# School Templates Frontend

This project is a React application that serves as a frontend for a school site. It is structured to utilize reusable templates for various components, ensuring a modular and maintainable codebase.

## Project Structure

```
school-templates-frontend
├── public
│   └── index.html          # Main HTML file for the application
├── src
│   ├── index.tsx          # Entry point of the React application
│   ├── App.tsx            # Main App component
│   ├── templates           # Contains reusable templates
│   │   ├── Header         # Header component
│   │   ├── Footer         # Footer component
│   │   ├── Layout         # Layout component
│   │   └── School         # School-related components
│   ├── components          # Reusable components
│   ├── pages               # Page components
│   ├── hooks               # Custom hooks
│   ├── services            # API service functions
│   ├── styles              # Global styles
│   └── types               # TypeScript types and interfaces
├── package.json            # npm configuration file
├── tsconfig.json           # TypeScript configuration file
└── README.md               # Project documentation
```

## Getting Started

To get started with the project, follow these steps:

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd school-templates-frontend
   ```

2. **Install dependencies:**
   ```
   npm install
   ```

3. **Run the application:**
   ```
   npm start
   ```

The application will be available at `http://localhost:3000`.

## Features

- Modular architecture with reusable templates for better maintainability.
- Custom hooks for handling API requests.
- TypeScript support for type safety.
- Global styles for consistent design across components.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.