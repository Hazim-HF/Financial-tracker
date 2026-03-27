import sys
from django.conf import settings
from django.urls import path
from django.http import HttpResponse
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application

# 1. Manual Settings Configuration
settings.configure(
    DEBUG=True,
    SECRET_KEY="a-very-secret-key-for-local-testing",
    ROOT_URLCONF=__name__,
)

# 2. The View (Your Logic)
def home(request):
    return HttpResponse("""
        <body style="font-family: sans-serif; text-align: center; padding: 50px;">
            <h1>One-File Django App 🚀</h1>
            <p>Yes, it works!</p>
            <p>Hazim Fitri bin Ahmad Faudzi</p>
        </body>
    """)

# 3. The Routing
urlpatterns = [
    path("", home),
]

# 4. The Execution Logic
if __name__ == "__main__":
    execute_from_command_line(sys.argv)

app = get_wsgi_application()
