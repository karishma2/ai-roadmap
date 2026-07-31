# Python vs JavaScript

## Side-by-Side Comparison

| Category | JavaScript | Python |
|---|---|---|
| Typical use | Frontend interactivity, web apps (browser/Node.js) | Data science, AI, scripting, backend services |
| Example — variable & print | `let name = "Karishma"; console.log(name);` | `name = "Karishma"\nprint(name)` |
| Example — user input | `const age = prompt("age");` | `age = input("age: ")` |
| Example — printing | `console.log(age)` | `print(age)` |
| Comments | `// single-line` and `/* multi-line */` | `# single-line` and `"""docstring"""` |
| Strings — uppercase | `name.toUpperCase()` | `name.upper()` |
| Strings — trim whitespace | `str.trim()` | `str.strip()` |
| Conditionals / logic | `if (...) { } else if (...) { }`, `&&`, `||`, `!` | `if ...: ... elif ...: ...`, `and`, `or`, `not` |
| Function (simple) | `const hello = () => "hi";` | `def hello(): return "hi"` |

## Conditionals / Logic Examples

JavaScript:
```javascript
if (x > 0) {
  console.log("positive");
} else if (x === 0) {
  console.log("zero");
} else {
  console.log("negative");
}

if (a > 0 && b > 0) {
  console.log("both positive");
}

if (!isDone) {
  console.log("not done");
}
```

Python:
```python
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

if a > 0 and b > 0:
    print("both positive")

if not is_done:
    print("not done")
```

## `switch` vs `match`

JavaScript uses `switch` for branching on discrete values. It is often used when a single expression can match several cases:
```javascript
switch (status) {
  case "ready":
    console.log("Ready!");
    break;
  case "waiting":
    console.log("Waiting...");
    break;
  default:
    console.log("Unknown state");
}
```

Python 3.10+ has `match` / `case`, which supports pattern matching and can branch on values, types, and structures:
```python
match status:
    case "ready":
        print("Ready!")
    case "waiting":
        print("Waiting...")
    case _:
        print("Unknown state")
```

For simple value-based branching, both are similar. Use `switch` in JavaScript and `match` in modern Python when you want a cleaner alternative to long `if` / `elif` chains.

## Quick Rules
- Choose JavaScript for interactive websites, client-side features, and event-driven apps.
- Choose Python for data work, AI/ML, automation, and rapid scripting.

## Notes / Key differences
- **Typing:** Both are dynamically typed; TypeScript adds static typing for JavaScript.
- **Syntax:** Python uses indentation for blocks; JavaScript uses braces and optional semicolons.
- **Runtime:** JavaScript commonly runs in browsers and Node.js; Python runs in CPython, PyPy, etc.
- **Concurrency:** JavaScript uses an event loop (async/await, Promises); Python has threads, asyncio, and the GIL considerations.
- **Package managers:** `npm` / `yarn` for JavaScript, `pip` / `pipenv` / `poetry` for Python.
- **When to pick:** Use JavaScript when you need browser integration or reactive UIs; use Python when you need rich data libraries or concise scripting.

If you want, I can also:
- apply additional formatting (examples as fenced code blocks),
- expand the comparison with performance, ecosystem, and learning resources.