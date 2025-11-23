# Template Method Pattern - Example 2: Build Process

## Problem Description

Different software projects (Java, Python, JavaScript) have different build steps, but they all follow a similar process: fetch dependencies, compile, test, package, deploy. The Template Method pattern defines this process structure while allowing each project type to customize specific steps.

**Real-world usage**: Used in build tools (Maven, Gradle, npm), CI/CD pipelines, deployment frameworks, and code generation tools.

## Class Diagram

```
                    ┌─────────────────────┐
                    │   BuildProcess      │
                    │  (Abstract Class)   │
                    ├─────────────────────┤
                    │ + build()            │
                    │ # fetchDependencies()│
                    │ # compile()          │
                    │ # runTests()         │
                    │ # package()          │
                    │ # deploy()           │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
    ┌───────────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
    │  JavaBuild       │ │PythonBuild │ │JavaScriptBuild│
    ├──────────────────┤ ├────────────┤ ├──────────────┤
    │ # fetchDependencies()│ │ # fetchDependencies()│ │ # fetchDependencies()│
    │ # compile()      │ │ # compile()│ │ # compile() │
    │ # runTests()     │ │ # runTests()│ │ # runTests() │
    │ # package()      │ │ # package()│ │ # package() │
    └──────────────────┘ └────────────┘ └──────────────┘
```

