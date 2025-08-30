from fasthtml.common import *

# Create the FastHTML app with Pico CSS enabled
app, rt = fast_app(
    pico=True,  # Enable Pico CSS framework
    hdrs=(
        # Add some custom styling
        Style("""
            .todo-item { margin: 10px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }
            .todo-done { background-color: #f0f8f0; text-decoration: line-through; }
            .priority-high { border-left: 4px solid #ff4444; }
            .priority-medium { border-left: 4px solid #ffaa00; }
            .priority-low { border-left: 4px solid #44aa44; }
        """),
        # Add HTMX for dynamic interactions
        Script(src="https://unpkg.com/htmx.org@1.9.10"),
    )
)

# Create database and tables
db = database('data/todos.db')

class Todo:
    id: int
    title: str
    done: bool
    priority: str
    created_at: str

todos = db.create(Todo, transform=True)

# Sample data
if not todos.all():
    todos.insert([
        Todo(title="Learn FastHTML", done=False, priority="high", created_at="2024-01-01"),
        Todo(title="Build a web app", done=False, priority="medium", created_at="2024-01-01"),
        Todo(title="Deploy with Docker", done=False, priority="low", created_at="2024-01-01")
    ])

@rt
def index():
    """Main page with todo list"""
    return Titled(
        "FastHTML Todo App",
        H1("FastHTML Todo App"),
        P("A simple todo application built with FastHTML"),
        
        # Add new todo form
        Form(
            H2("Add New Todo"),
            Div(
                Label("Title:"),
                Input(name="title", required=True, placeholder="Enter todo title"),
                Label("Priority:"),
                Select(
                    Option("high", value="high"),
                    Option("medium", value="medium"),
                    Option("low", value="low"),
                    name="priority"
                ),
                Button("Add Todo", type="submit"),
                cls="form-group"
            ),
            action="/add_todo",
            method="POST",
            cls="add-todo-form"
        ),
        
        # Todo list
        H2("Your Todos"),
        Div(
            *[render_todo(todo) for todo in todos.all()],
            cls="todo-list"
        ),
        
        # Footer
        Footer(
            P("Built with FastHTML - A modern Python web framework"),
            cls="footer"
        )
    )

@rt
def add_todo(req):
    """Add a new todo"""
    form_data = await req.form()
    title = form_data.get("title", "").strip()
    priority = form_data.get("priority", "medium")
    
    if title:
        new_todo = Todo(
            title=title,
            done=False,
            priority=priority,
            created_at=datetime.now().strftime("%Y-%m-%d")
        )
        todos.insert(new_todo)
    
    return RedirectResponse("/", status_code=303)

@rt
def toggle_todo(todo_id: int):
    """Toggle todo completion status"""
    todo = todos.get(todo_id)
    if todo:
        todo.done = not todo.done
        todos.update(todo)
    
    return RedirectResponse("/", status_code=303)

@rt
def delete_todo(todo_id: int):
    """Delete a todo"""
    todos.delete(todo_id)
    return RedirectResponse("/", status_code=303)

def render_todo(todo):
    """Render a single todo item"""
    priority_class = f"priority-{todo.priority}"
    done_class = "todo-done" if todo.done else ""
    
    return Div(
        Div(
            H3(todo.title, cls="todo-title"),
            P(f"Priority: {todo.priority.title()}", cls="todo-priority"),
            P(f"Created: {todo.created_at}", cls="todo-date"),
            cls="todo-info"
        ),
        Div(
            Button(
                "✓" if not todo.done else "↺",
                onclick=f"window.location.href='/toggle_todo/{todo.id}'",
                cls="btn btn-success" if not todo.done else "btn btn-warning"
            ),
            Button(
                "🗑️",
                onclick=f"if(confirm('Delete this todo?')) window.location.href='/delete_todo/{todo.id}'",
                cls="btn btn-danger"
            ),
            cls="todo-actions"
        ),
        cls=f"todo-item {priority_class} {done_class}"
    )

# Run the application
if __name__ == "__main__":
    serve()
