"""
Template Method Pattern - Build Process Example
Real-world usage: Build tools, CI/CD pipelines, deployment frameworks, code generation
"""

from abc import ABC, abstractmethod


class BuildProcess(ABC):
    """Abstract class defining the build template method"""
    
    def build(self):
        """Template method - defines the build algorithm skeleton"""
        print(f"\n🔨 Building {self.get_project_name()}...")
        print("=" * 60)
        self.fetch_dependencies()
        self.compile()
        self.run_tests()
        self.package()
        self.deploy()
        print("=" * 60)
        print(f"✅ Build completed for {self.get_project_name()}!")
    
    @abstractmethod
    def fetch_dependencies(self):
        """Abstract step - fetch project dependencies"""
        pass
    
    @abstractmethod
    def compile(self):
        """Abstract step - compile the project"""
        pass
    
    def run_tests(self):
        """Common step - can be overridden if needed"""
        print("3. Running tests...")
        print("   ✓ All tests passed")
    
    @abstractmethod
    def package(self):
        """Abstract step - package the project"""
        pass
    
    def deploy(self):
        """Common step - can be overridden if needed"""
        print("5. Deploying to production...")
        print("   ✓ Deployment successful")
    
    @abstractmethod
    def get_project_name(self) -> str:
        """Get project name"""
        pass


class JavaBuild(BuildProcess):
    """Concrete implementation - Java build process"""
    
    def fetch_dependencies(self):
        print("1. Fetching dependencies with Maven...")
        print("   Downloading: spring-boot, junit, lombok...")
        print("   ✓ Dependencies resolved")
    
    def compile(self):
        print("2. Compiling Java source files...")
        print("   javac -d target/classes src/main/java/**/*.java")
        print("   ✓ Compilation successful")
    
    def run_tests(self):
        print("3. Running JUnit tests...")
        print("   mvn test")
        print("   ✓ All tests passed")
    
    def package(self):
        print("4. Creating JAR package...")
        print("   mvn package")
        print("   ✓ Created: target/app.jar")
    
    def get_project_name(self) -> str:
        return "Java Application"


class PythonBuild(BuildProcess):
    """Concrete implementation - Python build process"""
    
    def fetch_dependencies(self):
        print("1. Installing dependencies with pip...")
        print("   pip install -r requirements.txt")
        print("   Installing: flask, pytest, requests...")
        print("   ✓ Dependencies installed")
    
    def compile(self):
        print("2. Checking Python syntax...")
        print("   python -m py_compile src/**/*.py")
        print("   ✓ Syntax check passed")
    
    def run_tests(self):
        print("3. Running pytest...")
        print("   pytest tests/")
        print("   ✓ All tests passed")
    
    def package(self):
        print("4. Creating wheel package...")
        print("   python setup.py bdist_wheel")
        print("   ✓ Created: dist/app-1.0.0-py3-none-any.whl")
    
    def get_project_name(self) -> str:
        return "Python Application"


class JavaScriptBuild(BuildProcess):
    """Concrete implementation - JavaScript build process"""
    
    def fetch_dependencies(self):
        print("1. Installing dependencies with npm...")
        print("   npm install")
        print("   Installing: react, webpack, jest...")
        print("   ✓ Dependencies installed")
    
    def compile(self):
        print("2. Bundling with Webpack...")
        print("   webpack --mode production")
        print("   ✓ Bundle created: dist/bundle.js")
    
    def run_tests(self):
        print("3. Running Jest tests...")
        print("   npm test")
        print("   ✓ All tests passed")
    
    def package(self):
        print("4. Creating production build...")
        print("   npm run build")
        print("   ✓ Created: build/ directory")
    
    def deploy(self):
        print("5. Deploying to CDN...")
        print("   Uploading to AWS S3...")
        print("   ✓ Deployment successful")
    
    def get_project_name(self) -> str:
        return "JavaScript Application"


class DockerBuild(BuildProcess):
    """Concrete implementation - Docker build process"""
    
    def fetch_dependencies(self):
        print("1. Pulling base images...")
        print("   docker pull node:18-alpine")
        print("   ✓ Base image ready")
    
    def compile(self):
        print("2. Building Docker image...")
        print("   docker build -t myapp:latest .")
        print("   ✓ Image built successfully")
    
    def run_tests(self):
        print("3. Running container tests...")
        print("   docker run --rm myapp:latest npm test")
        print("   ✓ All tests passed")
    
    def package(self):
        print("4. Tagging and pushing image...")
        print("   docker tag myapp:latest registry.io/myapp:v1.0")
        print("   ✓ Image tagged")
    
    def deploy(self):
        print("5. Deploying to Kubernetes...")
        print("   kubectl apply -f deployment.yaml")
        print("   ✓ Deployment successful")
    
    def get_project_name(self) -> str:
        return "Docker Application"


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("Template Method Pattern - Build Process Example")
    print("=" * 60)
    
    # Build different project types
    builds = [
        JavaBuild(),
        PythonBuild(),
        JavaScriptBuild(),
        DockerBuild()
    ]
    
    for build in builds:
        build.build()
        print()
    
    print("=" * 60)
    print("Key Benefit: Build process structure is defined once,")
    print("but each project type can customize specific steps!")
    print("=" * 60)

