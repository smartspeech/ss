# FastHTML Todo App

A modern, responsive todo application built with FastHTML - a Python web framework that combines the simplicity of HTML with the power of Python.

## Features

- ✨ **FastHTML Framework**: Built with the modern FastHTML Python web framework
- 🎨 **Pico CSS**: Clean, semantic CSS framework for beautiful styling
- 📱 **Responsive Design**: Works perfectly on desktop and mobile devices
- 🗄️ **SQLite Database**: Simple, file-based database for data persistence
- 🔄 **Real-time Updates**: Dynamic todo management with instant feedback
- 🏷️ **Priority System**: High, medium, and low priority levels for todos
- ✅ **CRUD Operations**: Create, read, update, and delete todos

## Quick Start

### Option 1: Docker (Recommended)

1. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

2. **Or build and run manually:**
   ```bash
   docker build -t fasthtml-todo .
   docker run -p 5001:5001 fasthtml-todo
   ```

### Option 2: Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

3. **Open your browser:**
   Navigate to `http://localhost:5001`

## Project Structure

```
.
├── main.py              # Main FastHTML application
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker container configuration
├── docker-compose.yml  # Docker Compose configuration
├── .dockerignore       # Docker build exclusions
├── data/               # SQLite database directory (auto-created)
└── README.md           # This file
```

## API Endpoints

- `GET /` - Main page with todo list
- `POST /add_todo` - Add a new todo
- `GET /toggle_todo/{id}` - Toggle todo completion status
- `GET /delete_todo/{id}` - Delete a todo

## Database Schema

The app uses a simple SQLite database with the following structure:

```python
class Todo:
    id: int          # Unique identifier
    title: str       # Todo title
    done: bool       # Completion status
    priority: str    # Priority level (high/medium/low)
    created_at: str  # Creation date
```

## Customization

### Styling
The app includes custom CSS for:
- Priority-based color coding (red for high, orange for medium, green for low)
- Completed todo styling with strikethrough
- Responsive layout and spacing

### Adding Features
FastHTML makes it easy to extend the application:
- Add new routes with the `@rt` decorator
- Create new database models
- Integrate additional CSS frameworks
- Add JavaScript functionality

## Docker Configuration

The Dockerfile includes:
- Python 3.11 slim base image
- Optimized layer caching
- Health checks
- Proper volume mounting for development
- System dependencies for building packages

## Development

### Hot Reload
When running locally, FastHTML provides automatic reloading for development.

### Database Persistence
The SQLite database is stored in the `data/` directory and persists between container restarts when using Docker volumes.

## Production Deployment

For production deployment:
1. Remove development volumes from docker-compose.yml
2. Set appropriate environment variables
3. Use a production WSGI server
4. Configure reverse proxy (nginx) if needed
5. Set up proper logging and monitoring

## Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Change port in docker-compose.yml or use different port
   docker-compose up -p 5002
   ```

2. **Database permissions:**
   ```bash
   # Ensure data directory has proper permissions
   chmod 755 data/
   ```

3. **Dependencies not found:**
   ```bash
   # Rebuild Docker image
   docker-compose build --no-cache
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Learn More

- [FastHTML Documentation](https://github.com/fasthtml/fasthtml)
- [Pico CSS Framework](https://picocss.com/)
- [HTMX Documentation](https://htmx.org/docs/)