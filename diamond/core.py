# core.py
import os # For the clear
import time # For wait()
import random # RNG, going to add more things soon
import math # Advanced math
import turtle # Arrow
import readline # QOL improvement
import importlib # Custom libraries
import sys # Proper globals

# -----------------------------
# Core Functions
# -----------------------------

def write(text=""):
    """Diamond-safe print (handles Unicode issues)."""
    try:
        print(text)
    except UnicodeEncodeError:
        safe_text = text.encode("utf-16", "surrogatepass").decode("utf-16", "ignore")
        print(safe_text)

def ask(question):
    return input(question)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(seconds):
    time.sleep(seconds)

# -----------------------------
# Arrow Class
# -----------------------------

class Arrow:
    def __init__(self, name):
        self.name = name
        self._turtle = turtle.Turtle()

    def line(self, distance, color="black"):
        self._turtle.pencolor(color)
        self._turtle.forward(distance)

    def turn(self, angle):
        self._turtle.right(angle)

    def rect(self, width, height, color="white", outline="black"):
        self._turtle.pencolor(outline)
        self._turtle.fillcolor(color)
        self._turtle.begin_fill()
        for _ in range(2):
            self._turtle.forward(width)
            self._turtle.right(90)
            self._turtle.forward(height)
            self._turtle.right(90)
        self._turtle.end_fill()

# -----------------------------
# Arrow Management
# -----------------------------

arrows = {}

def activate(name):
    if name in commands:
        write(f"Error: {name} already exists.")
        return
    new_arrow = Arrow(name)
    arrows[name] = new_arrow
    commands[name] = new_arrow
    setattr(sys.modules["diamond"], name, new_arrow)
    rebuild_sandbox()
    return new_arrow

# -----------------------------
# Anti-Print
# -----------------------------

def block_print(*args, **kwargs):
    write("What the heck are you doing? This is Diamond, not Python! Use write() instead!")

# -----------------------------
# Help Function
# -----------------------------

def help():
    write("Welcome to Diamond! Here are the available commands:\n")
    for cmd in commands:
        print(cmd)

# -----------------------------
# Math
# -----------------------------

def calculate(num1, operator, num2):
    if operator == "+":
      return num1 + num2
    elif operator == "-":
      return num1 - num2
    elif operator == "*":
      return num1 * num2
    elif operator == "/":
      return num1 / num2
    elif operator == "%":
      return num1 % num2
    elif operator == "//":
      return num1 // num2
    elif operator == "**":
      return num1 ** num2
    else:
      print("Error: Couldn't compute")

# -----------------------------
# Downloading custom libraries
# -----------------------------

def download(lib_name):
    global sandbox
    try:
        # Dynamically import the module from diamond.stdlib
        mod = importlib.import_module(f"diamond.stdlib.{lib_name}")

        # Ensure the diamond module has the attribute `rng` (or any other lib_name) directly
        globals()[f"diamond"] = sys.modules["diamond"]
        sys.modules["diamond"].__dict__[lib_name] = mod

        # Optionally, add to sandbox
        sandbox[lib_name] = mod

        print(f"Library '{lib_name}' successfully downloaded and added to diamond.")
    except Exception as e:
        print(f"Error loading library: {e}")

# -----------------------------
# Command Dictionary
# -----------------------------

commands = {
    'write': write,
    'ask': ask,
    'clear': clear,
    'wait': wait,
    'activate': activate,
    'sqrt': math.sqrt,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'pi': math.pi,
    'e': math.e,
    'help': help,
    'calculate': calculate,
    'download': download
}

# -----------------------------
# Auto Sandbox
# -----------------------------

def make_sandbox(command_dict):
    sb = command_dict.copy()
    sb["__builtins__"] = {"print": block_print}  # block print in all REPL code
    return sb

def rebuild_sandbox():
    global sandbox
    sandbox = make_sandbox(commands)

rebuild_sandbox()  # initial build

# -----------------------------
# REPL
# -----------------------------

def run():
    write("Welcome to the Diamond REPL! (type exit to quit)")
    write("Tip: separate multiple commands on one line with semicolons.\n")
    while True:
        code = input(">>> ").strip()
        line = code.lstrip()
        words = line.split()
        first = words[0]
        if first == "import" or first == "from":
            print("Imports are not allowed")
            continue
        if code == "exit":
            break
        if not code:
            continue

        for stmt in code.split(";"):
            stmt = stmt.strip()
            if not stmt:
                continue
            try:
                exec(stmt, sandbox)
            except Exception as e:
                write(e)

